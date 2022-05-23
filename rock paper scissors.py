rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
option=(input("What do you want to choose:?'0' for rock, '1' for paper, '2' for scissors"))
computer=random.randint(0,2)
if option==0:
	print(rock)
	if computer==0:
		print(rock)
		print("draw!!")
	elif computer==1:
		print(paper)
		print("you lost!!")
	else:
		print(scissors)
		print("you won!!")
elif option==1:
	print(paper)
	if computer==0:
		print(rock)
		print("you won!!")
	elif computer==1:
		print(paper)
		print("draw!!")
	else:
		print(scissors)
		print("you lost!!")
else:
	print(scissors)
	if computer==0:
		print(rock)
		print("you lost!!")
	elif computer==1:
		print(paper)
		print("you won!!")
	else:
		print(scissors)
		print("draw!!")

