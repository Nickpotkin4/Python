from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    pause = int(input("Press 2 anytime to stop playback and go back to the menu: "))
    if pause == 2:
      source.paused = True
      return
    else:
      continue

while True:
  # clear the screen 
  os.system('clear')
  # Show the menu
  print("🎵 MyPOD Music Player ")
  print()
  time.sleep(1)
  print("Press 1 to Play")
  print("Press 2 to Exit")
  time.sleep(1)
  print("Press anything else to see the menu again")
  print()
  # take user's input
  userInput = int(input("> "))
  print()
  # check whether you should call the play() subroutine depending on user's input
  if userInput == 1:
    print("Playing some tunes dude!")
    play()
  elif(userInput == 2):
    exit()
  else:
    continue