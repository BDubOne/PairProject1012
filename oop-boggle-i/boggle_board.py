import random
import string

class BoggleBoard:
  
  def __init__(self):
    # print("----\n----\n----\n----")
    pass
  
  @staticmethod
  def shake():
    count = 0
    while count <= 4:
        my_string = BoggleBoard.random_char(5)
        if "Q" in my_string:
          my_string = my_string.replace("Q", "Qu")
        print (my_string)
        count += 1
       
  @staticmethod
  # generates random char
  def random_char(y):
       return ''.join(random.choice(string.ascii_uppercase) for x in range(y))
  

  @staticmethod
  def start_game():
    #  print("----\n----\n----\n----")
    start = input("shake the board?(Y/n) ").upper()
    while start == "Y":
      BoggleBoard.shake()
      start = input("shake the board?(Y/n) ").upper()
    if start == "N":
      print("Bye")

      
  
    # creates boggle board
  # def generate_board():
    # def random_char(y):
    #    return ''.join(random.choice(string.ascii_uppercase) for x in range(y))
    # count = 0
    # while count <= 4:
    #     print (random_char(5))
    #     count += 1

  



# print (random_char(5))
# print (random_char(5))
# print (random_char(5))


# random.choice(string.ascii_uppercase)


  

# print(random.choice(string.ascii_uppercase))
# print("----\n----\n----\n----")

BoggleBoard.start_game()