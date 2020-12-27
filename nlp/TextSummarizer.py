# Making some essential imports
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
stopwords = list (STOP_WORDS)
punctuation += '\n'
from heapq import nlargest


# Defining a Class for extracting Summary
class Summarizer():
    
    ## constructor for data loading
    ## give either path or corpus itself
    def __init__(self, path = None, corpus = None):
        self.mCorpus = ''
        self.mWordFrequencies = {}
        self.mSentScore = {}
        self.mNumSentences = 0
        
        if path != None:
            file = open(path, "r")
            self.mCorpus = self.mCorpus + file.read()
        elif corpus != None:
            self.mCorpus = corpus
            
        self.mNlp = spacy.load('en_core_web_sm')
        self.mDoc = self.mNlp(self.mCorpus)
    
    
    # Function for Printing Corpus
    def PrintCorpus(self):
        print(self.mCorpus)
    
    
    ## defining a function for Calculating 
    ## word frequiences
    def WordFrequencyCalculator(self):
        for word in self.mDoc:
            wordInLowerCase = word.text.lower()
            
            if (wordInLowerCase not in stopwords) and (wordInLowerCase not in punctuation):
                if wordInLowerCase not in self.mWordFrequencies.keys():
                    self.mWordFrequencies[wordInLowerCase] = 1
                else:
                    self.mWordFrequencies[wordInLowerCase] += 1
    
        return
    
    
    ## Function for normalizing Frequency Values
    def WordFreqNormalizer(self):
        maxFreq = max(self.mWordFrequencies.values())
        
        for word in self.mWordFrequencies.keys():
            self.mWordFrequencies[word] = self.mWordFrequencies[word] / maxFreq
        
        return
    
    # Function For calculating  sentence score
    # based on computed normalized word Frequencies
    def CalSentScore(self):
        sentences = [sent for sent in summarizer.mDoc.sents]
        self.mNumSentences = len(sentences)
        
        for sent in sentences:
            for word in sent:
                wordInLowerCase = word.text.lower()
                
                if wordInLowerCase in self.mWordFrequencies.keys():
                    if sent not in self.mSentScore.keys():
                        self.mSentScore[sent] = self.mWordFrequencies[wordInLowerCase]
                    else:
                        self.mSentScore[sent] += self.mWordFrequencies[wordInLowerCase]
        return
    
    ## Writting the MainFunction for this script now
    def SummarizeMyText(self, fractionToReduce = 0.2):
        self.WordFrequencyCalculator()
        self.WordFreqNormalizer()
        self.CalSentScore()
        
        reducedSentNum = int (self.mNumSentences * fractionToReduce)
        print ('Total number of Sentences = {}'.format(self.mNumSentences))
        print('Num of Sentences Reduced to {}'.format(reducedSentNum))
        print('Summary as follows : \n')
        
        summaryList = nlargest(reducedSentNum, self.mSentScore, key = self.mSentScore.get)
        for sent in summaryList:
            print(sent, end = '')
        
        
    
    
