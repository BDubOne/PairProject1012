import random
import string

class BoggleBoard:
  
  def __init__(self):
    # print("----\n----\n----\n----")
    pass
  

  def shake():
    count = 0
    while count <= 4:
        my_string = BoggleBoard.random_char(5)
        if "Q" in my_string:
          my_string = my_string.replace("Q", "Qu")
        print (my_string)
        count += 1
       
  # generates random char
  def random_char(y):
       return ''.join(random.choice(string.ascii_uppercase) for x in range(y))
  


  def start_game():
    #  print("----\n----\n----\n----")
    start = input("shake the board?(Y/n) ").upper()
    while start == "Y":
      BoggleBoard.shake()
      start = input("shake the board?(Y/n) ").upper()
    if start == "N":
      print("Bye")