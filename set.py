#Create set
print("Create set")
s={"teena","meena","reena"}
print(s)   # it can print in unorder way

#pop the element from the set
print("\npop the element from the set")
s.pop()   # it can pop the element in unorder way
print(s)

#Add element in the set
print("\nAdd element in the set")
s.add("priya") # it can add the new value in unorder way 
print(s)
s.add("priya")   # distinct(not return same value in set)
print(s)

#Operation
print("\nOperation")
p={"rajesh","manish","reena"}
print(p)
print("Difference")
x=s.difference(p)
print(x)
print("Intersection")
z=s.intersection(p)
print(z)
print("Difference_update")
y=s.difference_update(p)
print(y)



