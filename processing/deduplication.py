import json
import os
import sys

sys.path.append(".")

from processing.cleaning import clean_records
from scrapers.books_scraper import scrape_books

from processing.validation import validate_records








# =========================
# DEDUPLICATION
# =========================
def count_duplicates(records):
    """
    Count duplicate records without removing them.
    """

    seen = set()
    duplicate_count = 0

    for record in records:

        source_url = record.get("source_url", "").strip()
        name_or_title = record.get("name_or_title", "").strip()

        unique_key = (
            source_url.lower(),
            name_or_title.lower()
        )

        if unique_key in seen:
            duplicate_count += 1
        else:
            seen.add(unique_key)

    return duplicate_count

def deduplicate_records(records):
    """
    Remove duplicate records.

    A record is considered a duplicate when it has
    the same source URL and name/title.

    Returns:
        unique_records
    """

    unique_records = []
    seen = set()

    for record in records:

        source_url = record.get("source_url", "").strip()
        name_or_title = record.get("name_or_title", "").strip()

        unique_key = (
            source_url.lower(),
            name_or_title.lower()
        )

        if unique_key not in seen:

            seen.add(unique_key)
            unique_records.append(record)

    return unique_records


def save_deduplicated_records(records):
    """
    Save deduplicated records to the output folder.
    """

    output_folder = "output"

    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(
        output_folder,
        "deduplicated_data.json"
    )

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(
            records,
            file,
            indent=4,
            ensure_ascii=False
        )

    return output_file



# if __name__ == "__main__":

#     test_records = [

#         {
#             "source": "Books to Scrape",
#             "source_url": "https://books.toscrape.com/",
#             "name_or_title": "Example Book",
#             "price": 25.99,
#             "rating": 5
#         },

#         {
#             "source": "Books to Scrape",
#             "source_url": "https://books.toscrape.com/",
#             "name_or_title": "Example Book",
#             "price": 25.99,
#             "rating": 5
#         },

#         {
#             "source": "Quotes to Scrape",
#             "source_url": "https://quotes.toscrape.com/",
#             "name_or_title": "Example Quote",
#             "price": None,
#             "rating": None
#         },
#         {
#     "source": "Books to Scrape",
#     "source_url": "https://books.toscrape.com/",
#     "name_or_title": "example book",
#     "price": 25.99,
#     "rating": 5
# }
#     ]

#     print("DEDUPLICATION STARTED")

#     duplicate_count = count_duplicates(test_records)

#     print("Duplicate records detected:", duplicate_count)

#     print("Records before deduplication:", len(test_records))

#     unique_records = deduplicate_records(test_records)

#     print("Records after deduplication:", len(unique_records))

#     print("Duplicates removed:",
#           len(test_records) - len(unique_records))








if __name__ == "__main__":

    

    print("\nSCRAPING BOOKS...")

    books = scrape_books()

    print("Books scraped:", len(books))

    print("\nCLEANING BOOK DATA...")

    cleaned_books = clean_records(books)

    print("Books after cleaning:", len(cleaned_books))

    print("\nVALIDATING BOOK DATA...")

    valid_books, invalid_books = validate_records(cleaned_books)

    print("Valid books:", len(valid_books))
    print("Invalid books:", len(invalid_books))


    print("\nDEDUPLICATING VALID BOOK DATA...")

    deduplicated_books = deduplicate_records(valid_books)

    print("Books before deduplication:", len(valid_books))
    print("Books after deduplication:", len(deduplicated_books))
    print(
        "Duplicates removed:",
        len(valid_books) - len(deduplicated_books)
    )

    # your existing test_records section continues here
    print(
        "Duplicates removed:",
        len(valid_books) - len(deduplicated_books)
    )
    output_file = save_deduplicated_records(deduplicated_books)

    print("Final data saved to:", output_file)