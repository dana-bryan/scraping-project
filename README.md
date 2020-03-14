# Web Scraping: WUFT

## What I scraped and what I wanted to get
I scraped the WUFT News website, specifically the environment section. I wanted to get the article headlines, dates and summaries from the first 39 pages (about 390 articles). This would show the most important environmental topics in Gainesville and discover a trend in what Gainesville environmental reporters at WUFT tend to focus on. It could also showcase some neglected environmental topics in Gainesville.

## Steps

### Step 1 The Fundamentals
I imported the necessary libraries (Beautiful Soup, requests, time and csv), set my base URL (the first page of the environment section on the WUFT website) and opened a new csv file for writing. I also wrote a header row for my csv, which included "Headings, Dates and Summaries."

### Step 2 The Function
I had to scrape every article off of the page. I did this with my `get_articles()` function. I defined the function with two arguments, soup and list. Afterward, I looked at the HTML of the page to determine what tag had all of the information in one article.

It was easier for me to focus on scraping the first article box of information than focusing on scraping all 39 pages at once. The information was in the container article with the class of `item-list.` I scraped the individual article information boxes by using `find_all` and put them in the variable `boxes.`

##### For Loop and Try and Except
Now, I needed to scrape the headline, date and summary from each individual article on the page. I did this by creating a for loop and a try and except within the for loop to find the needed information for each article, append it to an empty list called `list`, pause for 3 seconds (to look more human-like) and write it to a new row. The except prevents the loop from unexpectedly stopping because a headline, date or summary is missing. The list is caught and returned with `return list.`

This repeats until every article headline, date and summary is scraped off the page.

### Step 3 To Scrape Multiple Pages
After I was able to scrape the needed information off of the first page, I needed to do it for the other pages. I used requests and Beautiful Soup to get the URLs/pages and attach it to a variable. I called the `get_articles(soup, list)` function that I wrote earlier and placed it inside a variable, `list.`

Instead of writing partial links, I used this line of code `url = 'https://www.wuft.org/news/category/environment/page/' + str(i + 1)` to continue to move onto the next page. I could do this because of the way the pages I scraped were structured. The pages had the same URLs except for the ending number which changed depending on the page number.

All of this(Step 3) was in a for loop with a range of (1, 40), so the first 39 pages could be scraped, and the scraper would stop after the 39th page.

### Step 4 Close the File
The final step is to close the csv file that I created and opened earlier. I closed it with this final line of code `csvfile.close().`

## Unexpected Problems and Solutions
The biggest unexpected problem I encountered was forming the for loop inside the function using the try and except. I started my code by using print statements to ensure I was scraping the correct information, and mitigate future errors. However, I struggled to get rid of the print statements later on to produce a more professional-looking code that will write to a csv.

I solved this problem by looking over past projects and notes and contacting some outside help to help me. I think with time and practice I will get more comfortable changing my code to have zero print statements.  
