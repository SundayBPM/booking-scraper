from playwright.sync_api import sync_playwright
from utils import visit_booking_homepage, scroll_and_load_all_results, search_booking_homepage, dismiss_login_popup, filter_stars

import json

def booking_list_scraping(stars, USER_AGENTS:dict, city_name: str = ""):
    """
    Orchestrates the Booking.com scraping process. It initializes the browser and page, performs
    a search for the specified city, continuously loads more results, and saves the final HTML to a file.
    """
    with sync_playwright() as p:
        # Initialize browser and visit Booking.com homepage
        page, context, browser = visit_booking_homepage(p, USER_AGENTS)

        # Perform the search on the homepage
        search_booking_homepage(page, city_name)

        # Check for and handle login popup on homepage
        dismiss_login_popup(page)

        # Filter hotel by stars
        filter_stars(page, stars)

        # Wait for search results container to ensure the page is loaded
        page.wait_for_selector('//div[@data-results-container="1"]')

        # Check for and handle login popup on homepage
        dismiss_login_popup(page)

        # Scroll and click "Load more results" until reaching the bottom
        hotel_list = scroll_and_load_all_results(page)

        with open(f'jsons/list hotel in {city_name}.json', 'w', encoding='utf-8') as f:
            json.dump(hotel_list, f, ensure_ascii=False, indent=4)


        


        # # Save final HTML to file
        # html_content = page.content()
        # with open(output_file, 'w', encoding='utf-8') as f:
        #     f.write(html_content)
        # print(f"Final page HTML saved to {output_file}")

        # Close the context and browser
        context.close()
        browser.close()