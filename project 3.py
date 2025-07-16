#%%
import bs4

pip install requests
#%%
pip install bs4
#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all('article',class_='product_pod')
book_data=[]
for book in books:
    title = book.h3.a['title']
    price = book.find('p', class_='price_color').text
    print(f"Title: {title}\nPrice: {price}\n")
    book_data.append({"Title": title, "Price": price})
f=pd.DataFrame(book_data)
print(f)
#%%
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,6))
sns.barplot(x=book.title, y=book.values)
plt.xticks(rotation=45)
plt.title("Total book values")
plt.xlabel("Titles")
plt.show()
