import re
from datetime import datetime
from urllib.parse import urlparse


def clean_text(value):
    """
    Remove unnecessary whitespace and normalize text.
    """

    if value is None:
        return ""

    value = str(value)

    # Replace multiple spaces/newlines with one space
    value = re.sub(r"\s+", " ", value)

    # Remove spaces at beginning and end
    value = value.strip()

    return value


def clean_price(value):
    """
    Convert price text such as '£51.77' into 51.77.
    """

    if value is None or value == "":
        return None

    value = str(value)

    # Keep only numbers and decimal point
    value = re.sub(r"[^0-9.]", "", value)

    try:
        return float(value)
    except ValueError:
        return None


def clean_rating(value):
    """
    Convert rating into an integer between 1 and 5.
    """

    if value is None or value == "":
        return None

    try:
        rating = int(value)

        if 1 <= rating <= 5:
            return rating

        return None

    except (ValueError, TypeError):
        return None


def clean_url(value):
    """
    Check whether a URL looks valid.
    """

    if not value:
        return ""

    value = str(value).strip()

    try:
        parsed = urlparse(value)

        if parsed.scheme in ("http", "https") and parsed.netloc:
            return value

    except Exception:
        pass

    return ""


def clean_tags(value):
    """
    Clean comma-separated tags.
    """

    if not value:
        return ""

    tags = str(value).split(",")

    cleaned_tags = []

    for tag in tags:
        tag = clean_text(tag)

        if tag:
            cleaned_tags.append(tag)

    return ", ".join(cleaned_tags)


def clean_record(record):
    """
    Clean one scraped record and convert it
    into the common standardized structure.
    """

    cleaned = {
        "source": clean_text(record.get("source")),
        "source_url": clean_url(record.get("source_url")),
        "name_or_title": clean_text(
            record.get("name_or_title")
        ),
        "category": clean_text(
            record.get("category")
        ),
        "price": clean_price(
            record.get("price")
        ),
        "rating": clean_rating(
            record.get("rating")
        ),
        "author": clean_text(
            record.get("author")
        ),
        "tags": clean_tags(
            record.get("tags")
        ),
        "description": clean_text(
            record.get("description")
        ),
        "scraped_at": datetime.utcnow().isoformat()
    }

    return cleaned


def clean_records(records):
    """
    Clean a list of records.
    """

    cleaned_records = []

    for record in records:
        cleaned_record_data = clean_record(record)
        cleaned_records.append(cleaned_record_data)

    return cleaned_records





if __name__ == "__main__":

    test_record = {
        "source": "  Books to Scrape  ",
        "source_url": "https://books.toscrape.com/",
        "name_or_title": "  Example   Book  ",
        "category": "  Fiction ",
        "price": "£25.99",
        "rating": "5",
        "author": "",
        "tags": " Python, Programming ",
        "description": "  A test book  "
    }

    result = clean_record(test_record)

    print(result)

    