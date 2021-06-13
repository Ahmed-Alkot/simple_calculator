from pprint import pprint
import requests
import os
import urllib.parse

appid = '9HGGEE-4G3YXAKRXG'

quest = input("enter: ")
query = urllib.parse.quote_plus(f"integrate {quest}")
query_url = f"http://api.wolframalpha.com/v2/query?" \
            f"appid={appid}" \
            f"&input={query}" \
            f"&format=image,plaintext" \
            f"&output=json"

r = requests.get(query_url).json()

data = r["queryresult"]["pods"][0]["subpods"][0]
plaintext = data["plaintext"]
image = data['img']['src']
img_name = f"solution to {quest}.jpg"
img_data = requests.get(image).content

with open(img_name, 'wb') as handler:
    handler.write(img_data)
    print(f"Answer Saved to {img_name}.")

print(f"Anti derivative is \n{plaintext}")
