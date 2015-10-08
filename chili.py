import random
    guessesTaken = 0
    print ('Hello! What is your name?')
    myName = input ()
    number = random.randint(1, 100)
    #print number (to show the number for debugging purposes)
    print (myName + ' I am thinking of a number between 1 and 100.')
    my_list = []
    while guessesTaken < 10
        
        print('Take a guess.')
        guess = input()
        guess = int(guess)
        my_list.append(guess)
        try:
           my_list.index(guess)
        except ValueError:
          "Do nothing"
        else:
          print 'Please try again, you have already guessed this number.'
        guessesTaken = guessesTaken + 1
        print number, 'this is num' 
        #'this is number' 
        #add to differentiate to test 
        #print guessesTaken
        if guess == number: 
            print ('Good job,' + myName + '!You guessed my number in ' + str(guessesTaken) + ' guesses!')
            break
        elif guess < number:
            print ('Your guess is too low.')
        elif guess > number:
            print ('Your guess is too high.')
    if guessesTaken == 10:
        print('Sorry, the number I was thinking of was ' + str(number))
    #store in a list, compare to a number in the list

