import json
from pprint import pprint
counter=0
dict= {}
list= []
name= input("enter your name:")
with open("z.json","r")as f:
    z=json.loads(f.read())
    for i in z :
        print(i)
        r = input("enter your answer :")
        list.append(r)
        if r ==z[i]:
            print("True")
            counter+=1
        else:
            print("False")
        
    dict ={name:list}
    print(dict)
    print(" Your Final Result From 20 Degree is :",counter)
    
