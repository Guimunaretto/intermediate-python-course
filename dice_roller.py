def main():
 import random
 dice_sum = 0
 dice_rolls = int(input('How many die do you want to roll? '))
 dice_size = int(input('How many sides each die? '))

 for i in range (0,dice_rolls):    
	 roll = random.randint(1,6)
	 dice_sum += roll
	 if roll == 1:
	 	print(f'You have rolled a {roll}! Critical Fail!')
	 elif roll == dice_size:
	 	print(f'You have rolled a {roll}! Critical Success!')
	 else:
	 	print(f'You have rolled a {roll}')
 print (f'You have rolled a sum of {dice_sum}') 

if __name__== "__main__":
  main()
