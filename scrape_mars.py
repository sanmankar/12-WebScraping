# Import all the libraries
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests

def init_browser():
    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    #!which chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

def scrape():

    # Call the initialize browser function
    # https://splinter.readthedocs.io/en/latest/drivers/chrome.html
    #!which chromedriver
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # *************************************************************
    # Scrape NASA News Title and Paragraph



    #***********************************************************
    # Define URL and initialize the html parser
    news_url = "https://mars.nasa.gov/news"
    browser.visit(news_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    time.sleep(5)
    news_title = soup.find(class_='content_title')  

    #browser.quit()
   
    #***********************************************************
    # Define URL and scrape news_p
    time.sleep(5)
    news2_url = "https://mars.nasa.gov/news"
    browser.visit(news2_url)
    html = browser.html
    soup = bs(html, 'html.parser')

    time.sleep(10)
    news_p = soup.find(class_='article_teaser_body')

    #print(news_title.text)
    print('News Teaser :')
    print(news_p.text)

    #browser.quit()

    # *************************************************************
    # Scrape JPL Mars Space Images
    time.sleep(5)
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = bs(html, 'html.parser')
            
    time.sleep(5)

    browser.click_link_by_partial_text('FULL IMAGE')
    featured_image_url =  'https://www.jpl.nasa.gov' + soup.find(class_="button fancybox")['data-fancybox-href']
    #featured_image_url =  soup.find(class_="fancybox-image")
    #print(featured_image_url)

    # *************************************************************
    # Mars Facts
    facts_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(facts_url)
    html = browser.html
    soup = bs(html, 'html.parser')
            
    time.sleep(5)

    mars_weather=soup.find(class_="js-tweet-text-container")\
                        .find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")\
                        .text
    #print(mars_weather)

    # *************************************************************
    # Mars Facts
    mars_facts_url="https://space-facts.com/mars/"
    tables = pd.read_html(mars_facts_url)
    df = tables[0]
    df.columns = ['Description', 'Value']
    #df.set_index('Description', inplace=True)
    html_table = df.to_html()
    #print(html_table)

    # Mars Hemisphere
    mars_hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hem_url)
    time.sleep(5)
    html = browser.html
    soup = bs(html, "html.parser")

    hemisphere_image_urls=[]

    all_items = soup.find_all(class_='item')

    for item in all_items:
        details ={}
        url = item.find('img')['src']
        title = item.find('h3').text
        details['title'] = title
        details['img_url'] = 'https://astrogeology.usgs.gov' + url
        hemisphere_image_urls.append(details)
        
    print(hemisphere_image_urls)

    # Create Final dictionary
    v_mars_data = {
                "news_title" : news_title.text,
                "news_p" : news_p.text,
                "properties" : html_table,
                "featured_image_url" : featured_image_url,
                "mars_weather" : mars_weather,
                "hemisphere_image_urls" : hemisphere_image_urls     
                }

   # print(mars_data)

     # Quite the browser after scraping
    browser.quit()

    return v_mars_data

## Code for testing this program
# print("BEFORE THE SCRAPE CALL !!!!!!")
# x=scrape()
# print(x)
# print("Hi I scraped")
