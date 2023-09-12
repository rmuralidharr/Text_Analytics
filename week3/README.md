# Presidential Speeches Scraper

This Python program scapes the presidential speeches from the website: http://millercenter.org/ and merges this data with presidential information on term and party from https://www.britannica.com/topic/Presidents-of-the-United-States-1846696

## This uses:
* Selenium (https://pypi.org/project/selenium/)
* Gecko Webdriver (https://github.com/mozilla/geckodriver/releases/tag/v0.33.0) 
* BeautifulSoup (https://pypi.org/project/beautifulsoup4/)
* Pandas (https://pypi.org/project/pandas/)

> **Firefox also needs to be installed on the machine.**

## To run:
1. Run scrape_presidential_speeches.py - this will create a csv file with the scraped data from millercenter.org
   * Stores temporary results in speeches.csv.
2. Run scrape_and_merge_president_info.ipynb - this will create a csv file with the presidential information from britannica.com
   * Stores temporary results in presidents.csv
3. The final output is found in **presidential_speeches.csv**.

> NOTE1: Changes to selenium, gecko webdriver, or beautifulsoup may require changes to the code. This was tested on a MacOS machine with Python 3.10.6 and the library versions indicated above.

> NOTE2: The websites that are scraped may change their format, which may require changes to the code. This was last tested on 08-09-2023.
