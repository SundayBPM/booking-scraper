from time import sleep

def filter_stars(page, stars):
    for i in stars:
        rating = page.locator('div[data-testid="filters-group"]:has-text("Property rating")')
        print(i)
        rating.locator(f'div[data-filters-item="class:class={i}"]').click()
        sleep(5)