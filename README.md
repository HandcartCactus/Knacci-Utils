# K-nacci-Words-Python
This is a library for k-nacci word curves in python.
The k-nacci word is a string over the alphabet <img src="/tex/f2fa7155e973c035d80aa7aa0b483d0f.svg?invert_in_darkmode&sanitize=true" align=middle width=40.18272059999999pt height=24.65753399999998pt/> generated recursively via the rules:

<p align="center"><img src="/tex/86a1c703632dc6fa5ac0815e8d219aba.svg?invert_in_darkmode&sanitize=true" align=middle width=178.09934669999998pt height=20.6229144pt/></p>

<p align="center"><img src="/tex/ca99b418bd1b70837cb0187a1dbc8966.svg?invert_in_darkmode&sanitize=true" align=middle width=170.06911019999998pt height=22.127716049999997pt/></p>

The words are drawn via turtle-graphics (a non-branching Lindenmyer System, if you like) via a drawing rule:

  (1) Initalize: declare the turning angle $\alpha$, set the inital drawing angle to $\alpha_0$, and place the turtle on $(0,0)$. Set the index $i$ to 1.

  (2) Move the turtle forward one step.

  (3) If the $i$th character of the word is a '0', turn the turtle's direction by $(-1)^{i} \alpha$.

  (4) Increment the index $i$ by one.

  (5) If $i<|w|$, return to step 2.

To generate the fractal, we take each curve and rotate/scale it so that the endpoint of the curve touches $(0,1)$. Then we take the limit of the modified curve as $n \rightarrow \infty$.
