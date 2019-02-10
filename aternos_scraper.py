import requests
from bs4 import BeautifulSoup
import re
URL = "https://brethrenwhom.aternos.me/"

# Returns "Online" if online, "Offline" if otherwise
def get_status():
    # Get cookies from web page
    cookie_response = requests.get(URL)
    cookies = cookie_response.cookies

    # Get actual site from page
    response = requests.get(URL, cookies=cookies)
    html_text = response.text

    # Parses HTML Page to find server status using reg exp.
    soup = BeautifulSoup(html_text, 'html.parser')
    re_filter = re.compile("status-label (offline|online)")
    status = soup.find(class_=re_filter).string

    return status


if __name__ == "__main__":
    print(get_status())
