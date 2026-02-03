print("Welcome to Quiz game")

player = input("Do you want to play? (Yes/No): ")

if player.lower() == "yes":
    print("Let's Play")
else:
    print("Okay, maybe next time!")
    exit()

score = 0

# Question 1
answer = input(
    "1) What is the real reason people go to the office?\n"
    "A) To work\n"
    "B) For salary\n"
    "C) For free Wi-Fi\n"
    "D) To complain about work\n"
    "Your answer: "
).lower()
if answer == "b":
    print("Correct\n")
    score += 1
else:
    print("Wrong (Correct answer: B)\n")


# Question 2
answer = input(
    "What happens to motivation on Monday morning?\n"
    "A) Increases\n"
    "B) Stays the same\n"
    "C) Goes on leave\n"
    "D) Gets promoted\n"
    "Your answer: "
).lower()
if answer == "c":
    print("Correct\n")
    score += 1
else:
    print("Wrong (Correct answer: C)\n")


# Question 3

answer = input(
    "What do people say when they haven’t done the work?\n"
    "A) I forgot\n"
    "B) I was busy\n"
    "C) I didn’t get the mail\n"
    "D) All of the above\n"
    "Your answer: "
).lower()
if answer == "d":
    print("Correct\n")
    score += 1
else:
    print("Wrong (Correct answer: D)\n")


# Question 4

answer = input(
    "What is the fastest thing in the office?\n"
    "A) Internet\n"
    "B) Boss\n"
    "C) Deadline\n"
    "D) Gossip\n"
    "Your answer: "
).lower()
if answer == "d":
    print("Correct\n")
    score += 1
else:
    print("Wrong (Correct answer: D)\n")

# Question 5

answer = input(
    "What do we actually do in a “5-minute break?\n"
    "A) Drink water\n"
    "B) Stretch\n"
    "C) Check phone for 30 minutes\n"
    "D) Return in 5 minutes\n"
    "Your answer: "
).lower()
if answer == "c":
    print("Correct\n")
    score += 1
else:
    print("Wrong (Correct answer: C)\n")


# Question 6

answer = input(
    "What increases more than salary?\n"
    "A) Experience\n"
    "B) Responsibilities\n"
    "C) Stress\n"
    "D) All of the above\n"
    "Your answer: "
).lower()
if answer == "c":
    print("Correct\n")
    score += 1
else:
    print("Wrong (Correct answer: C)\n")

# Question 7

answer = input(
    "What do people say when the task is very hard?\n"
    "A) Easy\n"
    "B) Done already\n"
    "C) Almost finished\n"
    "D) Let’s check\n"
    "Your answer: "
).lower()
if answer == "c":
    print("Correct\n")
    score += 1
else:
    print("Wrong (Correct answer: C)\n")


# Question 8

answer = input(
    "What works hardest in the office?\n"
    "A) Employees\n"
    "B) Manager\n"
    "C) Coffee machine\n"
    "D) Printer\n"
    "Your answer: "
).lower()
if answer == "c":
    print("Correct\n")
    score += 1
else:
    print("Wrong (Correct answer: C)\n")


# Question 9
answer = input(
    "What is the most common words used in our office?\n"
    "A) Partiallity\n"
    "B) Comparison\n"
    "C) Discrimination\n"
    "D) All the above\n"
    "Your answer: "
).lower()
if answer == "D":
    print("Correct\n")
    score += 1
else:
    print("Wrong (Correct answer: D)\n")


# Question 10
answer = input(
    "What do people say when they are late?\n"
    "A) Sorry\n"
    "B) Traffic\n"
    "C) On the way\n"
    "D) All of the above\n"
    "Your answer: "
).lower()
if answer == "d":
    print("Correct\n")
    score += 1
else:
    print("Wrong (Correct answer: D)\n")
    

print(f"Quiz Finished! Your Score: {score} / 10")

if score >= 8:
    print("Office Legend")
elif score >= 5:
    print("Office Survivor")
else:
    print("Intern vibes")

input("\nPress Enter to exit...")























    
























            
