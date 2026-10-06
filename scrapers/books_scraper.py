import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


BASE_URL = "https://books.toscrape.com/"


#geathering bookd from every page of the website 
def scrape_books():
    
    books = []
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

        soup = BeautifulSoup(response.text, "html.parser")

        book_cards = soup.select("article.product_pod")

        for book in book_cards:

            try:
                title_element = book.select_one("h3 a")
                price_element = book.select_one(".price_color")
                availability_element = book.select_one(
                    ".availability"
                )
                rating_element = book.select_one(
                    ".star-rating"
                )

                title = (
                    title_element.get("title", "").strip()
                    if title_element
                    else ""
                )

                price = (
                    price_element.get_text(strip=True)
                    if price_element
                    else ""
                )

                availability = (
                    availability_element.get_text(
                        " ",
                        strip=True
                    )
                    if availability_element
                    else ""
                )

                rating = ""

                if rating_element:
                    rating_classes = rating_element.get("class", [])

                    rating_words = {
                        "One": "1",
                        "Two": "2",
                        "Three": "3",
                        "Four": "4",
                        "Five": "5"
                    }

                    for word, number in rating_words.items():
                        if word in rating_classes:
                            rating = number
                            break

                product_url = ""

                if title_element:
                    relative_url = title_element.get("href", "")
                    product_url = urljoin(
                        current_url,
                        relative_url
                    )

                book_data = {
                    "source": "Books to Scrape",
                    "source_url": product_url,
                    "name_or_title": title,
                    "category": "",
                    "price": price,
                    "rating": rating,
                    "author": "",
                    "tags": "",
                    "description": "",
                    "availability": availability
                }

                books.append(book_data)

            except Exception as error:
                print(f"Error processing a book: {error}")

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

    return books


if __name__ == "__main__":

    results = scrape_books()

    
    print(f"Total books collected: {len(results)}")
   

    for book in results[:5]:
        print(book)