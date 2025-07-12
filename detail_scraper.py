import json

from detail_scraping import extract_detail

# Define user-agents specific to each browser
with open('user_agents.json') as f:
    USER_AGENTS = json.load(f)

with open('jsons/list hotel in batam.json', 'r') as file:
    hotels = json.load(file)



if __name__ == "__main__":
    list_hotel = []

    for hotel in hotels:
        print(f'Extract {hotel['hotel_name']}')
        hotel_details = extract_detail(
            link = hotel['link'],
            USER_AGENTS = USER_AGENTS
        )

        list_hotel.append(hotel_details)
    
    output_json = "jsons/hotel_details.json"

    try: 
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(list_hotel, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(e)