class character:
  name = None
  health = "100"
  mp = "100"

  def __init__(self, name):
    self.name = name

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}")

  def setStats(self, health, mp):
    self.health = health
    self.mp = mp

class player(character):
  nickname = None
  lives = 3

  def __init__(self, nickname):
    self.name = "Player"
    self.nickname = nickname

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tNickname: {self.nickname}\tLives: {self.lives}")

  def isAlive(self):
    if self.lives > 0:
      print(f"{self.nickname} lives on!")
      return True
    else:
      print(f"{self.nickname} has expired!")
      return False

print("🌟Generic RPG🌟")
print()
ian = player("Ian the mighty")
ian.print()
ian.isAlive()
print()

class enemy(character):
  type = None
  strength = None

  def __init__(self, name, type, strength):
    self.name = name
    self.type = type
    self.strength = strength

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}")

class orc(enemy):
  speed = None

  def __init__(self, speed):
    self.name = "Orc"
    self.type = "Orc"
    self.strength = 200
    self.speed = speed

  def print(self):
    print(f"{self.name}\t\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\t\tStrength: {self.strength}\tSpeed: {self.speed}")

sharron = orc(250)
gary = orc(205)
ozzy = orc(225)

sharron.print()
gary.print()
ozzy.print()

class vampire(enemy):
  day = None

  def __init__(self, day):
    self.name = "Vampire"
    self.type = "Vampire"
    self.strength = 150
    self.day = day

  
  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tDay/Night?: {self.day}")

eric = vampire("Night")
lestat = vampire("Day")

eric.print()
lestat.print()