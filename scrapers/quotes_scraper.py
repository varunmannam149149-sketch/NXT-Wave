import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://quotes.toscrape.com/"


def scrape_quotes():
    """
    Scrape quotes from all available pages on Quotes to Scrape.
    """

    quotes = []
    current_url = BASE_URL

    while current_url:

        print(f"Scraping: {current_url}")

        try:
            response = requests.get(
                current_url,
                timeout=10
            )

            response.raise_for_status()

        except requests.RequestException as error:
            print(f"Failed to scrape {current_url}: {error}")
            current_url = None
            continue

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        quote_blocks = soup.select("div.quote")

        for quote_block in quote_blocks:

            try:
                text_element = quote_block.select_one(
                    "span.text"
                )

                author_element = quote_block.select_one(
                    "small.author"
                )

                tag_elements = quote_block.select(
                    "div.tags a.tag"
                )

                author_link_element = quote_block.select_one(
                    "span a"
                )

                quote_text = (
                    text_element.get_text(strip=True)
                    if text_element
                    else ""
                )

                author = (
                    author_element.get_text(strip=True)
                    if author_element
                    else ""
                )

                tags = [
                    tag.get_text(strip=True)
                    for tag in tag_elements
                ]

                author_url = ""

                if author_link_element:
                    relative_url = author_link_element.get(
                        "href",
                        ""
                    )

                    author_url = urljoin(
                        current_url,
                        relative_url
                    )

                quote_data = {
                    "source": "Quotes to Scrape",
                    "source_url": current_url,
                    "name_or_title": quote_text,
                    "category": "",
                    "price": "",
                    "rating": "",
                    "author": author,
                    "tags": ", ".join(tags),
                    "description": "",
                    "author_url": author_url
                }

                quotes.append(quote_data)

            except Exception as error:
                print(
                    f"Error processing a quote: {error}"
                )

        next_button = soup.select_one(
            "li.next a"
        )

        if next_button:
            next_url = next_button.get("href")
            current_url = urljoin(
                current_url,
                next_url
            )
        else:
            current_url = None

    return quotes


if __name__ == "__main__":

    results = scrape_quotes()

    
    print(f"Total quotes collected: {len(results)}")
    

    for quote in results[:5]:
        print(quote)