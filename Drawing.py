from math import pi, sin, cos, acos
from WordGen import f,t, prefix_generator

def unit_vec(theta:float):
    '''
    Returns a unit vector with angle theta
    try: 
    --------------------------------
    unit_vec(pi/3)
    --------------------------------
    '''
    return [cos(theta),sin(theta)]

def absvec(a:list):
    '''
    returns size of vector/list a in euclidean space
    Try:
    -----------------------------------------------------
    absvec([cos(1.8),sin(1.8)])
    -----------------------------------------------------
    from WordGen import f
    absvec(end_position(f(2,10)))
    -----------------------------------------------------
    '''
    return sum([v**2 for v in a])**.5

def get_uvec(vec):
    '''
    returns unit vector with same angle as vec
    try:
    [5*cos(pi/6), 5*sin(pi/6)]
    '''
    l = absvec(vec)
    return [v/l for v in vec]

def add(a,b):
    '''
    adds two lists elementwise
    try:
    add([0,1,0],[1,0,1])
    sure this exists in numpy, it was just giving me hella weird errors
    '''
    assert len(a)==len(b)
    return [a[i]+b[i] for i in range(len(b))]
        
def alpha_coeff(w):
    '''
    returns the coefficient of alpha (the turning angle) after drawing said word on the plane.
    Multiplying by alpha and adding pi/2 after gives you the final resulting drawing angle.
    not including pi/2
    try:
    for i in range(1,10):
        print(i,'0'*i, alpha_coeff('0'*i))
        
    for n in range(1,10):
        print(n, alpha_coeff(f(2,n)))
    
    '''
    # coeff = 0
    # for k,w_k in enumerate(w):
    #     if w_k == "0":
    #         coeff+= (-1)**(k+1)
    # return coeff        
    return sum((-1)**(k+1) if w_k=='0' else 0 for k,w_k in enumerate(w))
            


def V(w:str, alpha, a0=pi/2):
    '''
    returns the end position of a binary word on the plane as [x,y]
    (slows down at around f(2,10))
    try: 
    ---------------------
    V('0')
    ---------------------
    V('1')
    ---------------------
    V('010')
    ---------------------
    V(f(2,15))
    ---------------------
    '''
    ep = [0,0]
    for w_prime in prefix_generator(w):
        ep = [ep[0]+cos(alpha*alpha_coeff(w_prime)+a0),
              ep[1]+sin(alpha*alpha_coeff(w_prime)+a0)]
    return ep

def vertices(w:str, alpha:float, a0:float=pi/2):
    '''
    speedy! returns the vertices of a k-nacci curve on the plane as two lists, x and y.
    w is the binary word, 
    a is $\alpha$ the drawing angle, and 
    a0 is the inital drawing angle
    
    try:
    --------------------------------------------------------
    import matplotlib.pyplot as plt
    from WordGen import f
    
    plt.plot(vertices(f(2,15)))
    plt.show()
    --------------------------------------------------------
    
    Note:
    This totally lets you pass in words from any alphabet you like. Nonzeroes get treated like 1's.
    '''
    
    coeff = 0                       #coefficient of alpha
    x,y = [0],[0]                   #vertex lists
    pos = unit_vec(a0)              #current position (is going to be $\overline{u}_{\alpha_0}$ at start)
    
    for k,w_k in enumerate(w):
        
        #store the current position in the vertex lists
        x.append(pos[0])
        y.append(pos[1])
        
        #determines the step angle
        #equivalent to $\psi(w_k)$
        if w_k == "0":
            coeff+= (-1)**(k+1) + 0
            
        #add the step to the current position
        #we start having taken the first step 
        #(drawing angle is changed *after* step is taken, so say the papers.)
        if k!=len(w)-1:    
            pos = add(pos, unit_vec(coeff * alpha + a0))
            
    return x,y

def end_position(w, alpha, a0=pi/2):
    '''
    Returns the end position of a k-nacci word curve on the plane as [x,y] and also the coefficient of alpha in the net angle.
    w is the binary word, 
    a is $\alpha$ the drawing angle, and 
    a0 is the inital drawing angle
    Try:
    --------------------------------------------------------------------
    print(f(2,5), end_position(f(2,5)))
    --------------------------------------------------------------------
    for n in range(1,15):
        print('n=',n,"endpoint and coeff:",end_position(f(2,n), pi/3))
    --------------------------------------------------------------------   
    Note:
    This totally lets you pass in words from any alphabet you like. Nonzeroes get treated like 1's.
    '''
    coeff = 0
    pos = [0,1]
    
    for k,w_k in enumerate(w):
        
        if w_k == "0":
            coeff+= (-1)**(k+1) + 0
        
        if k!=len(w)-1:    
            pos = add(pos, unit_vec(coeff * alpha + a0))
            
    return pos, coeff
    
def f2n_analysis(max_n=18):
    '''
    just a little exploring tool
    '''
    absprev1, absprev2 = 1,1
    for n in range(1,18,1):
        f2n = f(2,n)
        pos,coeff = end_position(f2n, pi/3)
        print("n={},\tfirstfew={:5s},  <x,y> = <{:=0.2f}, {:=0.2f}>,\tvecang={:0.3f} pi,\tendcoeff={} alpha,\tL_n={:0.3f},\tB={:0.7f},\tB'={:0.7f}".format(n,f2n[0:5],pos[0],pos[1], acos(get_angle(pos)[1])/pi, coeff, absvec(pos), absvec(pos)/absprev2, absvec(pos)/absprev1))
        absprev2 = absprev1
        absprev1 = absvec(pos)
