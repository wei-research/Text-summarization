

# Abstractive Text Summarization 

Deliverable of UTS 32933 Research Project, Spring 2021

Supervisor: [Dr. Wei Liu](https://www.uts.edu.au/staff/wei.liu)


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

To run the model, you need to install the following dependancies in your virtual enrivonment: 
* Django == 2.2
* python >3.6
* gensim
* beautifulsoup4
* tensorflow==2.2.0
* sentencepiece
* tokenizers
* tfds-nightly
* numpy

## Use Tex Summarizer on Web page

###  Step 1. Start Django

* Navigate to .  PROJECT_PEGASUS/NLPSeq folder
* run commands: 
```
$ python manage.py runserver
```
......

## Run Inference on your own device with pretrained model.

.....

### Download model variables: 
Need to download the model variables and save the variable folder under /model directory

https://drive.google.com/file/d/1ZF2qO6bAnsTF2LSndLMir3e7NrlFL288/view

## Contact 

If you have any queries, feel free to create an issue or contact me via the email address in my profile.

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
