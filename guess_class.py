import random

class GuessGame:

    def __init__(self, range_min, range_max, guess_number=0):    
        self.range_min = range_min
        self.range_max = range_max 
        self.guess_number = random.randint(self.range_min , self.range_max)    
    
    def verify(self):
        print('- - - - - - - - - - - - ')
        print('= = = = NEW  GAME = = = ')

        verify_min = self.range_min

        verify_max = self.range_max                 

        for counter in range(51): 

            verify_range = range(verify_min , verify_max)
            middle_of_range = verify_max - int(len(verify_range)/2)           

            print('. . .')
            print('loop nbr ' + str(counter))
            print(verify_range)        
            print('middle_of_range (INT) is: ' + str(middle_of_range))
            print('. . .')
            print('the program return this value:')

            if self.guess_number == middle_of_range:
                print(0)
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
                print('+ + + PROGRAM WON + + +')
                print('~~~~~~~~~~~~~~~~~~~~~~~~')
                print('succeed in ' + str(counter) + ' loops')
                
                break

            elif self.guess_number < middle_of_range:
                print(-1)
                verify_max = middle_of_range
                
            elif self.guess_number > middle_of_range:
                print(1)
                verify_min = middle_of_range  
                        

            print('..............')

        else:
            print('_ _! YOU LOOSE !_ _')


######################################### 

newGame = GuessGame(1,1000000000000000)

newGame.verify()

print ('- - - the secret number was - - - ')
print (newGame.guess_number)
print('.  .  .  .  .  .  .  .  .  .  .  .  ')