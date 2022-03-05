# marana.main
#!/usr/bin/python3

"""
The main program for marana

"""
from pathlib import Path

def readfile():
    pass

def runfile():
    query = readfile()
    data = readfile()
    result = interpret(query, data)
    return result

if __name__ == '__main__':
    runfile() 
