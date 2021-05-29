import requests
from bs4 import BeautifulSoup as bs

def get_profile_image(username) -> str:
    url = f"https://github.com/{username}/"
    res = requests.get(url)
    soup = bs(res.content, 'html.parser')
    profile_image = soup.select('img.avatar.avatar-user')[0]['src']
    return profile_image


if __name__ == "__main__":
    github_username = input("Enter Github Username : ")
    print(get_profile_image(github_username))