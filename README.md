# K-nacci-Words-Python
This is a library for k-nacci word curves in python.
The k-nacci word is a string over the alphabet <img src="/tex/f2fa7155e973c035d80aa7aa0b483d0f.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=40.18272059999999pt height=24.65753399999998pt/> generated recursively via the rules:

<p align="center"><img src="/tex/86a1c703632dc6fa5ac0815e8d219aba.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=178.09934669999998pt height=20.6229144pt/></p>

<p align="center"><img src="/tex/ca99b418bd1b70837cb0187a1dbc8966.svg?invert_in_darkmode&sanitize=true&sanitize=true" align=middle width=170.06911019999998pt height=22.127716049999997pt/></p>

The words are drawn via turtle-graphics (a non-branching Lindenmyer System, if you like) via a drawing rule:

  (1) Initalize: declare the turning angle <img src="/tex/c745b9b57c145ec5577b82542b2df546.svg?invert_in_darkmode&sanitize=true" align=middle width=10.57650494999999pt height=14.15524440000002pt/>, set the inital drawing angle to <img src="/tex/1444c1b272ccbb529a05e07463acf386.svg?invert_in_darkmode&sanitize=true" align=middle width=17.06819399999999pt height=14.15524440000002pt/>, and place the turtle on <img src="/tex/e660f3b58b414524ec6f827411021073.svg?invert_in_darkmode&sanitize=true" align=middle width=36.52973609999999pt height=24.65753399999998pt/>. Set the index <img src="/tex/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/> to 1.

  (2) Move the turtle forward one step.

  (3) If the <img src="/tex/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/>th character of the word is a '0', turn the turtle's direction by <img src="/tex/9037305912841572c9ac50f054fed4fe.svg?invert_in_darkmode&sanitize=true" align=middle width=49.83937694999999pt height=27.15900329999998pt/>.

  (4) Increment the index <img src="/tex/77a3b857d53fb44e33b53e4c8b68351a.svg?invert_in_darkmode&sanitize=true" align=middle width=5.663225699999989pt height=21.68300969999999pt/> by one.

  (5) If <img src="/tex/d68a336214fdd11b1c8b0fa26a9d3b43.svg?invert_in_darkmode&sanitize=true" align=middle width=48.924151649999985pt height=24.65753399999998pt/>, return to step 2.

To generate the fractal, we take each curve and rotate/scale it so that the endpoint of the curve touches <img src="/tex/1e5ba49ae6981862f61b4d510dcf29af.svg?invert_in_darkmode&sanitize=true" align=middle width=36.52973609999999pt height=24.65753399999998pt/>. Then we take the limit of the modified curve as <img src="/tex/5b1d0e6cb391219b21d53d5848fe80a9.svg?invert_in_darkmode&sanitize=true" align=middle width=51.87587954999999pt height=14.15524440000002pt/>.
