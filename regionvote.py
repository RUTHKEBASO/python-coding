#regional votes 
countries=["kenya","uganda","tanzania"]

country=input("enter country").lower()

age=int(input("enter age"))

if country in countries and age>=18:
    print("legible to vote")
else:
    print("ineligible to vote")