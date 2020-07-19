Readme file for scrape-ao3-kudos
as of 7/19/2020

This program begins with a list of fiction works posted to Archive of our Own.  The goal is to scrape the list of users who "give kudos" or like a work.
If the page for a fic says "Joeblow, ficfanatic, and superfan123 left kudos on this work!" your end resulting table will look like:

	Kudoer		FicLink						ScrapeDate
0	Joeblow		https://archiveofourown.org/works/12345/kudos	07/19/2020
1	ficfanatic	https://archiveofourown.org/works/12345/kudos	07/19/2020
2	superfan123	https://archiveofourown.org/works/12345/kudos	07/19/2020

I use a 3rd party scraper to get the work links for my own research, although I do intend to write my own scraper at some point.

The public version of the program posted here is set to pull the list of fics from "fewficsforkudos.xlsx" which is also provided here.

You will want to either paste the addresses of the works whose kudos you'd like to scrape into that file or create your own file, knowing that you'll have to change the code somewhat to refer to your file name and column headings.

Note that the scraper works best if you list your addresses in the format https://archiveofourown.org/works/4065589/kudos.  If you leave off the "/kudos" the program will skip locked fics.

If you have many works to scrape, I recommend doing them in batches so that your end result doesn't get too large--I scraped my fandom's works in sets of 500 and the resulting tables ranged from 20k-58k rows.

There are 3 possible results with a scrape of each fic:  
1) the fic will not be found, in which case the program prints a 404 message and moves to the next fic
2) the fic is foud and kudos are scraped, in which case the program prints "Success!" and then the shape of the dataframe after adding the kudoers.
3) the fic will be found but it does not have any kudos, in which case the program prints "Success!" but does not print the new shape because it did not change.

At the end the program lists how many fics were attempted and how many were successfully scraped.

There is a 3 second pause after each scrape--this is to avoid hitting AO3's servers too frequently and getting blocked (which happened to me before I added the pause).
