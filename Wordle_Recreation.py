import random
from colorama import Fore
#The ASCII Art is from https://patorjk.com/software/taag/#p=display&f=Star%20Wars&t=Ascii
#The dictionary code comes from https://perchance.org/fiveletter
#The idea of the count function comes from https://www.simplilearn.com/tutorials/python-tutorial/count-in-python#:~:text=Python's%20count()%20function%20is,in%20a%20list%20or%20tuple.
word = ""
game = 0
coloredList = [Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET, Fore.RESET]


def title():
  print(
      """____    __    ____  ______   .______       _______   __       _______ 
\   \  /  \  /   / /  __  \  |   _  \     |       \ |  |     |   ____|
 \   \/    \/   / |  |  |  | |  |_)  |    |  .--.  ||  |     |  |__   
  \            /  |  |  |  | |      /     |  |  |  ||  |     |   __|  
   \    /\    /   |  `--'  | |  |\  \----.|  '--'  ||  `----.|  |____ 
    \__/  \__/     \______/  | _| `._____||_______/ |_______||_______|
                                                                     """)


def setWord(word):
  with open("dictionary.lock") as wordList:
    read_file = wordList.read()
    wordList = list(map(str, read_file.split()))
    word = random.choice(wordList)
    return word


def encrypt(guess, wordList, coloredList):
  max = []
  colors = ["N", "N", "N", "N", "N"]
  for i in range(5):
    max.insert(i, (wordList.count(guess[i])))
    if ("Y" + guess[i]) or ("G" + guess[i]) in colors:
      max[i] -= 1
    if guess[i] == wordList[i]:
      coloredList[i] = Fore.GREEN + guess[i]
      colors[i] = "G" + guess[i]
    else:
      if guess[i] in wordList and max[i] >= 1:
        coloredList[i] = Fore.YELLOW + guess[i]
        colors[i] = "Y" + guess[i]
        max[i] -= 1
      else:
        coloredList[i] = Fore.RESET + guess[i]
        colors[i] = "N" + guess[i]
    colors = ["N", "N", "N", "N", "N"]
  Fore.RESET
  return guess, wordList


def menu(mode):
  print("What do you want to do?")
  print("  1. Play")
  print("  2. Instructions")
  mode = int(input("I want to: "))
  if mode == 1:
    print()
    return mode
  else:
    print()
    Fore.RED
    print(""".______       __    __   __       _______     _______.   
|   _  \     |  |  |  | |  |     |   ____|   /       | _ 
|  |_)  |    |  |  |  | |  |     |  |__     |   (----`(_)
|      /     |  |  |  | |  |     |   __|     \   \       
|  |\  \----.|  `--'  | |  `----.|  |____.----)   |    _ 
| _| `._____| \______/  |_______||_______|_______/    (_)
                                                         """)
    print("  1. You have to guess a 5 letter word")
    print("  2. You have 6 tries to guess the word")
    print("  3. If you guess a letter correctly:")
    print("      1.Green: It's in the word and in the right spot")
    print("      2.Yellow: It's in the word but in the wrong spot\n\n")
    return mode


word = str(setWord(word))
wordList = list(word)
numOfLet = []
num = 1
count = 0

title()
menu(game)

guess = list(input(str(Fore.RESET + "Guess a 5 letter word: ")))
while guess != wordList and count != 5:
  encrypt(guess, wordList, coloredList)
  print("\n", "".join(coloredList), "\n")
  guess = list(input(str(Fore.RESET + "Guess a 5 letter word: ")))
  count += 1
if guess == wordList:
  encrypt(guess, wordList, coloredList)
  print("\n", "".join(coloredList), "\n")
  print(
      Fore.RESET +
      """____    ____  ______    __    __     ____    __    ____  ______   .__   __.  __  
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / /  __  \  |  \ |  | |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   / |  |  |  | |   \|  | |  | 
  \_    _/  |  |  |  | |  |  |  |      \            /  |  |  |  | |  . `  | |  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /   |  `--'  | |  |\   | |__| 
    |__|     \______/   \______/         \__/  \__/     \______/  |__| \__| (__)  
                                                                                                  """
  )
elif count == 5:
  print(
      """  _______      ___      .___  ___.  _______      ______   ____    ____  _______ .______      
 /  _____|    /   \     |   \/   | |   ____|    /  __  \  \   \  /   / |   ____||   _  \     
|  |  __     /  ^  \    |  \  /  | |  |__      |  |  |  |  \   \/   /  |  |__   |  |_)  |    
|  | |_ |   /  /_\  \   |  |\/|  | |   __|     |  |  |  |   \      /   |   __|  |      /     
|  |__| |  /  _____  \  |  |  |  | |  |____    |  `--'  |    \    /    |  |____ |  |\  \----.
 \______| /__/     \__\ |__|  |__| |_______|    \______/      \__/     |_______|| _| `._____|
                                                                                             """
  )
  print("\nThe word was", word + ".")
