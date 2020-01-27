c=1
while (c==1):
    print("1. Read")
    print("2.Write")
    print("3. Append")
    print("4. exit")
    a=int(input("Enter a no="))
    b=1
    while (b==1):
        if(a==1):
            p1=open("C:/Users/Kapil/Desktop/demo.txt",'r')
            print(p1.read())
            p1.close()
            b=0
        if(a==2):
            p1=open("C:/Users/Kapil/Desktop/demo.txt",'w')
            p1.write(input("Enter text="))
            p1.close()
            b=0
        if(a==3):
            p1=open("C:/Users/Kapil/Desktop/demo.txt",'a')
            p1.write(input("Enter text="))
            p1.close()
            b=0
        if(a==4):
            c=0
            b=0
