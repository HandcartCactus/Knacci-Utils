'''
Created on Apr 3, 2019

ROUTINES FOR DEBUGGING

@author: eli_adm
'''
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

def k_nacci_size(k:int, n:int):
    '''
    Gives proper length of f(k,n)
    '''
    if n==1:
        return 1
    if n==2:
        if k <= 2:
            return 2
        else:
            return k
    else:
        return k_nacci_size(k,n-1)*(k) + k_nacci_size(k,n-2)
