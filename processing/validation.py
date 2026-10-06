from urllib.parse import urlparse


VALID_SOURCES = {
    "Books to Scrape",
    "Quotes to Scrape"
}


def is_valid_url(url):
    """
    Check whether a URL looks valid.
    """

    if not url:
        return False

    try:
        parsed = urlparse(url)

        return (
            parsed.scheme in ("http", "https")
            and bool(parsed.netloc)
        )

    except Exception:
        return False


def validate_record(record):
    """
    Validate one cleaned record.

    Returns:
        (True, []) if the record is valid
        (False, [errors]) if the record is invalid
    """

    errors = []

    # 1. Check source
    source = record.get("source", "")

    if source not in VALID_SOURCES:
        errors.append("Invalid or unknown source")

    # 2. Check title / quote
    title = record.get("name_or_title", "")

    if not title:
        errors.append("Missing name_or_title")

    # 3. Check source URL
    source_url = record.get("source_url", "")

    if not is_valid_url(source_url):
        errors.append("Invalid source_url")

    # 4. Check price
    price = record.get("price")

    if price is not None:
        if not isinstance(price, (int, float)):
            errors.append("Price is not numeric")

        elif price < 0:
            errors.append("Price cannot be negative")

    # 5. Check rating
    rating = record.get("rating")

    if rating is not None:

        if not isinstance(rating, (int, float)):
            errors.append("Rating is not numeric")

        elif not 1 <= rating <= 5:
            errors.append("Rating must be between 1 and 5")

    is_valid = len(errors) == 0

    return is_valid, errors


def validate_records(records):
    """
    Validate all records.

    Returns:
        valid_records
        invalid_records
    """

    valid_records = []
    invalid_records = []

    for record in records:

        is_valid, errors = validate_record(record)

        if is_valid:

            valid_records.append(record)

        else:

            invalid_records.append({
                "record": record,
                "errors": errors
            })

    return valid_records, invalid_records


if __name__ == "__main__":

    test_records = [

        {
            "source": "Books to Scrape",
            "source_url": "https://books.toscrape.com/",
            "name_or_title": "Example Book",
            "price": 25.99,
            "rating": 5
        },

        {
            "source": "Unknown Website",
            "source_url": "wrong-url",
            "name_or_title": "",
            "price": -10,
            "rating": 8
        }
    ]

    valid, invalid = validate_records(test_records)

    print("VALID RECORDS:")
    print(len(valid))

    print("\nINVALID RECORDS:")
    print(len(invalid))

    for item in invalid:
        print("\nErrors:")

        for error in item["errors"]:
            print("-", error)











