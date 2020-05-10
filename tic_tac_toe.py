import random

board=[0,1,2,
       3,4,5,
       6,7,8]
def create_board():

    print(board[0] , ' | ' , board[1] , ' | ' , board[2])
    print('-----------')
    print(board[3] , ' | ' , board[4] , ' | ' , board[5])
    print('-----------')
    print(board[6] , ' | ' , board[7] , ' | ' , board[8])

def check(char, space1,space2,space3):
    if board[space1] == char and board[space2] == char and board[space3] == char:
        return True
def checkAll(char):
    if check(char,0,1,2):
       return True
    elif check(char,1,4,7):
       return True
    elif check(char,2,5,8):
       return True
    elif check(char,0,3,6):
        return True
    elif check(char,3,4,5):
        return True
    elif check(char,6,7,8): 
        return True
    elif check(char,0,4,8):
        return True
    elif check(char,2,4,6):
        return True

letter=''  
while not(letter == 'X' or letter == 'O'):
    print("Do you want to be X or O")

    letter = input().upper()       
while True:

    create_board()
    choice=int(input("Please choose an empty space from (0-8):"))

    
    if board[choice] !='X' and board[choice] !='O':
         board[choice]='X'

         if checkAll('X')==True:
             print("You won!!")
             break
                
         while True:
             random.seed()
             play_2=random.randint(0,8)

             if board[play_2]!='O' and board[play_2] !='X':
                 board[play_2] ='O' 

                 if checkAll('O')==True:
                      print("computer is winner!!")
                      break
                 break
   
print("The the space is already occupied!!")

    

