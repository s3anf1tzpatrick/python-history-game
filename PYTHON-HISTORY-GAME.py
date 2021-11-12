print("Welcome to my History Quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes": 
    quit()

print("Okay, Let's Start")
score = 0

answer = input("How do historians refer to the time period in the 1730s and 1740s when colonists began embracing secular rationalism over religion? ").lower()
if answer == "the great awakening":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is The Great Awakening.")

answer = input("What Act were colonists protesting with the Boston Tea Party? ").lower()
if answer == "the stamp act":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The Correct Answer is The Stamp Act.")

answer = input("What city was the first capitol of the United States? ").lower()
if answer == "new york city":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is New York City.")

answer = input("Who was the first president to live in the White House? ").lower()
if answer == "john adams":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The Correct Answer is John Adams.")

answer = input("Who was the first president to declare war? ").lower()
if answer == "james madison":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The Correct Answer is James Madison.")

answer = input("What was the war that James Madison declared? ").lower()
if answer == "the war of 1812":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is The War of 1812.")

answer = input("Who was the first President to be Impeached? ").lower()
if answer == "andrew johnson":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Andrew Johnson.")

answer = input("About 4,000 members of which Native American tribe died of cold, hunger or disease on the Trail of Tears? ").lower()
if answer == "cherokee":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Cherokee.")

answer = input("What was the bloodiest single-day battle of American history? ").lower()
if answer == "the battle of antietam":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The answer is The Battle of Antietam.")

answer = input("Who was the Confederate president during the Civil War? ").lower()
if answer == "jefferson davis":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Jefferson Davis.")

print("You got " + str(score) + " questions correct!")
print("You scored " + str((score / 10) * 100) + "%.")