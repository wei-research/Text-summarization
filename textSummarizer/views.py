from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize
import asyncio
import time
import json
import re

from textSummarizer.preprocess import webprocess, query


### using the hugging face Pegasus pre-trained model for inference



def result(request):
    if(request.method =="POST"):
        input_string = request.POST['input']
        print(input_string)

        #check if user input is website or plain text:
        website = re.match("^http*", input_string)

        #if it's a website:
        if website: 
            webpage= requests.get(input_string).text
            articel_processed = webprocess(webpage)

            gensim_summary = summarize(articel_processed, ratio = 0.1)
            # print(f"step 2: {article_processed}")

            # payload_input = {"inputs":"", "options": {"wait_for_model": True}}
            payload_input = {"inputs":""}
            payload_input["inputs"]=articel_processed
            abstract = query(payload_input)

            print(f"abstract.............. is {abstract}")
            print(f"type.............. is {type(abstract)}")

            iter = 0
            while isinstance(abstract, list) == False and iter < 15:  
                abstract = query(payload_input)
                print("................getting cache!!! ")
                iter =+1

            try: 
                output_summary = abstract[0]
            except:
                output_summary = {"summary_text": "Sorry, the server is busy, please go to back to homepage, refresh and try again. "}
            
            return render(request, "result.html", {"text"  : articel_processed,"summary" : output_summary['summary_text'], "gensim_summary" :gensim_summary })
       
        #if input is plain text
        else:     
            #if not empty
            if len(input_string) >0:

                payload_input = {"inputs":""}
                payload_input["inputs"]=input_string
                abstract = query(payload_input)

                print(f"abstract is...... {abstract}")

                iter = 0
                while isinstance(abstract, list) == False and iter < 15:
                    abstract = query(payload_input)
                    print("................Retry and getting cache from API server!!! ")
                    iter +=1
                
                try: 
                     output_summary = abstract[0]
                except:
                     output_summary = {"summary_text": "Sorry, the server is busy, please go to back to homepage, refresh and try again. "}

                gensim_summary = summarize(input_string, ratio =0.1)

                if len(gensim_summary) !=0: 
                    return render(request, "result.html", {"text"  : input_string, "summary" :output_summary['summary_text'], "gensim_summary" :gensim_summary})
                
                else:              
                    return render(request, "result.html", {"text"  : input_string, "summary" :output_summary['summary_text'], "gensim_summary" :"Sorry, no extractive summary generated because input texts doesn't meet the mininum length requirement."})


            else:
                return render(request, "result.html", {"text"  : "", "summary": "", "gensim_summary" : ""})
 
    else: 

        return render(request, "result.html", {"text"  : "", "summary": "", "gensim_summary" : ""})


def model(request):
    return render(request, "index.html")

def intro(request):
    return render(request, "intro.html")

def contact(request):
    return render(request, "contact.html")

def error(request):
    return render(request, "500.html")