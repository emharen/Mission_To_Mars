
#%%
from bs4 import BeautifulSoup as bs
from splinter import Browser
from selenium import webdriver
import os
import pandas as pd
import time

def scrape():

    # A webscraping function for the latest news on mars

    # Python dictionary of the results

    scrape_rsult = {}


    # Connect to chromedriver 
    executable_path = {'executable_path': 'C:/Users/emhar/Desktop/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # Connect to Mars news website 
    url = 'https://mars.nasa.gov/news/? page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    browser.visit(url)


    # HTML Object
    html = browser.html

    # Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')


    # Collect the latest News Title and Paragraph Text.
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='article_teaser_body').text

    # Display scrapped data 
    print(news_title)
    print(news_p)


    # Connect to Mars images website 
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)

    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)
    browser.click_link_by_partial_text('more info')
    time.sleep(2)
    browser.click_link_by_partial_text('.jpg')

    # HTML Object
    html2 = browser.html

    # Parse HTML with Beautiful Soup
    soup2 = bs(html2, 'html.parser')

    featured_img_url = soup2.find('img').get('src')
    print(featured_img_url)


    # Connect to Mars report twitter
    weather_url='https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_url)
    # HTML Object
    html3 = browser.html

    # Parse HTML with Beautiful Soup
    soup3 = bs(html3, 'html.parser')


    # Find the most recent weather tweet
    mars_weather=soup3.find('div', class_='js-tweet-text-container').text
    print(mars_weather)


    # Scrape table using pandas
    facts_url='https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    facts_df1=tables[0]


    # Reset index
    df = facts_df1.set_index(0)
    df


    # Dataframe to html
    facts_html= df.to_html()
    better_facts=facts_html.replace('\n', '')
    better_facts


    # Save as html file
    df.to_html('table.html')


    # Connect to hemisphere images
    hem_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(hem_url)


    # Create Lists
    hemisphere_image_urls=[]
    title_list=[]
    link_list=[]


   
    # HTML Object
    html4 = browser.html

    # Parse HTML with Beautiful Soup
    soup4 = bs(html4, 'html.parser')


    # Find the titles
    titles=soup4.find_all('div', class_='description')


    # Find the titles
    for title in titles:
        title_name = title.find('h3').text
        title_list.append(title_name)


    title_list 


    for one in title_list:
        browser.visit(hem_url)
        time.sleep(2)
        browser.click_link_by_partial_text(one)

        html5 = browser.html

        # Parse HTML with Beautiful Soup
        soup5 = bs(html5, 'html.parser')

        time.sleep(2)

        link=soup5.find('div', class_='downloads')
        time.sleep(2)
        link1 = link.a['href']
        link_list.append(link1)



    hemisphere_image_urls.append({"title" : title_list[0], "img_url" : link_list[0]})
    hemisphere_image_urls.append({"title" : title_list[1], "img_url" : link_list[1]})
    hemisphere_image_urls.append({"title" : title_list[2], "img_url" : link_list[2]})
    hemisphere_image_urls.append({"title" : title_list[3], "img_url" : link_list[3]})


    hemisphere_image_urls
    
    mars_data = {
    "News_Title": news_title,

    "Paragraph_Text": news_p,

    "Most_Recent_Mars_Image": featured_img_url,

    "Mars_Weather": mars_weather,

    "Mars_Hemisphere": hemisphere_image_urls

     }



    return mars_data

