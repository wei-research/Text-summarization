from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize


import re
### using the hugging face Pegasus pre-trained model for inference

API_URL = "https://api-inference.huggingface.co/models/google/pegasus-xsum"
headers = {"Authorization": "Bearer api_IYoGdhhHfQfojxgYNLQLtUnbcAyTEhWxLy"}


def result(request):
    if(request.method =="POST"):
        input_string = request.POST['input']
        print(input_string)

        #check if user input is website or plain text:
        website = re.match("^http*", input_string)

        #if it's a website:
        if website: 

            webpage= requests.get(input_string).text
            soup = BeautifulSoup(webpage)
            p_tags = soup.find_all('p')
            p_tags_text = [tag.get_text().strip() for tag in p_tags]
            sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
            sentence_list = [sentence for sentence in sentence_list if '.' in sentence]
            article_processed = ' '.join(sentence_list)
            gensim_summary = summarize(article_processed, ratio = 0.1)
            print(f"step 2: {article_processed}")

            response = requests.post(API_URL, headers=headers, json=input_string)
            abstract =response.json()
            print(f"abstract.............. is {abstract}")
            output_summary = abstract[0]

        
            return render(request, "result.html", {"text"  : article_processed, "summary" : output_summary['summary_text'], "gensim_summary" :gensim_summary })
       
        #if input is plain text
        else:     
            #if not empty
            if len(input_string) >0:
                response = requests.post(API_URL, headers=headers, json=input_string)
                abstract =response.json()
                print(f"abstract is...... {abstract}")
                output_summary = abstract[0]

                gensim_summary = summarize(input_string)

                if len(gensim_summary) !=0: 
                    return render(request, "result.html", {"text"  : input_string, "summary" :output_summary['summary_text'], "gensim_summary" :gensim_summary})
                
                else:              
                    return render(request, "result.html", {"text"  : input_string, "summary" :output_summary['summary_text'], "gensim_summary" :"Error: Doesn't meet the mininum input sentences requirement."})


            else:
                return render(request, "result.html", {"text"  : "", "summary": "", "gensim_summary" : ""})
 
    else: 

        return render(request, "result.html", {"text"  : "", "summary": "", "gensim_summary" : ""})


def index(request):
    return render(request, "index.html")

def intro(request):
    return render(request, "intro.html")

def contact(request):
    return render(request, "contact.html")
