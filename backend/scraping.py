import requests
from bs4 import BeautifulSoup


def get_response(prefix, suffix):
    url = prefix+suffix
    response = requests.get(url)
    return response

def get_soup(category):
    soup = BeautifulSoup(category.text, 'html.parser')
    return soup


def get_unsplash_urls_from_soup(soup):
    unsplash_urls = []
    for img in soup.find_all('img'):
        try:
            img_url = img['src']
            if 'https://images.unsplash.com/photo' in img_url:
                unsplash_urls.append(img_url)
        except:
            pass
    return unsplash_urls


def scrape_unsplash_urls(prefix, categories):
    # category_image_urls = {}
    images_scraped = []
    for category in categories:
        response = get_response(prefix, category)
        category_soup = get_soup(response)
        images_scraped.extend(get_unsplash_urls_from_soup(category_soup))
    return images_scraped