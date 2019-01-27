from selenium import webdriver
from urllib import parse
import time
from bs4 import BeautifulSoup

from .models import Location, Sub_location, Pensions


def crawler(location, sub_location):
    driver = webdriver.Chrome()

    params = {
        'location': location.location_number,
        'subLocation': sub_location.sub_location_number,
    }
    url = 'http://www.yapen.co.kr/region?' + parse.urlencode(params)

    driver.get(url)
    driver.implicitly_wait(3)
    # SCROLL_PAUSE_TIME = 3
    # # Get scroll height
    # last_height = driver.execute_script("return document.body.scrollHeight")
    #
    # while True:
    #     # Scroll down to bottom
    #     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #
    #     # Wait to load page
    #     time.sleep(SCROLL_PAUSE_TIME)
    #
    #     # Calculate new scroll height and compare with last scroll height
    #     new_height = driver.execute_script("return document.body.scrollHeight")
    #     if new_height == last_height:
    #         break
    #     last_height = new_height

    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    get_ul = soup.findAll('ul', attrs={'class': 'dest-place-opt-fea'})
    img_src = soup.findAll('div', attrs={'class': 'imgBox'})

    title = []
    img = []
    ypidx = []

    for index, get_li in enumerate(get_ul):
        title.append(get_li.contents[3].get_text())

    for src in img_src:
        img_url = src.find('img').get('src')
        img.append(img_url)
        match = img_url[37:42]
        ypidx.append(match)

    for name, img, ypidx in zip(title, img, ypidx):
        Pensions.objects.create(sub_location=sub_location, name=name, pension_img=img, ypidx=ypidx)

    driver.close()



