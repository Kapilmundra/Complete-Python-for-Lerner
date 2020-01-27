#Exception Handling
print("\nException Handling")
try:
    num1=int(input("Enter a no="))
    num2=int(input("Enter a no="))
    print(num1/num2)
    print("Done Calculation")
except ZeroDivisionError:
    print("An Error Occourred")
    print("Due to zero Division")

#Multiple Different Except
print("\nMultiple Different Except")
try:
    num3=int(input("Enter a no="))
    num4=int(input("Enter a no="))
    print(num3/num4)
    print(num3+"Kapil")
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError,TypeError):
    print("Type Error Occorred")
finally:
    print("Final statement will always execute")

#raising Exceotion
try:
    num5=int(input("Enter a no="))
    num6=int(input("Enter a no="))
    print(num5/num6)
except:
    raise

print("\nraising Exceotion")
name="123"
raise NameError("Invalid name")
