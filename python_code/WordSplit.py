'''
Created on Apr 3, 2019

COMPARING AND DECOMPOSING WORDS

@author: eli_adm
'''
from WordGen import f,t,h
from queue import Queue

def c_gen(*words):
    '''
    generator that yields tuples of chars at each index for every word passed in,
     or a '' at that position if no char. 
     
    try:
    for x in c_gen('12','123','12345'):       
        print(x)
        
    then look at the columns
    '''
    #for each integer index from the largest word possible
    for i in range(max(len(w) for w in words)):
        #return a tuple of either the char at that index or a '' if non existent
        yield tuple(words[w][i] if i<len(words[w]) else '' for w in range(len(words)))
        
def lev_dist_all(a:float, w1:str, *words:str):
    '''
    returns the Levenshtein distance for words. 
    a is the base of the number used for the metric
    w1 is the main word to measure against
    if all of the words following w1 have different characters, add a**
    
    try:
    lev_dist_all(0.5, 'main word', '_ain word', 'm_in wor_')
    '''
    #initial distance = 0
    dist = 0
    
    #for each char tuple over all words
    for idx,chars in enumerate(c_gen(w1,*words)):
        #if any one of the chars doesn't equal the one in w1
        if not all(chars[0] == c for c in chars):
            #add the power of a
            dist+= a**idx
            
    return dist

def lev_dist_any(a:float, w1:str, *words:str):
    '''
    returns the Levenshtein distance for words. 
    a is the base of the number used for the metric
    w1 is the main word to measure against
    if any of the words following w1 have different characters, add a**
    
    try:
    lev_dist_any(0.5, 'main word', '_ain word', '__in wor_')
    '''
    #initial distance = 0
    dist = 0
    
    #for each char tuple over all words
    for idx,chars in enumerate(c_gen(w1,*words)):
        #if any one of the chars doesn't equal the one in w1
        if not any(chars[0] == c for c in chars[1:]):
            #add the power of a
            dist+= a**idx
            
    return dist

def lev_dist(a:float, mainword:str, *words:str):
    '''
    returns the Levenshtein distance for words in a tuple. 
    a is the base of the number used for the metric
    mainword is the main word to measure against
    
    try:
    print(lev_dist(1, '123456789','_23456789','12345678_',''))
    print(lev_dist(1.0/2, 'hello?','Hello?','Hello','UWU'))
    should count the number of chars not matching '123456789'
    
    potential issue:
    requires iterating over mainword over and over.
    '''
    return tuple(lev_dist_all(a,mainword,wk) for wk in words)

def split_to(origwd:str, subwds:dict):
    '''
    splits original word origwd into the subwords found and named in the dict
    returns a list of origwd represented by the keys of the dict
    try:
    print('01010',{'A':'01','B':'1','C':'0'})
    print(split_to('01010',{'A':'01','B':'1','C':'0'}))
    
    '''
    finished = []
    
    def search_item(leftovers:str, kwrep:str):
        return {'leftovers':leftovers, 'kwrep':kwrep}
    
    def try_to_split(word:str, prevkwrep):
        for k,w in subwds.items():
            try:
                
                if word[:len(w)]==w: #fine
                    leftover = word[len(w):]
                    kwrep = prevkwrep + k
                    if leftover=='':
                        finished.append(kwrep)
                    else:
                        yield search_item(leftover, kwrep)
            finally:
                1+1 
    
    #make the queue and add the first word
    q = Queue(maxsize=0)
    q.put(search_item(origwd, ""))
    
    while q.qsize()!=0:
        new_task = q.get()
        for si in try_to_split(new_task['leftovers'], new_task['kwrep']):
            print('LOC:',len(si['leftovers']),'\t kwrep',si['kwrep'])
            q.put(si)
        
    return finished

'''
'f(n-2p) ':f(k,n-2*p),
't(n-2p) ':t(k,n-2*p),
'''
k = 3
n = 7
p = 2
results = split_to(f(k,n),
    {
     'f(n-p) ':f(k,n-p),
     't(n-p) ':t(k,n-p),
     '<f(n-p)-f(n-p-2)> ':,
     'h(n-p)':h(k,n-p)
     }
    )
print("\n"*10)
for decomp in results:
    print(decomp)