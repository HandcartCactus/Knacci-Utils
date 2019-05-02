'''
Created on Apr 25, 2019

@author: eli_adm
'''
from numpy import array, cos, sin, pi, matmul
from AngleAndVertex import end_position, alpha_coeff, addvec
from WordGen import f
from Debugging import random_word



def wordmat(w:str, alpha:float):
    '''
    rotation matrix for after word has been drawn
    '''
    return array([[(-1)**len(w) * cos(alpha_coeff(w) * alpha),(-1)**(2*len(w)+1) * sin(alpha_coeff(w) * alpha)],
       [(-1)**len(w) * sin(alpha_coeff(w) * alpha),     cos((-1)**len(w) * alpha_coeff(w) * alpha)]])

def ep_for_words(alpha, *w):
    #assert all(type(wk)==str for wk in w), "only takes strings"
    sumw, sumz, sumc = "", [0,0], 0
    for wk in w:
        #get the end point and net angle of the word
        z, c = end_position(wk,alpha)
        sumc += c * (-1)**(len(sumw))
        sumz = addvec(matmul(wordmat(sumw, alpha), z), sumz)
        
        sumw += wk
    return sumz, sumc  
