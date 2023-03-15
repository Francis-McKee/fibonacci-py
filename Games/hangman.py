from random import *

player_score = 0
computer_score = 0

def start():
  print("Let's play a game of Hangman.")
  while game():
    pass
  scores()

def game():
  dictionary = ["python","javascript","html","css","swift","php"]
  word = choice(dictionary)
  word_length = len(word)
  clue = word_length * ["_"]
  tries = 6
  letters_tried = ""
  letters_wrong = 0
  global computer_score, player_score

  while (letters_wrong != tries) and ("".join(clue) != word):
    letter = guess_letter()
    if len(letter) == 1 and letter.isalpha():
      if letters_tried.find(letter) != -1:
        print("You've already picked", letter)
      else:
        letters_tried = letters_tried + letter
        first_index = word.find(letter)
        if first_index == -1:
          letters_wrong += 1
          print("Sorry,",letter,"isn't what I'm looking for.")
        else:
          print("Congratulations,",letter,"is correct.")
          for i in range(word_length):
            if letter == word[i]:
              clue[i] = letter
    else:
      print("Choose another.")

    print("".join(clue))
    print()
    print("Guesses: ", letters_tried)

    if letters_wrong == tries:
      print("Game Over.")
      print("The word was",word)
      computer_score += 1
      break
    if "".join(clue) == word:
      print("You win!")
      print("The word was",word)
      player_score += 1
      break
  return play_again()

def guess_letter():
  print()
  letter = input("Take a guess at the mystery word:")
  letter.strip()
  letter.lower()
  print()
  return letter

def play_again():
  answer = input("\nWould you like to play again? y/n: ")
  if answer in ("y", "Y", "yes", "Yes"):
    return answer
  else:
    print("Thank you for playing. See you next time!")
    print()

def scores():
  global player_score, computer_score
  print("\nHIGH SCORES")
  print("Player: ", player_score)
  print("Computer: ", computer_score)

if __name__ == '__main__':
  start()