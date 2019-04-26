'''
Created on Apr 3, 2019
ROUTINES FOR WORD CREATION
@author: eli_adm
'''

def f(k:int,n:int):
    '''
    k-nacci word f(k,n)
    try f(2,8)
    '''
    assert k>0
    assert n>=1
    
    if n==1:
        return "0"
    if n==2:
        if k <= 2:
            return "01"
        else:
            return "0"*(k-1) + "1"
    else:
        return f(k,n-1)*(k) + f(k,n-2)
    
def twiddle(word:str):
    '''
    does the operation that swaps the last two chars
    tested, will work on all lengths
    try '' or '1' or '21' or '123456798'
    '''
    #uses array slicing notation [start:stop:increment]
    # [:-2] all but last two, [:-2-1:-1], the last two in reverse order, stop is exclusive.
    return word[:-2] + word[:-3:-1]
    
def t(k:int,n:int):
    '''
    the word t as defined in class, f with last two chars swapped
    '''
    return twiddle(f(k,n))

def prefix_generator(w:str):
    '''
    returns the first prefixes
    try: 
    prefix_generator("123456")
    '''
    for i in range(len(w)):
        yield w[:-i]