import sys
import requests
from bs4 import BeautifulSoup

def scrape_extension_version(extn_url):
    page = requests.get(extn_url)
    soup = BeautifulSoup(page.content, "html.parser")
    extn_version = soup.find("span", {"class": "C-b-p-D-Xe h-C-b-p-D-md"}).get_text()
    return extn_version

def trigger_message_to_chat(info_text, extn_version):
    url = '<GoogleChatWebhook>'
    card_data = {
                    "cards": [
                        {
                            "header": {
                                "title": info_text,
                                "subtitle": "VERSION : " + extn_version,
                                "imageUrl": "<ChromeImageUrl>",
                                "imageStyle": "IMAGE"
                            }
                        }
                    ]
                }
    requests.post(url, json = card_data)

extn_url = sys.argv[1]
file_name = "extension_version"
info_text = "Extension Published!!!"

f = open(file_name + ".txt", "r")
version_from_file = f.read()
extn_version = scrape_extension_version(extn_url)

if version_from_file != extn_version:
    f = open(file_name + ".txt", "w")
    f.write(extn_version)
    f.close()
    trigger_message_to_chat(info_text, extn_version)
