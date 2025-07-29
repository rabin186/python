import sys
from sayings import hello, goodbye    #Used to import two functions hello and goodbye from sayings.py file

if len(sys.argv) != 2:
    sys.exit()

hello(sys.argv[1])
goodbye(sys.argv[1])
