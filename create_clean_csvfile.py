# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 11:45:11 2020

@author: Karate Kid
"""

import nltk
import csv
import numpy 
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import stopwords
import pickle
import simplejson 
import pandas as pd
import string 
import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import Word2Vec
from nltk.util import ngrams


def write_file(filename,word):
    with open(filename,'w') as f:
        for item in word:
            string5 = ''
            string5 = ' '.join(map(str, item))
            #f.write("%s\n" % item)
            f.write(string5+"\n")
    f.close()
    
def write_file_list(filename,word_list):
    f = open(filename,'w')
    simplejson.dump(word_list, f)
    f.close()    

def remove_punct(string): 
  
    # punctuation marks 
    punctuations = '''!()-[]{};:'"\,<>/?@#$%^&*_~'''
  
    # traverse the given string and if any punctuation 
    # marks occur replace it with null 
    for x in string: 
        if x in punctuations: 
            string = string.replace(x, "") 
  
    # Print string without punctuation 
    return string

def remove_stopwords(lis):
    file_sw = open("sw.txt",'r')
    
    stop_words_str = ''
    stop_words_str = file_sw.read()
    
    stop_words = []
    stop_words = list(stop_words_str.split(" "))
    
    filtered_sentence = [] 
    
    for word in lis:
        if word not in stop_words: 
            filtered_sentence.append(word)
            
    #filtered_sentence.append([word for word in sentences if word not in stop_words])
    
    return filtered_sentence


def start_fun(filename):    
    #opening csv file and storing data into variable data   
    raw_data = pd.read_csv(filename)
    tokenized_word = [] 
    data1 = raw_data['tweet']            #only taking data from column tweet
  
    clean_data = []
    for row in (data1[:]): #this is Df_pd for Df_np (text[:])
        #new_text = re.sub(r'^https?:\/\/.*[\r\n]*', '', row, flags=re.MULTILINE)
        #new_text = re.sub('http://','',row)
        new_text = re.sub('<.*?>', '', row)   # remove HTML tags
        new_text = re.sub(r"http\S+", "", new_text)
        new_text = re.sub(r"@\S+", "", new_text)
        new_text = re.sub(r"rt\S+", "", new_text)
        new_text = remove_punct(new_text)      # remove punc.
        new_text = re.sub(r'\d+','',new_text)# remove numbers
        new_text = new_text.lower()# lower case, .upper() for upper          
        if new_text != '':
            clean_data.append(new_text)
    print(clean_data)
     
    new_filename = filename[:-4] + "_clean.csv"
    df = pd.DataFrame(clean_data, columns=["tweet"])
    df.to_csv(new_filename, index=False)
    
    


start_fun("hate.csv")
start_fun("offensive.csv")
start_fun("neutral.csv")