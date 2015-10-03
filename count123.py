""" Counts the numbers from 3 to 117. But for multiples of three add 3 instead of
 1 and for the multiples of five add 5 instead of 1. For numbers which are
 multiples of both three and five add 15 instead of 1. Ex: If we are looking at
 numbers 5 to 15 (inclusive), the program would output 39
"""
import sys
import math

output = 0 #counts the numbers
x = 0 #user input from 3 to 117
c = '' #user input string

def main():
    global c, x, output
    print "Counts the numbers from 3 to 117 until you enter"
    print "'Q' for Quit\n"

    while (c != 'q') :

        c = raw_input("Enter a number from 3 to 117 or [Q]uit: ").lower()
        
        if c.isdigit(): #checking if the input is a digit 
            x = int(c)

            if (x < 3): #checks if the input is within the range 
                print "The number should be between 3 and 117" 
            elif (x > 117): #checks if the input is within the range
                print "The number should be between 3 and 117"
            elif ((x%5==0) and (x%3== 0)): # checks multiples of three and five
                output += 15		
            elif x%5==0:            # checks multiples of five
                output += 5
            elif x%3==0:            # checks multiples of three
                output += 3      
            else:              	    # every other input is counted as 1
                output += 1  
            print "Running count: %d" % output
        elif c == 'q':         
                print "Enter 'OK' with mouse or press Enter"
                gb = raw_input("Bye. [Hit Enter]")
        else:
            print "Enter an integer between 3 and 117" 
             

    print "\nFinal Count: %d" % output
    
if __name__ == "__main__":
    main()