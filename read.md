# NxtWave Web Scraping Assignment

## Introduction

This project is a web scraping and data processing assignment.

The main purpose of this project is to collect book data from the
Books to Scrape website and process the collected data.

The data is scraped, cleaned, validated and checked for duplicate
records before saving the final output.

## Website Used

Books to Scrape:

https://books.toscrape.com/

## Technologies Used

- Python
- Requests
- BeautifulSoup
- JSON
- VS Code

## Project Structure

NXT-Wave/
│
├── scrapers/
│   └── books_scraper.py
│
├── processing/
│   ├── cleaning.py
│   ├── validation.py
│   ├── deduplication.py
│   └── __init__.py
│
├── output/
│   └── deduplicated_data.json
│
├── tests/
│
├── main.py
├── requirements.txt
├── AI_USAGE.md
└── read.md

## Process Followed

### 1. Scraping

The scraper collects book information from all available pages of
the Books to Scrape website.

The following information is collected:

- Book name
- Price
- Rating
- Source
- Source URL
- Availability

A total of 1000 book records were collected.

### 2. Cleaning and Standardization

The collected data is cleaned before further processing.

The cleaning process includes:

- Removing unwanted spaces
- Cleaning price values
- Standardizing rating values
- Cleaning URLs
- Cleaning text fields

### 3. Validation

The cleaned records are checked to make sure that the required
fields contain valid information.

The validation result was:

- Valid records: 1000
- Invalid records: 0

### 4. Deduplication

Duplicate records are identified using the source URL and book name.

After deduplication:

- Records before deduplication: 1000
- Records after deduplication: 1000
- Duplicates removed: 0

### 5. Final Output

The final processed data is stored in:

`output/deduplicated_data.json`

The final output contains 1000 processed book records.

## How to Run

First activate the virtual environment.

Then install the required packages:

```bash
pip install -r requirements.txt