

# Abstractive Text Summarization 

Deliverable of UTS 32933 Research Project, Spring 2021

Web Application: [Link](https://absumapp.herokuapp.com/)

Supervisor: [Professor. Wei Liu](https://www.uts.edu.au/staff/wei.liu)


## What is it

- Abstractive Text Summarization is a task of generating a short and concise summary that captures the salient ideas of the source text. The generated abstractive summaries involves paraphrasing, which potentially contain new phrases and sentences that may not appear in the source text.
- Extractive summarization creates the summaries from phrases or sentences in the source document(s).

- The Text Summarizer is a tool to address the ever-growing amount of text data available online to both better help discover relevant information and to consume relevant information faster.

## The model
- The abstractive summarization model is pre-trained with Extracted Gap-sentences for Abstractive SUmmarization Sequence-to-sequence models, known as PEGASUS, which uses self-supervised objective Gap Sentences Generation (GSG) to train a transformer encoder-decoder model. The paper can be found on [arXiv](https://arxiv.org/abs/1912.08777). ICML 2020 accepted. Hugging Face's API is used for inference on the web page of pegasus model trained on XSUM dataset.

- For comparision of different summarization approaches, Genism extractive summarization model (TextRank Algorithm) is added to compare the outputs. 

## Demo
To see the working demo, click on the links
- <a href="#" target="_blank">The video on Demo will be updated shortly</a>

## Overview of the Web Application

#### HomePage: (Introduction of the web application and how it works)

![image](https://user-images.githubusercontent.com/71624659/138288463-570ae28b-fdb6-4bc8-bb65-37519c7e2799.png)

#### Text Summarizer page: (Where the model takes user input and start summarization)
![image](https://user-images.githubusercontent.com/71624659/138288722-f0a499f4-7f89-4669-a35f-7c3a4700541f.png)


#### Result Page: (Will display Texts input by user, Abstractive and Extractive summaries)
![image](https://user-images.githubusercontent.com/71624659/138289400-fb5f01e2-7e91-41e2-92bb-a6e88a2917f8.png)
![image](https://user-images.githubusercontent.com/71624659/138288849-47e3de70-63c0-444c-962e-22e48d00f315.png)


## Dependancies

The automatic text summarizer is deployed with Django framework. 

To run and modify the model on your own device, you need to install the following dependancies in your virtual enrivonment: 
* Django == 2.2
* python >3.6
* gensim
* beautifulsoup4

Under the main directory:
run commands: 
```
$ python manage.py runserver
```
<br>
The webpage will start at django server with private address at: http://127.0.0.1:8000/


<br>

## Contact 

If you have any queries, feel free to create an issue or contact me via the email address 14013635@student.uts.edu.au

## Reference
If you use this code or these models, please cite the following paper:
```
@misc{zhang2019pegasus,
    title={PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization},
    author={Jingqing Zhang and Yao Zhao and Mohammad Saleh and Peter J. Liu},
    year={2019},
    eprint={1912.08777},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
