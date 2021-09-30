'''
GRADING 2.0
-------------------
Copy your Grading 1.0 program and modify it to also print out the letter grade depending on the numerical grade.
If they fail, tell them to "Transfer to Johnston!"
'''


grade = float(input("What is your current grade? "))
overall = grade
if overall >= 90:
    print("You're grades are fantastic! A+", overall)
elif overall >= 80:
    print("Your grades are great! B", overall)
elif overall >= 70:
    print("Your grades are good! C+", overall)
elif overall >= 60:
    print("Your grades are good! C+", overall)

else:
    print("Your grades suck! Go transfer to Johnston!")


