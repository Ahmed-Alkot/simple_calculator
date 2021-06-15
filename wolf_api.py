#quick WolframAlpha engine computations
import requests
import urllib.parse
from decouple import config
from main import inpt
# storing appid which acts like a key
# taking the input from the user and parsing it
appid = '9HGGEE-4G3YXAKRXG'

quest = inpt
query = urllib.parse.quote_plus(f"derivate {quest}")
query_url = f"http://api.wolframalpha.com/v2/query?" \
            f"appid={appid}" \
            f"&input={query}" \
            f"&format=image,plaintext" \
            f"&output=json"

# making the request
r = requests.get(query_url).json()

#fetching the data, images and storing them
data = r["queryresult"]["pods"][0]["subpods"][0]
plaintext = data["plaintext"]
image = data['img']['src']
img_name = f"solution to {quest}.jpg"
img_data = requests.get(image).content

# writing the image data in a .jpg file
with open(img_name, 'wb') as handler:
    handler.write(img_data)
    print(f"Answer Saved to {img_name}.")

print(f"Anti derivative is \n{plaintext}")
