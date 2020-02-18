# Knacci-Utils
This is a semi-maintained and developing library for k-nacci words and word curves in python, first developed for research in 2018-2019.
## Introduction to <img src="/tex/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/>-nacci Words and Curves
The k-nacci word is a string over the alphabet <img src="/tex/f2fa7155e973c035d80aa7aa0b483d0f.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true&sanitize=true" align=middle width=40.18272059999999pt height=24.65753399999998pt/> generated recursively via the rules:

<p align="center"><img src="/tex/86a1c703632dc6fa5ac0815e8d219aba.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true&sanitize=true" align=middle width=178.09934669999998pt height=20.6229144pt/></p>

<p align="center"><img src="/tex/ca99b418bd1b70837cb0187a1dbc8966.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true&sanitize=true" align=middle width=170.06911019999998pt height=22.127716049999997pt/></p>

The word curves are drawn via turtle-graphics (a non-branching Lindenmyer System, if you like) via a drawing rule:

  (1) Initalize: declare the turning angle <img src="/tex/c745b9b57c145ec5577b82542b2df546.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/>, set the inital drawing angle to <img src="/tex/1444c1b272ccbb529a05e07463acf386.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true" align=middle width=17.06819399999999pt height=14.15524440000002pt/>, and place the turtle on <img src="/tex/e660f3b58b414524ec6f827411021073.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true" align=middle width=36.52973609999999pt height=24.65753399999998pt/>. Set the index <img src="/tex/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/> to 1.

  (2) Move the turtle forward one step.

  (3) If the <img src="/tex/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>th character of the word is a '0', turn the turtle's direction by <img src="/tex/9037305912841572c9ac50f054fed4fe.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true" align=middle width=49.83937694999999pt height=27.15900329999998pt/>.

  (4) Increment the index <img src="/tex/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/> by one.

  (5) If <img src="/tex/d68a336214fdd11b1c8b0fa26a9d3b43.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true" align=middle width=48.924151649999985pt height=24.65753399999998pt/>, return to step 2.

To generate the fractal, we take each curve and rotate/scale it so that the endpoint of the curve touches <img src="/tex/1e5ba49ae6981862f61b4d510dcf29af.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true" align=middle width=36.52973609999999pt height=24.65753399999998pt/>. Then we take the limit of the modified curve as <img src="/tex/5b1d0e6cb391219b21d53d5848fe80a9.svg?invert_in_darkmode&sanitize=true&sanitize=true&sanitize=true" align=middle width=51.87587954999999pt height=14.15524440000002pt/>.


## Code Snippets
Usage examples of the files included in this repo:

### WordGen.py

With Knacci Utils, you can obtain all types of <img src="/tex/63bb9849783d01d91403bc9a5fea12a2.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=9.075367949999992pt height=22.831056599999986pt/>-nacci words easily. Get <img src="/tex/8bf47a184625f8d124ae8f140f572f17.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=37.61820479999999pt height=22.831056599999986pt/> via the command `f(k,n)`. For example,

```python
from WordGen import f

for n in range(1,10):
    print(n, f(2,n))
  ```
  
 You can also get <img src="/tex/a0d7950f40d86754b91c430dde7e0094.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=35.50631534999999pt height=20.221802699999984pt/> via the command `t(k,n)`.
 
 ### Debugging.py
 
 It is easy to test hypotheses about the drawing rule with `random_word`, which returns a random binary word of any arbitrary length. There are a few other tools.
 ```python
 from Debugging import random_word
 w = random_word(100)       #makes a random binary word of length 100
 is_alphabet_valid(w)       #checks to see if the alphabet is a subset of {'0','1'}
 ```
 
 ### AngleAndVertex.py
This gives you <img src="/tex/f031da32bd07d67f527ef5841e8436fe.svg?invert_in_darkmode&sanitize=true" align=middle width=33.68543309999999pt height=24.65753399999998pt/>, draws pictures of the word curves, and lets you have a list of vertices in the word curve.
  ```python
  
 from math import pi
 from WordGen import f
 from AngleAndVertex import alpha_coeff, vertices, draw_me, end_position
 
 #gives the coefficient of alpha that the drawer is 
 # pointing after drawing the word, related to net angle.
 alpha_coeff(f(3,5))
 
 #a list of vertices in the word curve given some drawing angle
 vertices(f(2,5), pi/3)
 
 #plt.plot(), plt.show() the vertices in the word curve.
 draw_me(f(2,11), pi/3)    
 
 #gives both the coefficient of alpha after drawing and also the last vertex in the word curve
 end_position(f(2,17), pi/3)      
 ```
 
 ### WordSplit.py
 For discovering word generation patterns. There also exist some word comparison generators, not sure what I was doing with those.
 
 ```python
 from WordGen import f
 from WordSplit import split_to
 
 # outputs all possible word decompositions given the subwords in the dict.
 split_to(f(2,7), {"f(2,6)":f(2,6), "f(2,5)":f(2,5), "f(2,4)":f(2,4), "f(2,3)":f(2,3)}) 
 ```
 
 ### HighLevelEndpoints.py
 Determine the endpoints of a composition of words. This file uses numpy.
 ```python
 from math import pi
 from WordGen import f, t
 from HighLevelEndpoints import wordmat, ep_for_words
 
 # z(w) + wordmat(w).z(v) = z(wv)
 #gives the translation/rotation matrix for 
 # drawing another word curve after drawing a word.
 wordmat(f(2,7), pi/3) 
 #gives the endpoint and drawing angle coefficient after drawing all words given.
 ep_for_words(pi/2, f(2,7),f(2,8),t(2,5)) 
 ```
 
 ## Impact: 
Aided validation of the IFS that makes the 2-nacci word fractal. We used combinatorial tools to observe recurring patterns in word-decompositions.
### Periodicity mod 2 in the 2-nacci words (odd)

<img src="per2nacci_5.png" align=middle/>

<img src="per2nacci_7.png" align=middle/>

<img src="per2nacci_9.png" align=middle/>

 <img src="per2nacci_11.png" align=middle/>
 
 <img src="per2nacci_13.png" align=middle/>
 
 <img src="per2nacci_15.png" align=middle/>

