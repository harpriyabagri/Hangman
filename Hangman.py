import random
HANGMANPICS = ['''

      +---+
      |   |
          |
          |
          |
          |
=================''', '''


      +---+
      |   |
      0   |
          |
          |
          |
=================''', '''


      +---+
      |   |
      O   |
      |   |
          |
          |
=================''', '''


      +---+
      |   |
      O   |
      |/  |
          |
          |
=================''', '''


      +---+
      |   |
      O   |
     \|/  |
          |
          |
=================''', '''


      +---+
      |   |
      O   |
     \|/  |
       \  |
          |
=================''', '''

      +---+
      |   |
      O   |
     \|/  |
     / \  |
          |
=================''']


WordBank = 'joy toy cat mouse house blanket feet hanger backpack jacket moo cow horse cloudy engineering freeze mississipi ranch shirt socks static light carrot water sink soap dish warm earring taco tag game guess letter shirt hall sweet salty sour savoury fifty sky trees windy sunny rainy tornado'
WordBank = WordBank.split()


def PickWord(WordBank):
      index = random.randint(0,len(WordBank)-1)
      word = WordBank[index]
      return word


def DisplayBoard(Incorrect_Letters, Correct_Letters, word, HANGMANPICS):
      print(HANGMANPICS[len(Incorrect_Letters)])
      print()
      print('Letters you\'ve already guessed: ',end=' ')
      print(Incorrect_Letters)
      print()


def DisplayLetters(letter, word):
      index = 0   
      while( index < len(word)):
            if word[index] in Correct_Letters:
                  print(word[index], end= ' ')
            else:
                  print("_", end= ' ')
            index = index +1
            print()

def CheckWinner(word, Correct_Letters):
      index = 0
      while(index < len(word)):
            if word[index] not in Correct_Letters:
                  return False
            index = index+1
      return True




letter = 'z'
play_again = 'yes'
while play_again == 'yes':
                  
      print("H A N G M A N")
            
      word = PickWord(WordBank)
      word = list(word)
      
      Incorrect_Letters = []
      
      Correct_Letters = []
      guesses = 0
      
      game_over = False
      while game_over == False:
            DisplayBoard(Incorrect_Letters, Correct_Letters, word, HANGMANPICS)
            DisplayLetters(letter, word)
            
            print("Take a guess")
            letter = input()
            letter = letter.lower()

            if len(letter) != 1:
                  print('Please enter a SINGLE letter')
                  letter = input ()
                  letter = letter.lower()
            elif letter not in 'qwertyuiopasdfghjklzxcvbnm':
                  print("Please guess a aphabetical LETTER")
                  print("Take a guess")
                  letter = input()
                  letter = letter.lower()
                  
            if letter in Incorrect_Letters:
                  print("You've already guessed this letter. Please guess again.")
                  letter = input()
                                   
            if letter in word:
                  print("Good Guess!")
                  Correct_Letters.append(letter)
                  game_over = CheckWinner(word, Correct_Letters)
                  
            elif letter not in word:
                  print("Try again!")
                  Incorrect_Letters.append(letter)
                  
            if len(Incorrect_Letters) == len(HANGMANPICS):
                  game_over = True

      if CheckWinner(word, Correct_Letters) == True:
            print("Congratulation! You have won! The word was", end=' ')
            print(word)
      else:
            print('Hangman. The word was ', end=' ')
            print(word, end =' ')
            print("Better luck next time!")

      print('Do you want to play again? (yes or no)')
      play_again = input()
      if play_again != 'yes':
            print("Goodbye.")
            

            




