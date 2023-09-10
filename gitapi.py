import requests
# from helpers.Helper import *

api_url = "https://api.github.com/users/shayda-banihashemi"

shayda = requests.get(api_url)
print(shayda.text)

shayda_json = shayda.json()
# print(Helper.prettify(shayda_json))

