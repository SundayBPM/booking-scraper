from time import sleep
from playwright.sync_api import sync_playwright, TimeoutError as playwrightTimeoutError
from utils import visit_hotel


def extract_detail(USER_AGENTS:dict, link, max_retries=3):
    list_hotel = []

    for attempt in range(max_retries+1):
        try:
            with sync_playwright() as p:
                page, context, browser = visit_hotel(p, USER_AGENTS=USER_AGENTS, link=link)

                hotel_name = page.locator('div[data-capla-component-boundary="b-property-web-property-page/PropertyHeaderName"]').text_content()
                page.locator('a[id="map_trigger_header"]').click()
                koor = page.locator('a[title="Open this area in Google Maps (opens a new window)"]').get_attribute('href')
                brand_loc = page.locator('div[data-testid="brand-name"]')
                brand = None

                if brand_loc.count() > 0:
                    brand = brand_loc.locator('xpath=(./div/div)[1]').text_content()
                
                data = {
                    'hotel_name': hotel_name,
                    'coordinate': koor,
                    'brand': brand
                }

                # print("hotel name", hotel_name)
                # print("Hotel koordinat ", koor)
                # print("Brand Hotel", brand)
                return data


        except Exception as e:
            print(f"   Error: {e}")
            
            delay = 3
            if attempt < max_retries:
                print(f"⏳ Menunggu {delay} detik sebelum mencoba ulang...")
                sleep(delay)
            else:
                print("🚫 Gagal setelah maksimal percobaan. Lewati hotel ini.")
                return []
            