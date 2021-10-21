

# Abstractive Text Summarization 

Deliverable of UTS 32933 Research Project, Spring 2021

Web Application: [Link](https://absumapp.herokuapp.com/)

Supervisor: [Professor. Wei Liu](https://www.uts.edu.au/staff/wei.liu)


## What is it

- Abstractive Text Summarization is a task of generating a short and concise summary that captures the salient ideas of the source text. Different from extractive summarization, the generated summaries potentially contain new phrases and sentences that may not appear in the source text.

- The Automatic Text Summarizer is a tool to address the ever-growing amount of text data available online to both better help discover relevant information and to consume relevant information faster.

## The model
- The abstractive summarization model is pre-trained with Extracted Gap-sentences for Abstractive SUmmarization Sequence-to-sequence models, known as PEGASUS, which uses self-supervised objective Gap Sentences Generation (GSG) to train a transformer encoder-decoder model. The paper can be found on [arXiv](https://arxiv.org/abs/1912.08777). ICML 2020 accepted. Hugging Face's API is used for inference on the web page of pegasus model fine tuned on XSUM dataset.

- For comparision of different summarization approaches, genism summarization model is added to compare the outputs.


## Demo
To see the working demo, click on the links
- <a href="#" target="_blank">The video on Demo will be updated shortly</a>

## Dependancies

The automatic text summarizer is deployed with Django framework. 

To run the model on your own device, you need to install the following dependancies in your virtual enrivonment: 
* Django == 2.2
* python >3.6
* gensim
* beautifulsoup4


## Use Tex Summarizer on Web page

###  Step 1. Start Django

* Navigate to .PROJECT_PEGASUS/NLPSeq folder
* run commands: 
```
$ python manage.py runserver
```
<br>
The webpage will start at django server with private address at: http://127.0.0.1:8000/

#### HomePage: (Where you can enter a url or plain text for summarization)

![image](https://user-images.githubusercontent.com/71624659/135486669-cd4c9943-7c32-4d28-91b7-45d1f114ea48.png)

#### Result Page: (With Texts input by user, and the Abstractive summary with Pegasus)
![image](https://user-images.githubusercontent.com/71624659/135486817-1ee2b1c3-98d0-4e64-98ea-50cffaec0615.png)

#### Result Page: (with Genisum summarization function for comparison)
![image](https://user-images.githubusercontent.com/71624659/135487076-df8a40ab-3103-4042-a077-c2895cae900e.png)

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
