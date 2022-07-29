import requests

FACEBOOK_APP_ID =378892710938489


def requestStories(user_id):
    url = f"https://graph.facebook.com/{user_id}/stories?access_token=1090062614937465"
    return requests.get(url).json()


if __name__ == "__main__":
    print(requestStories("17841405822304914"))
