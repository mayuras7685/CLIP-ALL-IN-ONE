import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()
access_key = os.getenv('ACCESS_KEY')
base_url = "https://api.unsplash.com"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Authorization": f"Client-ID {access_key}"
# }


# def get_response(prefix, suffix):
#     url = prefix+suffix
#     # print(url)
#     # print(requests.get(f"{base_url}/photos/?client_id={access_key}"))
#     response = requests.get(f"{base_url}/photos/?client_id={access_key}")
#     print(response.status_code)
#     if response.status_code != 200:
#         print(f"Failed to retrieve URL: {url}")
#     return response

def get_response(prefix, suffix):
    url = prefix+suffix
    response = requests.get(url)
    return response

def get_soup(category):
    soup = BeautifulSoup(category.text, 'html.parser')
    print(soup.prettify())
    return soup


# def get_unsplash_urls_from_soup(soup):
#     unsplash_urls = []
#     for img in soup.find_all('img'):
#         try:
#             print(img)
#             # img_url = img['src']
#             img_url = img.get('src')
#             if img_url and 'https://images.unsplash.com/photo' in img_url:
#                 unsplash_urls.append(img_url)
#         except Exception as e:
#             print(f"Error extracting image URL: {e}")
#     return unsplash_urls

# main function which uses the api to retrieve photo
def scrape_unsplash_urls(categories):
    # category_image_urls = {}
    images_scraped = []
    for category in categories:
        # response = get_response(prefix, category)
        response = requests.get(f"{base_url}/search/photos", params={
            "query": category,
            "client_id": access_key,
            "per_page":1
        })
        if response.status_code == 200:
            # category_soup = get_soup(response)
            # images_scraped.extend(get_unsplash_urls_from_soup(category_soup))
            data = response.json()
            for image_data in data['results']:
                image_url = image_data['urls']['regular']
                images_scraped.append(image_url)
        else:
            print(f"Skipping category {category} due to request failure.")
    return images_scraped


def get_bbc_headlines_from_soup(soup):
    bbc_headlines = []
    # Find all the headlines using the "h3" tag and "gs-c-promo-heading" class
    headlines= soup.find_all("p")
    # Loop through each headline and print the text
    for headline in headlines:
        try:
            bbc_headlines.append(headline.get_text())
        except:
            pass
    return [i for i in bbc_headlines if len(i.split()) >=7]

def scrape_bbc_headlines(prefix, categories: list):
    headlines = []
    for category in categories:
        response = get_response(prefix, category)
        category_soup = get_soup(response)
        headlines.extend(get_bbc_headlines_from_soup(category_soup))
    return headlines

#testing...
# prefix = "https://unsplash.com/t/"
# test_category = ["travel", "nature"] 
# image = scrape_unsplash_urls(test_category)
# print(image)
# response = get_response(test_category)
# soup = get_soup(response)
# image_urls = get_unsplash_urls_from_soup("travel")

# print("Scraped Image URLs:", image_urls)
