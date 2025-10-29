# execute.py
import sys
from hello import hello, goodbye
# uncomment the above line of code

if len(sys.argv) == 2:
    hello(sys.argv[1])