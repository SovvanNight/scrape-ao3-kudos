from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from datetime import date
# note - need to do pip install xlrd, pip install openpyxl
# change the path and file name as needed to refer to your excel fic list
# change the path and file name at the end for where you want to export the end result



today = date.today()
d3 = today.strftime("%m/%d/%Y")

kudodf = pd.DataFrame(columns=["Kudoer", "FicLink", "ScrapeDate",])
print('made kudo dataframe')

ficlist = pd.read_excel('g://fewficsforkudos.xlsx', sheet_name='Sheet1', header=None, skiprows=1, names=['FicTitle', 'FicLink', 'Kudos', 'IsRemoved', 'FicRating'])
print('opened excel')
#print(ficlist)


#initialize number of fics checked and successful
nbrfics=0
nbrsuc=0

for index, row in ficlist.iterrows():
    nbrfics=nbrfics+1
    print(row['FicLink'])
    response = requests.get(row['FicLink'])
    #print(response)

    if response.status_code == 404:
        print('404-not found.')
    elif response.status_code == 200:
        print('Success!')
        nbrsuc=nbrsuc+1

        resp_text = response.text

        soup = BeautifulSoup(resp_text, 'html.parser')
        #print(soup.prettify()) if you want to see your html

        #here's what the html looks like:
        #      <p class="kudos">
        #       <a href="/users/Perky">
        #        Perky
        #       </a>

        kudo = soup.find("p", { "class" : "kudos" })

        if kudo != None:
            children = kudo.find_all("a")
            #print(children)

            for link in children:
                kudodf = kudodf.append({"Kudoer": link.text, "FicLink": row['FicLink'], "ScrapeDate": d3}, ignore_index=True)
            print(kudodf.shape)




# Delete bad data from dataFrame - "(collapse)", "and xx more users"
# seems to only be needed if you scrape from work/12345 and not work/12345/kudos but i'm leaving it in just in case
print("Final step: delete known bad data that ends up in the kudoer dataframe.")
indexNames = kudodf[ kudodf['Kudoer'] == '(collapse)' ].index
kudodf.drop(indexNames , inplace=True)
print(kudodf.shape)
indexNames = kudodf[kudodf['Kudoer'].str.contains(" more users")].index
kudodf.drop(indexNames , inplace=True)
print(kudodf.shape)

print("Number of titles attenpted:  ", nbrfics)
print("Number of titles successfully scraped:  ", nbrsuc)
kudodf.to_excel('g://kudoersample2.xlsx')




