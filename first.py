oxford={
    "hello": "a set of dictonary",
    "instagram": "a picture sharing page",
    "youtube": "a video sharing page",
    "mylist": [1,2,3,4,5,6,7,8]
}
#print(oxford)
#rint(oxford["instagram"])
#print(oxford.items())
#for a, b in oxford.items():
    #print(a,":+",b)
#for key in oxford.keys():
    #print(key)
oxford.update({"manmay":"is a good programmer", "instagram":"sriti kumari","mylist":[58,6]})
for a,b in oxford.items():
    print(a,b)
oxford.get("not present in the dictionary")