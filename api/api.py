from flask import Flask
import requests
from requests.auth import HTTPBasicAuth

EAT_KEY = "SwRbyFIaQWtvjhKNl1xugM4UTBVEqpGm"
EAT_AUTH = HTTPBasicAuth(EAT_KEY, "")
EAT_BASE_URL = "https://co2.eaternity.ch"

MIG_AUTH = HTTPBasicAuth("hackzurich2020", "uhSyJ08KexKn4ZFS")
MIG_BASE_URL = "https://hackzurich-api.migros.ch"

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return "<h1>MeGrow API v0.1</h1>"

@app.route('/products/<int:product_id>')
def get_product(product_id):
    murl = f"{MIG_BASE_URL}/products/{product_id}"
    r = requests.get(murl, auth=MIG_AUTH)
    if r.status_code not in [200, 201, 202]:
        print(f"M ERROR: Failed GETting product {product_id} with status {r.status_code}: '{r.text}'")
    else:
       print(f"M SUCCESS: GET product {product_id}")
        #return r.json()

    # extract information
#    mig_json = r.json()
#    prod_id = product_id
#    prod_name = mig_json['name']
#    prod_gtin = mig_json['gtins'][0]

    # if has category code:BeSS_010115, its a frozen product

#    prod_nam  "names": [
#    {
#      "language": "de",
#      "value": "Karottenpuree"
#    }
#  ],
#  "amount": 20,
#  "unit": "gram",
#  "producer": "hipp",
#  "ingredients-declaration": "Karotten, Tomaten",
#  "nutrient-values": #{
#    "energy-kcal": 200,
#    "fat-gram": 12.3,
#    "saturated-fat-gram": 2.5,
#    "carbohydrates-gram": 8.4,
#    "sucrose-gram": 3.2,
#    "protein-gram": 2.2,
#    "sodium-chloride-gram": 0.3
#  },
#  "origin": "paris, frankreich",
#  "transport": "ground",
#  "production": "standard",
#  "processing": "raw",
#  "conservation": "fresh",
#  "packaging": "none"
#}

    url = f"{EAT_BASE_URL}/api/products/{product_id}"
    print(url)
    response = requests.get(url, auth=EAT_AUTH)
    if response.status_code not in [200, 201, 202]:
        print(f"E ERROR: Failed GETting product {product_id} with status {response.status_code}: '{response.text}'")
    else:
        print(f"E SUCCESS: GET product {product_id}")
        #return response.json()

    return r.json() + response.json()
