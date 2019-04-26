'''
Created on Apr 25, 2019

@author: eli_adm
'''
from numpy import array, cos, sin, pi, matmul
from AngleAndVertex import end_position, alpha_coeff, add
from WordGen import f
from Debugging import random_word

def r(angle:float):
    '''
    numpy Rotation matrix for a given angle
    '''
    ret = array([[cos(angle),-sin(angle)],[sin(angle), cos(angle)]])
    return ret

def R(w:str, alpha:float):
    '''
    rotation matrix for after word has been drawn
    '''
    #print("_{"+str((-1)**(len(w)) * alpha_coeff(w)) + " \\alpha}")
    return r((-1)**len(w) * alpha_coeff(w) * alpha)

def T(w:str):
    return array([[(-1)**len(w),0],[0, 1]])

def ep_for_words(alpha, *w):
    #assert all(type(wk)==str for wk in w), "only takes strings"
    sumw, sumz, sumc = "", [0,0], 0
    for wk in w:
        #get the end point and net angle of the word
        z, c = end_position(wk,alpha)
        sumc += c * (-1)**(len(sumw))
        sumz = add(matmul(T(sumw), matmul(R(sumw, alpha), z)), sumz)
        
        sumw += wk
    return sumz, sumc  
        

print("evens")
for n in range(1,30):
    wrong=0
    for i in range(100):
            
        w1,w2 = (random_word(n) for i in range(2))
        
        testz, tc = ep_for_words(pi/3,w1,w2)
        baselinez,bc = end_position(w1 + w2, pi/3)
        if sum([(testz[i]-baselinez[i])**2 for i in range(2)])**.5 >= 0.01:
            wrong+=1
            print("wrong: "+str(n), testz,baselinez,bc, sep="\t")
    print(wrong)
    print("*"*30,n+1,)