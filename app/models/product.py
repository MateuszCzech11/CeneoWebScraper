from typing_extensions import Self
import requests
from bs4 import BeautifulSoup
from utils import get_item
import os
import pandas as pd

class Product:
    def __init__(self, product_id=0,opinions=[],product_name="",opinions_count=0,pros_count=0,cons_count=0,average_score=0 ):
        self.product_id = product_id
        self.opinions = opinions
        self.product_name = product_name
        self.opinions_count = opinions_count
        self.pros_count= pros_count
        self.cons_count=cons_count
        self.average_score = average_score


        return self

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def to_dict(self):
        pass

    def extract_product():
        url = f"https://www.ceneo.pl/{self.product_id}#tab=reviews"
        all_opinions = []
        while(url):
            response = requests.get(url)
            page = BeautifulSoup(response.text, 'html.parser')
            self.product_name= product_name
            opinions = page.select("div.js_product-review")
            for opinion in opinions:
                single_opinion = {
                    key:get_item(opinion, *value)
                        for key, value in selectors.items()
                }
                single_opinion["opinion_id"] = opinion["data-entry-id"]
                all_opinions.append(single_opinion)
            try:    
                url = "https://www.ceneo.pl"+get_item(page,"a.pagination__next","href")
            except TypeError:
                url = None
            if not os.path.exists("app/opinions"):
                os.makedirs("app/opinons")
            with open(f"app/opinions/{product_id}.json", "w", encoding="UTF-8") as jf:
                json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
        return self

    def save_opinions(self):
        if not os.path.isdir("app/opinions"):
            os.mkdir("app/opinions")
        with open(f"app/opinions/{product_id}.json", "w", encoding="UTF-8") as jf:
            json.dump(all_opinions, jf, indent=4, ensure_ascii=False)