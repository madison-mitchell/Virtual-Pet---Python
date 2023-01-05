class VirtualPet:

  def __init__(self,
               name,
               health=100,
               hunger=50,
               thirst=50,
               energy=75,
               entertainment=35):
    self.name = name
    self.health = health
    self.hunger = hunger
    self.thirst = thirst
    self.energy = energy
    self.entertainment = entertainment
    self.isAlive = True

  def __str__(self):
    return f"{self.name}{self.health}"

  def feed(self):
    self.hunger += 31
    self.thirst -= 7

  def water(self):
    self.thirst += 37

  def nap(self):
    self.energy += 83
    self.hunger -= 13
    self.thirst -= 19

  def play(self):
    self.entertainment += 43
    self.hunger -= 5
    self.thirst -= 9
    self.health -= 3

  def heal(self):
    self.health = 103
    self.hunger = 107
    self.thirst = 111
    self.energy = 53
    self.entertainment = 31

  def checkIsAlive(self):
    if self.energy < 0:
      self.energy = 0
      self.health -= 9

    if self.hunger < 0:
      self.hunger = 0
      self.health -= 10

    if self.thirst < 0:
      self.thirst = 0
      self.health -= 18

    if self.health <= 0:
      self.isAlive = False
      print(f"Oh no! {self.name} fainted!")

  def endTurn(self):
    self.health -= 3
    self.hunger -= 7
    self.thirst -= 11
    self.energy -= 13
    self.entertainment -= 11

    if self.health > 100:
      self.health = 103

    if self.hunger > 100:
      self.hunger = 107

    if self.thirst > 100:
      self.thirst = 111

    if self.energy > 100:
      self.energy = 113

    if self.entertainment > 100:
      self.entertainment = 111

  def getStatus(self):
    print(f"\n{self.name}\'s status:")
    print("-----------------------------------------------------------------")
    print("| HEALTH\t| HUNGER\t| THIRST\t| ENERGY\t| ENTERTAINMENT\t|")
    print(
      f"| {self.health} \t\t| {self.hunger} \t\t| {self.thirst} \t\t| {self.energy} \t\t| {self.entertainment}\t\t\t|"
    )
    print("-----------------------------------------------------------------")