#Script that is designed to find a match for a random number between 1 and 4096

import random
import time

#Lower limit for our random number
lower_limit = 0

#Upper limit for our random number
#Don't use numbers bigger than 1 million, otherwice finding a match can take quite a while
upper_limit = 524288    #524,288 = 2^19

#Number of tries until match is found
counter = 0

#x is the random number we want to find a match for
x = random.randint(lower_limit, upper_limit)

#Used to time how long the process of finding a match takes
time_to_find_match = time.process_time()

#Using while-loop here is a bit simpler as we don't have to limit the number of times the loop tries to find a match for x
#By limiting the random numbers to something under 1 million, this algorithm doesn't take unreasonable ammount of time
while(True):
    
    #Generate a random y until y == x
    #Attention! for y randint has to use the same parameters as we used for x 
    y = random.randint(lower_limit, upper_limit)

    if y == x:
        
        #elapsed_time_to_find_match times how long it takes to find a match for x 
        elapsed_time_to_find_match = time.process_time() - time_to_find_match
        
        print("\nA match has been found!")
        print(f"The number was: {x:,}")     #Having {:,} makes it so that large numbers have comma separators in them, improving readability
        print(f"It took {counter:,} tries to find")
        print(f"It took {elapsed_time_to_find_match:.6f} seconds to find \n")  #{:.6f} means that we want to show 6 decimals of the timer
        
        #THIS BREAK IS REALLY IMPORTANT
        #We want to stop the loop after the first match is found
        break

    #If y is not a match for x, then we add 1 to the counter
    if y != x:
        counter = counter + 1
