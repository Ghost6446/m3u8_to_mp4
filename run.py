# 18.09.2023

# Import
from util.m3u8 import download
from util.util import console
import requests

# Variable
url = ""
headers = ""
key = ""


def main():

    r = requests.get(url, headers=headers)

    if r.ok:
        download(url, r.content, headers, key, "test.mp4")
    else:
        console.log("[red]Insert valid headers or url")

if __name__ == "__main__":
    main()