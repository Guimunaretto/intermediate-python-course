def main():
 import random
 dice_sum = 0
 dice_rolls = 2
 for i in range(0,dice_rolls):    
 	 roll = random.randint(1,6)
 	 dice_sum += rolled
 print (f'You have rolled a sum of {dice_sum}') 
if __name__== "__main__":
  main()
