#Rutgers GPA Calculator via Python
#For those who don't have access to Excel for some reason

print("What year are you currently? \n1. Freshman with no credits \n2.Freshman with credits \n3. Sophomore \n4 Junior \n5. Senior \n6. Super Senior")
year = input('Enter:  ')
year = int(year)
if year == 1:
    print("No credits.")
else:
    print("What is the total amount of credits you have so far")
    upper = input('Enter:  ')
    upper = int(upper)

print('How many credits did you take this semester?')
credits = input('Enter:')
credits = float(credits)

#Class GPA Calculator
print('Enter the amount of credits for each class and the grade')
Class_cred1 = input('Enter the amount of credits for class 1:  ')
Class_cred1 = float(Class_cred1)
grade_1 = input('Enter the grade for class 1 here: ')
if grade_1 == "A":
    print(Class_cred1, "*4.0", "=", Class_cred1 * 4.0)
elif grade_1 == "B+":
    print(Class_cred1, "*3.5", "=", Class_cred1 * 3.5)
elif grade_1 == "C+":
    print(Class_cred1, "*2.5", "=", Class_cred1 * 2.5)
elif grade_1 == "C":
    print(Class_cred1, "*2.0", "=", Class_cred1 * 2.0)
elif grade_1 == "D":
    print(Class_cred1, "*1.0", "=", Class_cred1 * 1.0)
elif grade_1 == "F":
    print(Class_cred1, "*0.0", "=", Class_cred1 * 0.0)
else:
    print('Only one Class')
Class_cred2 = input('Enter the amount of credits for class 2 here:')
Class_cred2 = float(Class_cred2)
grade_2 = input('Enter the grade for class 2 here:')
if grade_2 == "A":
    print(Class_cred2, "*4.0", "=", Class_cred2 * 4.0)
    print('This is how many points you have for this class')
elif grade_2 == "B+":
    print(Class_cred2, "*3.5", "=", Class_cred2 * 3.5)
    print('This is how many points you have for this class')
elif grade_2 == "B":
    print(Class_cred2, "*3.0", "=", Class_cred2 * 3.0)
    print('This is how many points you have for this class')
elif grade_2 == "C+":
    print(Class_cred2, "*2.5", "=", Class_cred2 * 2.5)
    print('This is how many points you have for this class')
elif grade_2 == "C":
    print(Class_cred2, "*2.0", "=", Class_cred2 * 2.0)
    print('This is how many points you have for this class.')
elif grade_2 == "D":
    print(Class_cred2, "*1.0", "=", Class_cred2 * 1.0)
    print('This is how many points you have for this class.')
else:
    print(Class_cred2, "*0.0", "=", Class_cred2 * 0.0)
Class_cred3 = input('Enter the amount of credits for class 3 here:')
Class_cred3 = float(Class_cred3)
grade_3 = input('Enter the grade for class 3 here:')
if grade_3 == "A":
    print(Class_cred3, "*4.0", "=", Class_cred3 * 4.0)
    print('This is how many points you have for this class')
elif grade_3 == "B+":
    print(Class_cred3, "*3.5", "=", Class_cred3 * 3.5)
    print('This is how many points you have for this class')
elif grade_3 == "B":
    print(Class_cred3, "*3.0", "=", Class_cred3 * 3.0)
    print('This is how many points you have for this class')
elif grade_3 == "C+":
    print(Class_cred3, "*2.5", "=", Class_cred3 * 2.5)
    print('This is how many points you have for this class')
elif grade_3 == "C":
    print(Class_cred3, "*2.0", "=", Class_cred3 * 2.0)
    print('This is how many points you have for this class.')
elif grade_3 == "D":
    print(Class_cred3, "*1.0", "=", Class_cred3 * 1.0)
    print('This is how many points you have for this class.')
else:
    print(Class_cred3, "*0.0", "=", Class_cred3 * 0.0)
Class_cred4 = input('Enter the amount of credits for class 4 here:')
Class_cred4 = float(Class_cred4)
grade_4 = input('Enter the grade for class 4 here:')
if grade_4 == "A":
    print(Class_cred4, "*4.0", "=", Class_cred4 * 4.0)
    print('This is how many points you have for this class')
elif grade_4 == "B+":
    print(Class_cred4, "*3.5", "=", Class_cred4 * 3.5)
    print('This is how many points you have for this class')
elif grade_4 == "B":
    print(Class_cred4, "*3.0", "=", Class_cred4 * 3.0)
    print('This is how many points you have for this class')
elif grade_4 == "C+":
    print(Class_cred4, "*2.5", "=", Class_cred4 * 2.5)
    print('This is how many points you have for this class')
elif grade_4 == "C":
    print(Class_cred4, "*2.0", "=", Class_cred4 * 2.0)
    print('This is how many points you have for this class.')
elif grade_4 == "D":
    print(Class_cred4, "*1.0", "=", Class_cred4 * 1.0)
    print('This is how many points you have for this class.')
else:
    print(Class_cred4, "*0.0", "=", Class_cred4 * 0.0)
Extra=True
while Extra:
    More = input('Did you take more classes?')
    if More == "yes":
        More_1 = input('Enter the amount of credits here: ')
        More_1 = float(More_1)
        Xtra_G = input('Enter your grade here: ')
        if Xtra_G == "A":
            print(More_1, "*4.0", "=", More_1 * 4.0)
            print('This is how many points you have for this class')
        elif Xtra_G == "B+":
            print(More_1, "*3.5", "=", More_1 * 3.5)
            print('This is how many points you have for this class')
        elif Xtra_G == "B":
            print(More_1, "*3.0", "=", More_1 * 3.0)
            print('This is how many points you have for this class')
        elif Xtra_G == "C+":
            print(More_1, "*2.5", "=", More_1 * 2.5)
            print('This is how many points you have for this class')
        elif Xtra_G == "C":
            print(More_1, "*2.0", "=", More_1 * 2.0)
            print('This is how many points you have for this class.')
        elif Xtra_G == "D":
            print(More_1, "*1.0", "=", More_1 * 1.0)
            print('This is how many points you have for this class.')
        elif Xtra_G == "F":
            print(More_1, "*0.0", "=", More_1 * 0.0)
        else:
            print('Move along')
    break

#Final section where it tallys final semester GPA



