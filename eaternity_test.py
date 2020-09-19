#authentication_token = ('', 'SR011ZC1hWbkge6LmrEnUO2l0tz4TM5X')
#response = requests.get('https://co2.eaternity.ch/api/kitchens/my_kitchen', auth=authentication_token)


import requests
from requests.auth import HTTPBasicAuth

YOUR_KEY = "SR011ZC1hWbkge6LmrEnUO2l0tz4TM5X"
AUTH = HTTPBasicAuth(YOUR_KEY, "")
BASE_URL = "https://co2.eaternity.ch"

if YOUR_KEY == "CHANGEME":
    raise RuntimeError("Please change your api key!!")

def create_kitchen(name, kitchen_id, location):
    url = f"{BASE_URL}/api/kitchens/{kitchen_id}"

    body = {
        "kitchen": {
            "name": name,
            "location": location
        }
    }

    response = requests.put(url, json=body, auth=AUTH)
    if response.status_code not in [200, 201, 202]:
        print(f"ERROR: Failed PUTting kitchen {kitchen_id} with status {response.status_code}: '{response.text}'")
    else:
        print(f"SUCCESS: PUT kitchen {kitchen_id}")
        return response.json()


def put_product(product_id):
    url = f"{BASE_URL}/api/products/{product_id}"

    body = {
      "id": "180320201",
      "date": "2020-02-02",
      "gtin": "00123456789023",
      "names": [
        {
          "language": "de",
          "value": "Karottenpuree"
        }
      ],
      "amount": 20,
      "unit": "gram",
      "producer": "hipp",
      "ingredients-declaration": "Karotten, Tomaten",
      "nutrient-values": {
        "energy-kcal": 200,
        "fat-gram": 12.3,
        "saturated-fat-gram": 2.5,
        "carbohydrates-gram": 8.4,
        "sucrose-gram": 3.2,
        "protein-gram": 2.2,
        "sodium-chloride-gram": 0.3
      },
      "origin": "paris, frankreich",
      "transport": "ground",
      "production": "standard",
      "processing": "raw",
      "conservation": "fresh",
      "packaging": "none"
    }
    response = requests.put(url, json=body, auth=AUTH)
    if response.status_code not in [200, 201, 202]:
        print(f"ERROR: Failed PUTting product {product_id} with status {response.status_code}: '{response.text}'")
    else:
        print(f"SUCCESS: PUT product {product_id}")
        return response


def get_product(product_id):
    url = f"{BASE_URL}/api/products/{product_id}"
    print(url)

    response = requests.get(url, auth=AUTH)
    if response.status_code not in [200, 201, 202]:
        print(f"ERROR: Failed GETting product {product_id} with status {response.status_code}: '{response.text}'")
    else:
        print(f"SUCCESS: GET product {product_id}")
        return response.json()


def get_recipe(recipe_id, kitchen_id):
    url = f"{BASE_URL}/api/kitchens/{kitchen_id}/recipes/{recipe_id}"

    body = {
        "recipe": {
            "titles": [
                {
                    "language": "en",
                    "value": "Carrots and onions"
                }
            ],
            "date": "2020-09-19",
            "location": "Schweiz",
            "servings": 1,
            "ingredients": [
                {
                    "id": "my_unique_carrot_id",
                    "names": [{"language": "en", "value": "Carrots"}],
                    "amount": 250,
                    "unit": "gram",
                    "origin": "Germany",
                    "transport": "ground",
                    "production": "standard",
                    "conservation": "fresh"
                },
                {
                    "id": "my_unique_onion_id",
                    "names": [{"language": "en", "value": "Onions"}],
                    "amount": 75,
                    "unit": "gram",
                    "origin": "Poland",
                    "transport": "ground",
                    "production": "standard",
                    "conservation": "dried"
                }
            ]
        }
    }

    response = requests.put(url, json=body, auth=AUTH)
    if response.status_code not in [200, 201, 202]:
        print(f"ERROR: Failed PUTting recipe {recipe_id} with status {response.status_code}: '{response.text}'")
    else:
        print(f"SUCCESS: PUT recipe {recipe_id}")
        return response.json()


if __name__ == '__main__':
    kitchen_id = "my_first_kitchen"
    #create_kitchen("My First Kitchen", kitchen_id, "Switzerland")
    #put_recipe("my_first_recipe", kitchen_id)
    put_product("180320201")
    get_product("180320201")
    get_product("180320201")

    product_response = {
      "names": [
        {
          "language": "de",
          "value": "Karottenpuree"
        }
      ],
      "id": "180320201",
      "co2-value": 478,
      "co2-value-improvement-percentage": -41,
      "co2-value-reduction-value": -140,
      "foodUnit": 0.3,
      "amount": 20,
      "gtin": "00123456789023",
      "unit": "gram",
      "info-text": "No cooking date was provided.",
      "eaternity-award": True,
      "rating": "A",
      "date": "2020-02-02",
      "ingredients-declaration": "Karotten, Tomaten",
      "ingredients": [
        {
          "id": "FoodServiceb7a7f176-690b-11ea-9516-ae471177f174",
          "names": [
            {
              "language": "de",
              "value": "Karotten"
            }
          ],
          "amount": 100,
          "unit": "gram",
          "origin": "",
          "transport": "",
          "gtin": "",
          "rating": "A",
          "bar-chart": 100,
          "co2-value": 32,
          "foodUnit": 0.10978478484848483
        },
        {
          "id": "FoodServiceb7a8081e-690b-11ea-9516-ae471177f174",
          "names": [
            {
              "language": "de",
              "value": "Tomaten"
            }
          ],
          "amount": 6.938894e-22,
          "unit": "gram",
          "origin": "",
          "transport": "",
          "gtin": "",
          "rating": "B",
          "bar-chart": 0,
          "co2-value": 0,
          "foodUnit": 5.48973752311336e-25
        }
      ]
    }


