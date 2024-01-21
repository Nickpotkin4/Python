import os, time

f = open("high.score", "r")
scores = f.read().split("\n")
f.close()

highscore = 0
name = None

for row in scores:
  data = row.split()
  if data != []:
    if int(data[1]) > highscore:
      highscore = int(data[1])
      name = data[0]

print("🌟Current Leader🌟")
print()
print("Analyzing high scores...")
print()
print("The winner is", name, "with", highscore)
time.sleep(4)
os.system("clear")
exit()