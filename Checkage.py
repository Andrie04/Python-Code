def classify_age(age):
    if age < 10:
        print("Invalid age!")
    elif age <= 12:
        print("Child")
    elif age <= 19:
        print("Teen")
    elif age <= 61:
        print("Adilt")
    else:
        print("Senior")
       
while True:
    age = int(input("Enter age: "))       
    classify_age(age)