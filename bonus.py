#number of years 
salary=int(input("enter salary"))
year=int(input("enter years of service"))

if(year>10):
    print("net bonus is:",salary*0.01)
elif(year>=6 and year<=10):
    print("net bonus",salary*0.08)
else:
    print("net bonus is",salary*0.05)



    