import os
from bs4 import BeautifulSoup as bs


def get_file_names(direcory_name):
    files_list = os.listdir(direcory_name)
    files_names = []
    for file in files_list:
        if "html" in file:
            files_names.append(file)
    return files_names


def scrape_verse(path):
    with open(path, "r", encoding="utf-8") as f:
        raw_html = f.read()

    html = bs(raw_html, "lxml")
    main_with_tags = html.select("main")

    main = ""
    for line in main_with_tags:
        main += line.text

    # title text scraping
    h1_with_tags = html.select("h1")
    h1 = h1_with_tags[0].text

    # time
    time_with_tags = html.select("time")
    time = time_with_tags[0].text

    return (time, h1, main)
