'''
Created on Apr 3, 2019
ROUTINES FOR DEBUGGING
@author: eli_adm
'''
from random import choice

def get_alphabet_str(word:str):
    '''
    returns the minimal alphabet used to make a word (sorted, as a string)
    try '' or '0110100010010010001001' or 'the quick brown foxes jumped over the lazy dog'
    '''
    return "".join(sorted(set(word)))

def get_alphabet_set(word:str):
    '''
    returns the minimal alphabet used to make a word (as a set, order will be randomized)
    try '' or '0110100010010010001001' or 'the quick brown foxes jumped over the lazy dog'
    '''
    return set(word)

def is_alphabet_valid(word:str):
    return get_alphabet_set(word).issubset({"0","1"})

def random_word(n:int):
    return "".join(choice(["0","1"]) for _ in range(n))
