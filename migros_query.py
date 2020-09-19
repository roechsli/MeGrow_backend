import requests
import pandas as pd
from utils.Product import Product


authentication_token = ('hackzurich2020', 'uhSyJ08KexKn4ZFS')
response = requests.get('https://hackzurich-api.migros.ch/hack/logistic/orders?articleID=881620110442', auth=authentication_token)

print(response.json())

print("")

df = pd.DataFrame.from_dict(response.json(), orient='columns')

product = Product(df.iloc[0])


print("Product '{0}' came from '{1}'".format(product.get_name(), product.get_origin()))
