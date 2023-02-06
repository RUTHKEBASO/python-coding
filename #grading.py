#grading 
unit1=int(input("enter unit1:"))
unit2=int(input("enter unit2:"))
unit3=int(input("enter unit3:"))
avg=(unit1+unit2+unit3)/3
if(avg >=70  and avg<=100):
    print("A")
elif(avg >=60  and avg<=69):
     print("B")
elif(avg >=50  and avg<=59):
    print("C")
elif(avg >=40  and avg<=49):
     print("D")
else:
    print("fail")


