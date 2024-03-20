""" Functions that are use to Navigating Html Content """
import csv

"""Function to extract Product Name""" 
def get_title(product):
  try:
    title_string = product.find("div", attrs={"class":'_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y'}).text.strip()
  except AttributeError:
    title_string = ""
  return title_string

"""Function to extract Product Price"""
def get_price(soup):
  try:
    price = soup.find("span", attrs={'class':'p13n-sc-price'}).string.strip()
  except AttributeError:
    price = ""
  return price

"""Function to extract Product Rating"""
def get_rating(product):
  try:
    rating = product.find("span", attrs={'class':'a-icon-alt'}).string.split(' ')[0]
  except AttributeError:
    rating = ""	
  return rating

""" Function to extract Number of User Reviews """
def get_review_count(product):
    try:
        review_count = product.find("div", attrs={'class':"a-icon-row"}).find("span", attrs={'class':'a-size-small'}).string.strip()
    except AttributeError:
        review_count = ""	
    return review_count

""" Function to extract the author name of product  """
def get_author_name(product):
  try:
    author = product.find("span", attrs= {'class': "a-size-small a-color-base"}).find("div", attrs={'class':"_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y"}).string.strip()
    
  except AttributeError:
    author = ""
  return author 


""" Function to extract the image Url of product  """
def get_img_url(product):
  try:
    img_url = product.find("img").get('src')
  except:
    img_url = ''
  return img_url


""" Function to Convert String to Integer Numbers"""
def string_to_integer(s):
  if s is None:
    return None
    
  # Remove commas if present and convert to integer
  s_without_commas = s.replace(',', '')
  try:
    return int(s_without_commas)
  except ValueError:
    # Handle cases where the string contains non-numeric characters
    return None


"""Function to check if a book name already exists in the CSV file"""
def is_book_name_unique(book_name):
  try:
    with open('audible_best_sellers.csv', mode='r', encoding='utf-8') as file:
      reader = csv.reader(file)
      for row in reader:
        if row[0] == book_name:
          return False
  except FileNotFoundError:
    return True  # File does not exist, so the book name is unique
  return True