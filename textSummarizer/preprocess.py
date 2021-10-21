
from bs4 import BeautifulSoup
import requests
import json

def webprocess(web):

    soup = BeautifulSoup(web, features="html.parser")
    p_tags = soup.find_all('p')
    p_tags_text = [tag.get_text().strip() for tag in p_tags]
    sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
    sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
    processed_text= ' '.join(sentence_list)

    return processed_text


def query(payload):
    API_URL = "https://api-inference.huggingface.co/models/google/pegasus-xsum"
    headers = {"Authorization": "Bearer api_IYoGdhhHfQfojxgYNLQLtUnbcAyTEhWxLy"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()