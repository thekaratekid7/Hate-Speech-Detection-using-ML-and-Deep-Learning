# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 13:10:35 2020

@author: Karate Kid
"""

import nltk
from nltk import ngrams
import csv
import numpy 
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import stopwords
import pickle
import simplejson 
import pandas as pd
import string 
import re




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


def ngram(filename,classl):    
    #opening csv file and storing data into variable data   
    raw_data = pd.read_csv(filename)
    tokenized_word = [] 
    data1 = raw_data['tweet']            #only taking data from column tweet
  
    clean_data = []
    for row in (data1[:]): #this is Df_pd for Df_np (text[:])
        #new_text = re.sub(r'^https?:\/\/.*[\r\n]*', '', row, flags=re.MULTILINE)
        #new_text = re.sub('http://','',row)
        new_text = re.sub('<.*?>', '', row)   # remove HTML tags
        new_text = remove_punct(new_text)      # remove punc.
        new_text = re.sub(r'\d+','',new_text)# remove numbers
        new_text = new_text.lower()# lower case, .upper() for upper          
        if new_text != '':
            clean_data.append(new_text)
    
    string2 = ' '.join(map(str, clean_data))
    
    #print(clean_data)
    list_sent=[]
    
    #sentences = sent_tokenize(string2)
   
    #list_sent = [word.replace(".", "") for word in clean_data]
    
    word_tokens = []
    word_tokens_nested = []
    i=1
    output_ngram = []
    for each_sentence in clean_data[:]:
        s = ''
        s = ''.join(map(str,each_sentence))
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9\s]', ' ',  s)
        #tokens = [token for token in s.split(" ") if token != ""]
        tokens = nltk.tokenize.word_tokenize(s)
        #pos_tokens = nltk.pos_tag(tokens)
               
        if classl=='1':
        	filepath = "D:/Sem 8/Seminar and Project/Project Work/Uni grams/Hate unigrams/file_" + str(i) + ".txt"
  		
        elif classl=='2':
            filepath = "D:/Sem 8/Seminar and Project/Project Work/Uni grams/Offensive unigrams/file_" + str(i) + ".txt"
        
        else:
        	filepath = "D:/Sem 8/Seminar and Project/Project Work/Uni grams/Neutral unigrams/file_" + str(i) + ".txt"
        
        f = open(filepath, "w")
        unigram_tokens = list(tokens)
        for ele in unigram_tokens[:]:
            f.write(ele)
            f.write(" \n")
            #simplejson.dump(t, f)
        f.close()
        i+=1 
    
        
    
    
    
        

    
ngram("hate_clean.csv",'1')
ngram("offensive_clean.csv",'2')
ngram("neutral_clean.csv",'0')









