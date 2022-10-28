# Scrapy Framework
## Real example for scraping with ```Pandas``` from a website of [Dhaka Stock Exchange](https://www.dse.com.bd)

First of all, you need to know about the technology which are using for built this program.

## Built With
* [Python](https://www.python.org) - Programming language
* [Scrapy](https://docs.scrapy.org/en/latest/index.html) - Scrapy is a fast high-level web crawling and web scraping framework.
* [Pandas](https://pandas.pydata.org) - Powerful data structures for data analysis, time series, and statistics.

## Goal of the Project
In the first link there is a dropdown of Trading Code List (Search by Trading Code) which shows all the Company enlisted. You can select a Trading Code and see all the latest news of the company. In the second lisk there is a list of all companies with their Trading Code.

Use the following link of Bangladesh Stock exchange
* https://www.dse.com.bd/news_archive.php
* https://www.dse.com.bd/company_listing.php

### Mission and Vision
You have to use the scrapy framework for crawling and python generators for data processing. Your task would be to crawl the first ```250``` companies' news from the first link and take the company names from the second link. Out of the crawled data prepare a separate csv file.

The csv schema would be:
* Trading Code
* Company Name
* News Title
* News Text
* Post Date

## Installation Notes

Clone the repository from [GitHub](https://github.com/farjanul-nayem/scrapy-example-with-pandas) and create a virtual environment on destination directory by following command.

```
virtualenv venv
```

Activate the virtual environment

```
source venv/bin/activate
```

Install requirements dependencies

```
pip install -r requirements.txt
```

Now, You are ready to go for run the program and get the result. 

## Run and Results
Run the program by following the command line.
```
scrapy crawl dse
```

The output files will be in the ```output``` directory. If the program runs successfully, 3 types of output files will be generated. ```news_archive.csv```, ```company_listing.csv``` and ```combine_data.csv```

**news_archive.csv** will be contained:
* Trading Code
* News Title
* News
* Post Date

**company_listing.csv** will be contained:
* Trading Code
* Company Name

### Final and analysis output file
**combine_data.csv** is the final output file, which contained the expected data for each company:
* Trading Code
* Company Name
* News Title
* News
* Post Date

## Connect with developer
* [LinkedIn](https://www.linkedin.com/in/farjanuln/)
