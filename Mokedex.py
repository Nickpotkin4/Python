mokedex = {"Beast Name": None, "Type": None, "Special Move": None, "HP": None, "MP": None}

print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾")
print()

for name in mokedex.keys():
  mokedex[name] = input(f"{name}:\t").strip().title()
  print()

if mokedex["Type"]=="Earth":
  print("\033[32m", end="")
elif mokedex["Type"]=="Air":
  print("\033[37m", end="")
elif mokedex["Type"]=="Fire":
  print("\033[31m", end="")
elif mokedex["Type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[0m")

for name, value in mokedex.items():
  print(f"{name:<15}: {value}")