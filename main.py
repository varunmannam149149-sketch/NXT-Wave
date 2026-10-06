from scrapers.books_scraper import scrape_books
from scrapers.quotes_scraper import scrape_quotes
from processing.cleaning import clean_records
from processing.validation import validate_records
from processing.deduplication import deduplicate_records, save_deduplicated_records


print("Starting NxtWave scraping assignment...")

# Step 1: Scrape
books = scrape_books()
print("Books scraped:", len(books))

# Scrape quotes
quotes = scrape_quotes()
print("Quotes scraped:", len(quotes))

# Step 2: Clean
# Step 2: Clean
all_records = books + quotes
cleaned_books = clean_records(all_records)
print("Records cleaned:", len(cleaned_books))

# Step 3: Validate
valid_books, invalid_books = validate_records(cleaned_books)
print("Valid records:", len(valid_books))
print("Invalid records:", len(invalid_books))
# Step 4: Remove duplicates
final_books = deduplicate_records(valid_books)
print("Final records:", len(final_books))

# Step 5: Save final data
output_file = save_deduplicated_records(final_books)
print("Final data saved to:", output_file)

print("Assignment completed successfully!")