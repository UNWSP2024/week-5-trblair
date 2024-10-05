# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.
import random
def mathproblem():
    firstnum=random.randint(0,1000)
    secondnum=random.randint(0,1000)
    print(" ",firstnum,"\n+",secondnum,"\n------")
    useranswer=int(input())
    answer=firstnum+secondnum
    if useranswer == answer:
        print("Correct!")
    else:
        print("Incorrect!")
    mathproblem()


mathproblem()
