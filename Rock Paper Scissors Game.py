from getpass import getpass as input

print("E P I C    🪨  📄 ✂️    B A T T L E ")
print()
print("Select your move (r, p or s)")
print()

player1Score = 0
player2Score = 0

while True:
  player1Move = input("Player 1 > ")
  print()
  player2Move = input("Player 2 > ")
  print()

  if(player1Move=="r"):
    if(player2Move=="r"):
      print("You both picked Rock, draw!")
    elif(player2Move=="s"):
      print("Player1 smashed Player2's Scissors into dust with their Rock!")
      player1Score += 1
    elif(player2Move=="p"):
      print("Player1's Rock is smothered by Player2's Paper!")
      player2Score += 1
  elif(player1Move=="p"):
    if(player2Move=="r"):
      print("Player2's Rock is smothered by Player1's Paper!")
      player1Score += 1
    elif(player2Move=="s"):
      print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
      player2Score += 1
    elif(player2Move=="p"):
      print("Two bits of paper flap at each other. Dissapointing. Draw.")
  elif(player1Move=="s"):
    if(player2Move=="r"):
      print("Player 2's Rock makes metal-dust out of Player1's Scissors")
      player2Score += 1
    elif(player2Move=="s"):
      print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw.")
    elif(player2Move=="p"):
      print("Player1's Scissors make confetti out of Player2's paper!")
      player1Score += 1

    print("Player 1 has", player1Score, "wins.")
    print("Player 2 has", player2Score, "wins.")

    if player1Score == 3 or player2Score == 3:
       print("Thanks for playing!")
       exit()
    else:
      continue