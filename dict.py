#initialization of dictionary
print("initialization of dictionary")
d={"name":"kavita",
   "rollno":123,
   "msg":"Hello"}   
print(d)

print("\nShow keys and values of dictionary")
for x in d:
    print(x)   #Show keys in dictionary
    print(d[x])  #show value in dictionary

#add new value in dictionary
print("\nadd new value in dictionary")
d["subject"]="Maths"
print(d)

#show length of dictionary
print("\nshow length of dictionary")
length=len(d)
print(length)

#Empty dictionary
print("\nEmpty dictionary")
a={"a":1,"b":2,"c":3}
print(a)
a.clear()
print(a)

#pop the element from dictionary
print("\npop the element from dictionary")
a={"a":1,"b":2,"c":3}
a.pop("a")
print(a)

#print values of dictionary
print("\nprint values of dictionary")
for x in d.values():
    print(x)

#print items of dictionary
print("\nprint items of dictionary")
for x in d.items():
    print(x)

#get value by key
print("\nget value by key")
x=d.get("name")
print(x)

#delete the dictionary
print("\ndelete the dictionary")
del a
print(a)
