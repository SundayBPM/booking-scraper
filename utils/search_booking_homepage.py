import random

from utils.helper_methods import get_dates, random_delay, simulate_human_mouse  # Ensure these functions exist in your helper_methods module

def search_booking_homepage(page, city_name: str):
    """
    Performs the homepage search by entering the city name, selecting check-in and check-out dates,
    and clicking the search button.
    """
    # Fill in the search field
    page.type("xpath=//*[@name='ss']", city_name, delay=random.randint(50, 150))
    random_delay(1, 2)
    print(f"Entered city name: {city_name}")

    # Open the date selector
    page.click("xpath=//*[@data-testid='searchbox-dates-container']")
    random_delay(1, 2)

    # Pick check-in and check-out dates
    tomorrow_date, day_after_tomorrow_date = get_dates()
    page.click(f"xpath=//span[@data-date='{tomorrow_date}']")
    page.click(f"xpath=//span[@data-date='{day_after_tomorrow_date}']")
    random_delay(1, 2)
    print(f"Selected check-in: {tomorrow_date}, check-out: {day_after_tomorrow_date}")

    # Simulate human mouse movement before clicking the search button
    simulate_human_mouse(page)
    search_button = page.locator('form[aria-label="Search properties"]').locator('button:has-text("Search")')
    print(search_button.count())
    search_button.click()
    random_delay(5, 6)
    print("Clicked search button...")