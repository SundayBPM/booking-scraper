from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from time import sleep
from .collect_hotel import collect_hotel

def scroll_and_load_all_results(page):
    """
    Continuously scrolls down the page and clicks 'Load more results' (if visible)
    until there are no more hotels to load.
    """

    try:
        load_more_xpath = '//button[span[text()="Load more results"]]'

        prev_count = -1
        selector = 'div[data-testid="property-card"]'

        while True:
            # Scrolling ke bawah
            page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
            sleep(5)

            # Hitung jumlah elemen/hotel
            elements = page.locator(selector).all()
            current_count = len(elements)

            print(f"Jumlah hotel: {current_count}")

            if current_count == prev_count:
                print("Sudah mencapai akhir. Tidak ada elemen baru")
                break

            prev_count = current_count
        sleep(5)

        # Collect all the hotel list
        hotel_list = collect_hotel(page, selector,prev_count)

        return hotel_list

    except PlaywrightTimeoutError as e:
        print(f"Terjadi error di scroll and load. {e}")
    