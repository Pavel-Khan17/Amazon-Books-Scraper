from bs4 import BeautifulSoup
import requests, csv, time
from Nav_Functions import *

# user agent 
HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0', 'Accept-Language': 'en-US, en;q=0.5'})

def scrape_product_details(category_url):
  """ Single product scriping function """
  
  # HTTP Request
  response = requests.get('https://www.amazon.com/'+ str(category_url), headers=HEADERS)
  print(response.status_code)
  
  if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'lxml')
    
    # Fetch links as List of Tag Objects
    products = soup.find_all("div", attrs={'class':'p13n-sc-uncoverable-faceout'}, limit=5)
    
    
    # # Loop for extracting product details from each link 
    for product in products:
      """Function calls to display all necessary product information"""
      book_name = get_title(product)
      author = get_author_name(product)
      img_url = get_img_url(product)
      price = get_price(product)
      rating = get_rating(product)
      num_ratings = string_to_integer(get_review_count(product))
      
      
      if is_book_name_unique(book_name):
        # Storing the product information into the csv file 
        with open('audible_best_sellers.csv', mode='a', encoding='utf-8', newline='') as file:
          writer = csv.writer(file)
          writer.writerow([book_name, author, rating, num_ratings, price, img_url])
      
    print(f"Scraped: {category_url}")
    
  else:
    time.sleep(5)
    scrape_product_details(category_url) 


def scrape_audible_best_sellers(base_url):
  """ Main scraping function """
  
  # HTTP Request
  response = requests.get(base_url, headers=HEADERS)
  
  print(response.status_code)
  
  if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, "lxml")
    
    categories = soup.find_all('div', attrs={'class': "_p13n-zg-nav-tree-all_style_zg-browse-item__1rdKf _p13n-zg-nav-tree-all_style_zg-browse-height-large__1z5B8"})
    category_urls = [cat.a.get('href') for cat in categories if cat.a is not None]
    
    for category_url in category_urls:
      scrape_product_details(category_url)

  else:
    print(f"Failed to scrape base URL: {base_url}")
    time.sleep(5)
    scrape_audible_best_sellers(base_url)



if __name__ == '__main__':
  # The webpage URL
  URL = "https://www.amazon.com/Best-Sellers-Audible-Books-Originals/zgbs/audible/ref=zg_bs_unv_audible_1_18571910011_1"
  
  scrape_audible_best_sellers(URL)
  
  print(f"Scraping Complete")

