import text_eval
import public_parsing_ops
import tensorflow as tf
import numpy as np
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize

_SPM_VOCAB = 'ckpt/c4.unigram.newline.10pct.96000.model'
encoder = public_parsing_ops.create_text_encoder("sentencepiece",
                                                 _SPM_VOCAB)
shapes = {
    'cnn_dailymail': (1024, 128),
    'gigaword':(128, 32)
}

if __name__ == '__main__':


#get website from user input

    articel_1 = input("Enter the news website you need to summarize:")

    page = requests.get(articel_1).text

#scrape the website to text: 

    soup = BeautifulSoup(page)

#get the news headline for futher comparison
    headline = soup.find('h1').get_text()
    p_tags = soup.find_all('p')
#apply preprocessing: 
    p_tags_text = [tag.get_text().strip() for tag in p_tags]
    sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
    sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
    article_processed = ' '.join(sentence_list)

    import argparse

    parser = argparse.ArgumentParser()
    # parser.add_argument("--article", help="path of your example article", default="example_article")
    # parser.add_argument("--model_dir", help="path of your model directory", default="model/")
    parser.add_argument("--model_dir", help="path of your model directory", default="model/")   
    parser.add_argument("--model_name", help="path of your model directory", default="gigaword")
    args = parser.parse_args()

    # text = open(args.article, "r", encoding="utf-8").read()

    text = article_processed

    #get extractive summarization with Gensim
    gensim_summary = summarize(article_processed, ratio=0.1)


    shape,_ = shapes[args.model_name]

    input_ids = encoder.encode(text)
    inputs = np.zeros(shape)
    idx = len(input_ids)
    if idx>shape: idx =shape

    inputs[:idx] = input_ids[:idx]
    imported = tf.saved_model.load(args.model_dir, tags='serve')
    example = tf.train.Example()
    example.features.feature["inputs"].int64_list.value.extend(inputs.astype(int))
    output = imported.signatures['serving_default'](examples=tf.constant([example.SerializeToString()]))


    print(f"\nNews Headline is: \n {headline}")
    print("\nAbstractive summary is: \n ", text_eval.ids2str(encoder, output['outputs'].numpy(), None))
    print(f"\nSummary with Gensim model is: \n {gensim_summary}")
