from pprint import pprint

def collect_hotel(page,selector,prev_count):
    # selector = 'div[data-testid="property-card"]'
    hotel_list = []
    for i in range(prev_count):
        hotel = {}
        hotel_name = page.locator(selector).nth(i).locator('h3').text_content()
        hotel_link = page.locator(selector).nth(i).locator('h3 a').get_attribute('href')
        hotel_stars = page.locator(selector).nth(i).locator('div[data-testid="rating-stars"]').locator(':scope > div')
        stars = None
        if hotel_stars.count() > 0:
            stars = hotel_stars.count()
            # print('Bintang hotel',hotel_stars)

        else:
            hotel_stars = page.locator(selector).nth(i).locator('div[data-testid="rating-squares"]').locator(':scope > div')
            if hotel_stars.count() > 0:
                stars = hotel_stars.count() 
            else:
                stars = None

        hotel['hotel_name'] = hotel_name
        hotel['stars'] = stars
        hotel['link'] = hotel_link

        # print(hotel)

        hotel_list.append(hotel)
    
    # pprint(hotel_list)
    return hotel_list
    
