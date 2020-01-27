#Create list
print("Create list")
a=["kavita","duggu","kaplu"]

#Store the data of list in another list
print("\nStore the data of list in another list")
b=list(a)
print(b)

#Append
print("\nappend")
a.append("pasta")
print(a)

#Pop the data from list
print("\nPop the data from list")
a.pop()

#Copy the data in another list
print("\nCopy the data in another list")
c=a.copy()
print(c)

#Remove the data from the list
print("\nRemove the data from the list")
a.remove("kavita")
print(a)

#Insert the data in list
print("\nInsert the data in list")
a.insert(1,"kavita")
print(a)

#Indexing by value
print("\nIndexing by value")
print(a.index("kavita"))

#Position
print("\nPosition")
a[0]="kapil"
print(a)

#Searching in list
print("Searching")
print("kavita" in a)

#Range
print("\nRange")
num=list(range(10))
print(num)
num1=list(range(5,8))
print(num1)
num2=list(range(5,20,2))
print(num2)
