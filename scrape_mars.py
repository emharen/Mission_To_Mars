{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 113,
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup as bs\n",
    "from splinter import Browser\n",
    "from selenium import webdriver\n",
    "import os\n",
    "import pandas as pd\n",
    "import time"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Connect to chromedriver \n",
    "executable_path = {'executable_path': 'C:/Users/emhar/Desktop/chromedriver'}\n",
    "browser = Browser('chrome', **executable_path, headless=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Connect to Mars news website \n",
    "url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'\n",
    "browser.visit(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {},
   "outputs": [],
   "source": [
    "# HTML Object\n",
    "html = browser.html\n",
    "\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup = bs(html, 'html.parser')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "InSight Captures Sunrise and Sunset on Mars\n",
      "InSight joins the rest of NASA's Red Planet surface missions, all of which have photographed either the start or end of a Martian day.\n"
     ]
    }
   ],
   "source": [
    "# Collect the latest News Title and Paragraph Text.\n",
    "news_title = soup.find('div', class_='content_title').find('a').text\n",
    "news_p = soup.find('div', class_='article_teaser_body').text\n",
    "\n",
    "# Display scrapped data \n",
    "print(news_title)\n",
    "print(news_p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Connect to Mars images website \n",
    "url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "browser.visit(url2)\n",
    "\n",
    "browser.click_link_by_partial_text('FULL IMAGE')\n",
    "time.sleep(2)\n",
    "browser.click_link_by_partial_text('more info')\n",
    "time.sleep(2)\n",
    "browser.click_link_by_partial_text('.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "https://photojournal.jpl.nasa.gov/jpeg/PIA19685.jpg\n"
     ]
    }
   ],
   "source": [
    "# HTML Object\n",
    "html2 = browser.html\n",
    "\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup2 = bs(html2, 'html.parser')\n",
    "\n",
    "featured_img_url = soup2.find('img').get('src')\n",
    "print(featured_img_url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Connect to Mars report twitter\n",
    "weather_url='https://twitter.com/marswxreport?lang=en'\n",
    "browser.visit(weather_url)\n",
    "# HTML Object\n",
    "html3 = browser.html\n",
    "\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup3 = bs(html3, 'html.parser')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "InSight sol 151 (2019-04-30) low -97.1ºC (-142.8ºF) high -17.5ºC (0.4ºF)\n",
      "winds from the W at 4.1 m/s (9.2 mph) gusting to 12.3 m/s (27.5 mph)\n",
      "pressure at 7.40 hPapic.twitter.com/SQsvKRWwHz\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# Find the most recent weather tweet\n",
    "mars_weather=soup3.find('div', class_='js-tweet-text-container').text\n",
    "print(mars_weather)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Scrape table using pandas\n",
    "facts_url='https://space-facts.com/mars/'\n",
    "tables = pd.read_html(facts_url)\n",
    "facts_df1=tables[0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Equatorial Diameter:</th>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Polar Diameter:</th>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Mass:</th>\n",
       "      <td>6.42 x 10^23 kg (10.7% Earth)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Moons:</th>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Distance:</th>\n",
       "      <td>227,943,824 km (1.52 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Orbit Period:</th>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Surface Temperature:</th>\n",
       "      <td>-153 to 20 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>First Record:</th>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Recorded By:</th>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                  1\n",
       "0                                                  \n",
       "Equatorial Diameter:                       6,792 km\n",
       "Polar Diameter:                            6,752 km\n",
       "Mass:                 6.42 x 10^23 kg (10.7% Earth)\n",
       "Moons:                          2 (Phobos & Deimos)\n",
       "Orbit Distance:            227,943,824 km (1.52 AU)\n",
       "Orbit Period:                  687 days (1.9 years)\n",
       "Surface Temperature:                  -153 to 20 °C\n",
       "First Record:                     2nd millennium BC\n",
       "Recorded By:                   Egyptian astronomers"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Reset index\n",
    "df = facts_df1.set_index(0)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'<table border=\"1\" class=\"dataframe\">  <thead>    <tr style=\"text-align: right;\">      <th></th>      <th>1</th>    </tr>    <tr>      <th>0</th>      <th></th>    </tr>  </thead>  <tbody>    <tr>      <th>Equatorial Diameter:</th>      <td>6,792 km</td>    </tr>    <tr>      <th>Polar Diameter:</th>      <td>6,752 km</td>    </tr>    <tr>      <th>Mass:</th>      <td>6.42 x 10^23 kg (10.7% Earth)</td>    </tr>    <tr>      <th>Moons:</th>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <th>Orbit Distance:</th>      <td>227,943,824 km (1.52 AU)</td>    </tr>    <tr>      <th>Orbit Period:</th>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <th>Surface Temperature:</th>      <td>-153 to 20 °C</td>    </tr>    <tr>      <th>First Record:</th>      <td>2nd millennium BC</td>    </tr>    <tr>      <th>Recorded By:</th>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>'"
      ]
     },
     "execution_count": 131,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Dataframe to html\n",
    "facts_html= df.to_html()\n",
    "better_facts=facts_html.replace('\\n', '')\n",
    "better_facts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 324,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Save as html file\n",
    "df.to_html('table.html')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 325,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Connect to hemisphere images\n",
    "hem_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'\n",
    "\n",
    "browser.visit(hem_url)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 326,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create Lists\n",
    "hemisphere_image_urls=[]\n",
    "title_list=[]\n",
    "link_list=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 327,
   "metadata": {},
   "outputs": [],
   "source": [
    "# HTML Object\n",
    "html4 = browser.html\n",
    "\n",
    "# Parse HTML with Beautiful Soup\n",
    "soup4 = bs(html4, 'html.parser')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 328,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the titles\n",
    "titles=soup4.find_all('div', class_='description')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 329,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Find the titles\n",
    "for title in titles:\n",
    "    title_name = title.find('h3').text\n",
    "    title_list.append(title_name)\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 330,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Cerberus Hemisphere Enhanced',\n",
       " 'Schiaparelli Hemisphere Enhanced',\n",
       " 'Syrtis Major Hemisphere Enhanced',\n",
       " 'Valles Marineris Hemisphere Enhanced']"
      ]
     },
     "execution_count": 330,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "title_list "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 331,
   "metadata": {},
   "outputs": [],
   "source": [
    "for one in title_list:\n",
    "    browser.visit(hem_url)\n",
    "    time.sleep(2)\n",
    "    browser.click_link_by_partial_text(one)\n",
    "    \n",
    "    html5 = browser.html\n",
    "\n",
    "    # Parse HTML with Beautiful Soup\n",
    "    soup5 = bs(html5, 'html.parser')\n",
    "    \n",
    "    time.sleep(2)\n",
    "    \n",
    "    link=soup5.find('div', class_='downloads')\n",
    "    time.sleep(2)\n",
    "    link1 = link.a['href']\n",
    "    link_list.append(link1)\n",
    "   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 334,
   "metadata": {},
   "outputs": [],
   "source": [
    "hemisphere_image_urls.append({\"title\" : title_list[0], \"img_url\" : link_list[0]})\n",
    "hemisphere_image_urls.append({\"title\" : title_list[1], \"img_url\" : link_list[1]})\n",
    "hemisphere_image_urls.append({\"title\" : title_list[2], \"img_url\" : link_list[2]})\n",
    "hemisphere_image_urls.append({\"title\" : title_list[3], \"img_url\" : link_list[3]})\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 335,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'title': 'Cerberus Hemisphere Enhanced',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},\n",
       " {'title': 'Schiaparelli Hemisphere Enhanced',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},\n",
       " {'title': 'Syrtis Major Hemisphere Enhanced',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},\n",
       " {'title': 'Valles Marineris Hemisphere Enhanced',\n",
       "  'img_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]"
      ]
     },
     "execution_count": 335,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "hemisphere_image_urls"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
