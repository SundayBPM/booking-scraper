import json

from booking_list_scraping import booking_list_scraping

# Define user-agents specific to each browser
with open('user_agents.json') as f:
    USER_AGENTS = json.load(f)



if __name__ == "__main__":
    booking_list_scraping(city_name='batam', 
                        output_file='sylhet.html', 
                        USER_AGENTS=USER_AGENTS,
                        stars=['4','5'])


