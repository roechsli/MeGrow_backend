from flask import Flask
import requests
from requests.auth import HTTPBasicAuth

EATERNITY_KEY = "SwRbyFIaQWtvjhKNl1xugM4UTBVEqpGm"
EATERNITY_AUTH = HTTPBasicAuth(EATERNITY_KEY, "")
EATERNITY_BASE_URL = "https://co2.eaternity.ch"

MIGROS_AUTH = HTTPBasicAuth("hackzurich2020", "uhSyJ08KexKn4ZFS")
MIGROS_BASE_URL = "https://hackzurich-api.migros.ch"

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def home():
    return "<h1>MeGrow API v0.1</h1>"

@app.route('/products/<int:product_id>')
def get_product(product_id):
    murl = f"{MIGROS_BASE_URL}/products/{product_id}"
    r = requests.get(murl, auth=MIGROS_AUTH)
    if r.status_code not in [200, 201, 202]:
        print(f"ERROR: Failed GETting product {product_id} with status {r.status_code}: '{r.text}'")
    else:
        print(f"SUCCESS: GET product {product_id}")
        return r.json()

    url = f"{EATERNITY_BASE_URL}/api/products/{product_id}"
    response = requests.get(url, auth=EATERNITY_AUTH)
    if response.status_code not in [200, 201, 202]:
        return f"ERROR: Failed GETting product {product_id} with status {response.status_code}: '{response.text}'"
    else:
        print(f"SUCCESS: GET product {product_id}")
        return response.json()

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
