#required modules
import re
import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen

#re pattern for filtering product title
pattern = r"\)[^\)]*$"

#base urls of both sites
fpt_base_url = "https://www.flipkart.com/search?q="
azn_base_url = "https://www.amazon.in/s?k="

#for server -  identify the client making the request, typically a web browser or a software application. 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}


#function for scraping amazon's product details
def azn_product_df(keyword):
    # lists for storing scraped details 
    products_list = []
    prices_list = []
    images_list = []

    try:
        #trying to open url 
        azn_url = urlopen(azn_base_url+keyword)
    except:
        #returns false if url not opens
        return False
    else:
        #parsing query output html document
        azn_reader = BeautifulSoup(azn_url, 'html.parser')

        #finding tags with relative content
        azn_product_name = azn_reader.findAll('span', {'class':'a-text-normal'})
        azn_product_price = azn_reader.findAll('span', {'class':'a-price-whole'})
        azn_product_image = azn_reader.findAll('img', {'class':'s-image'})

        #itereting each tag for extracting content  using .get_text() and adding these contents into corresponding lists
        for name, price, link in zip(azn_product_name, azn_product_price, azn_product_image):
            if "Redmi 8" or "redmi 8" in name.get_text():
                products_list.append(re.sub(pattern, ")", name.get_text()))
                prices_list.append(int(re.sub('[₹,]', '', price.get_text())))
                images_list.append(link.attrs['src'])

        #converting lists into single dataframe called as azn_products_df
        azn_products_df = pd.DataFrame(data={'Name':products_list,'Price':prices_list, 'links':images_list})

        return azn_products_df
    

#function for scraping flipkart's product details
def fpt_product_df(keyword):
    # lists for storing scraped details  
    products_list = []
    prices_list = []
    images_list = []

    try:
        #trying to open url 
        fpt_url = urlopen(fpt_base_url+keyword)
    except:
        #returns false if url not opens
        return False
    else:
        #parsing query output html document
        fpt_reader = BeautifulSoup(fpt_url, 'html.parser')

        #finding tags with relative content
        fpt_product_name = fpt_reader.findAll("div", {'class':'_4rR01T'})
        fpt_product_price = fpt_reader.findAll('div', {'class':'_30jeq3'})
        fpt_product_image = fpt_reader.findAll('img', {'class':'_396cs4'})

        #itereting each tag for extracting content  using .get_text() and adding these contents into corresponding lists
        for name, price, link in zip(fpt_product_name, fpt_product_price, fpt_product_image):
            if "Redmi 8" in name.get_text():
                products_list.append(re.sub(pattern, ")", name.get_text()))
                prices_list.append(int(re.sub('[₹,]', '', price.get_text())))
                images_list.append(link.attrs['src'])

        #converting lists into single dataframe called as azn_products_df
        fpt_products_df = pd.DataFrame(data={'Name':products_list,'Price':prices_list, 'links':images_list})

        return fpt_products_df
    


    


