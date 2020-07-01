#!/usr/bin/env python3
import base64

getText = open('secretbaselocation.txt','r')
ourString = getText.read()
ourString = str(ourString)
getText.close()

for i in range(5):
    newText = base64.b64decode(ourString)
    ourString = newText

flag = newText.decode('utf-8')

printFlag = open('flag.txt','a')
printFlag.write(flag)
printFlag.close()