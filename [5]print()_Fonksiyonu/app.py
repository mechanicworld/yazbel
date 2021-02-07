import sys
import os


f = open("test.txt","a")
lis1=[1,2,3,4,5]
print(*"Hello Oguz",sep="*", end="\r",flush=True,file=f)
print(*"Mello Oguz",sep="*", end="\r",flush=True,file=f)

print(*"Kahramanmaraşlılaştıramadıklarımızdanmısınız?",sep=".")