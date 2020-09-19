from flask import Flask
import requests
from requests.auth import HTTPBasicAuth

EAT_KEY = "SR011ZC1hWbkge6LmrEnUO2l0tz4TM5X"
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
    # MIGROS FETCH
    murl = f"{MIG_BASE_URL}/products/{product_id}"
    r = requests.get(murl, auth=MIG_AUTH)
    if r.status_code not in [200, 201, 202]:
        print(f"MIG ERROR: Failed GETting product {product_id} with status {r.status_code}: '{r.text}'")
    else:
        # success
        #return r.json()

    # EATERNITY FETCH
    url = f"{EAT_BASE_URL}/api/products/{product_id}"
    response = requests.get(url, auth=EAT_AUTH)
    if response.status_code == 400:
        # product not found, add it to eaternityDB
        put_product(r.json())
    elif response.status_code == 601:
        # product not ready yet

    elif response.status_code not in [200, 201, 202]:
        # error
        print(f"EAT ERROR: Failed GETting product {product_id} with status {response.status_code}: '{response.text}'")
    else:
        # success
        eat_json = response.json()
        eat_co2value = eat_json['co2-value']
        eat_rating = eat_json['rating']
        

def put_product(mig_json):
    # extract information
    mig_json = r.json()
    prod_id = mig_json['gtins']['id']
    prod_name = mig_json['name']
    prod_gtin = mig_json['gtins'][0]
    prod_name = mig_json['name']
    prod_amount = mig_json['package']['net_weight']
    prod_unit = mig_json['package']['net_weight_unit']
    prod_origin = mig_json['origins']['producing_country']
    prod_ingred = mig_json['ingredients']

    body = {
      "id": prod_id,
      "gtin": prod_gtin,
      "names": [
        {
          "language": "de",
          "value": prod_name
        }
      ],
      "amount": prod_amount,
      "unit": prod_unit,
      "producer": "hipp",
      "ingredients-declaration": prod_ingred,
      "nutrient-values": {
        "energy-kcal": parse_nutrientval(mig_json['nutrients'], "PIM_NUT_ENERGIE"),
        "fat-gram": parse_nutrientval(mig_json['nutrients'], "PIM_NUT_GES_FETT"),
        "saturated-fat-gram": parse_nutrientval(mig_json['nutrients'], "PIM_NUT_GESFETTS"),
        "carbohydrates-gram": parse_nutrientval(mig_json['nutrients'], "PIM_NUT_GES_KOHL"),
        "sucrose-gram": parse_nutrientval(mig_json['nutrients'], "PIM_NUT_GES_ZUCK")
      },
      "origin": prod_origin
#      "transport": "ground",
#      "production": "standard",
#      "processing": "raw",
#      "conservation": "fresh",
#      "packaging": "none"
    }

    url = f"{EAT_BASE_URL}/api/products/{prod_id}"
    r = requests.put(url, json=body, auth=EAT_AUTH)
    if r.status_code not in [200, 201, 202]:
        # error
        print(f"ERROR: Failed PUTting product {product_id} with status {response.status_code}: '{response.text}'")
    else:
        # success

def parse_nutrientval(json_object, code):
    return [obj for obj in json_object if obj['code']==code][0]['quantity']

