import requests

def getImageUrlFrom(query, key):
    endPointURL = f"https://api.giphy.com/v1/gifs/search?api_key={key}&q={query}&limit=25&offset=0&rating=g&lang=en"
    response = requests.get(endPointURL).json()
    imgURL = response["data"][0]["images"]["fixed_height"]["url"]
    return imgURL