# from bs4 import BeautifulSoup
# import requests
#
# url = 'https://asaxiy.uz/product/kompyutery-i-orgtehnika/noutbuki/noutbuki-2'
# data = requests.get(url).text
#
# item = []
# soap = BeautifulSoup(data, "html.parser")
# row = soap.find("div", class_="row")
# info = row.find_all("div", class_='col-6')
# for product in info:
#     rasmi = product.find('img', class_='img-fluid')['data-src']
#     name = product.find('span',class_='product__item__info-title').get_text()
#     price = product.find('span', class_='product__item-price').get_text()
#     item.append({
#         "Noutbook-rasmi": rasmi,
#         "Noutbook-nomi": name,
#         "Noutbook-narxi": price
#     })
#
# print(item)













