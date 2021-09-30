'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''
score = 0
#Question 1
answer = input("What is the square root of 50405 * the square root of 50405? ")
if answer.lower() == "50405":
    print("Good job! You got it correct")
    score += 1
elif answer.lower() == "fifty thousand four hundred and five":
    print("Good Job, you got it right!")
    score+=1
else:
    print("Incorrect! The answer was 50405. Next question")



#Question 2
print("A. 28")
print("B. 36")
print("C. 42")
answer_2 = input("What is the area of a triangle with a base of 7 and a height of 8? ")

if answer_2.lower() == "a":
    print("Correct! good job")
    score += 1
else:
    print("Incorrect! The answer was A. Next question")



#Question 3
answer_3 = input("Who are the main characters of Red Dead Redemption 2? ")
if answer_3.lower() == "arthur morgan and john marston":
    print("Good job! you were correct")
    score += 1
elif answer_3.lower() == "john marston and arthur morgan":
    print("Good job! You were correct")
    score += 1

else:
    print("Incorrect! The answer was Arthur Morgan and John Marston")





#Question 4
print("A. Rio Bravo")
print("B. High plains drifter")
print("C. The searchers")
print("D. True grit")
answer_4 = input("What was John Waynes most famous film? ")
if answer_4.lower() == "c":
    print("Good job! You got it right")
    score += 1
else:
    print("Incorrect! It was C")




#Question 5
answer_5 = input("When did Michael Jordan sign with the Chicago White Sox? ")
if answer_5.lower() == "1994":
    print("Good job! you got it right!")
    score += 1
elif answer_5.lower() == "nineteen ninety four":
    print("Good Job! You got it right!")
    score += 1
else:
    print("Incorrect! It was 1994")


#Question 6
print("A. High Plains Drifter")
print("B. The good, The bad, and The Ugly")
print("C. Rio Bravo")
print("D. The outlaw Josey Wales")

answer_6 = input("Which one of these films did Clint Eastwood not act in? ")
if answer_6.lower() == "c":
    print("Good Job! You got it right!")
    score += 1
else:
    print("Incorrect! the answer was C")


#Question 7
answer_7 = input("How many title defenses does Canadian Mixed Martial Artist, Georges St-Pierre have? ")
if answer_7 == "9":
    print("Good Job! You got it right")
    score += 1
elif answer_7.lower() == "nine":
    print("Good Job! you got it right")
    score += 1
else:
    print("Incorrect, the correct answer was nine")


overall = score/7*100
if overall >= 90:
    print("You're grades are fantastic! A+", overall)
elif overall >= 80:
    print("Your grades are great! B", overall)
elif overall >= 70:
    print("Your grades are good! C+", overall)
elif overall >= 60:
    print("Your grades are good! D+", overall)
else:
    print("You got an F! Your grades suck! Go transfer to Johnston!", overall)





