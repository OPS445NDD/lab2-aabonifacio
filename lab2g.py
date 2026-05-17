#!/usr/bin/env python3
#Author: Allen Aleczandre Bonifacio
#Author ID: aabonifacio
#Date Created: 2026/01/16
import sys

if len(sys.argv) == 1:
    timer = 3
else:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1

print("blast off!")
