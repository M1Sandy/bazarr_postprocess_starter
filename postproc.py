#!/usr/bin/python3

import subprocess
import sys

argProgram = []

if __name__ == "__main__":
  
    argCount = len(sys.argv)
    for i in range(1, argCount):
        argProgram.append(sys.argv[i])
    subprocess.call(argProgram)
