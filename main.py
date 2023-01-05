from VirtualPet import VirtualPet
import random
import os
import time

print("Welcome to Virtual Pet!")
petName = input("What would you like to name your pet?\n> ")

pet = VirtualPet(petName)

print(f"{pet.name} loves you already!")

pet.getStatus()

while pet.isAlive == True:
  if pet.entertainment <= 0:
    print(f"Oh no! {pet.name} chewed up your couch! >:|")
  elif pet.entertainment <= 15:
    print(
      f"{pet.name} is getting a little restless. You might want to play with them."
    )

  print("How do you want to interact with your pet?")
  userChoice = input("1.\tFeed\n2.\tWater\n3.\tNap\n4.\tPlay\n5.\tHeal\n> ")

  if userChoice == '1':
    pet.feed()
    os.system('clear')
    print(f"\n{pet.name}\'s belly is happy!")

  if userChoice == '2':
    pet.water()
    os.system('clear')
    print(f"\n{pet.name} is feeling hydrated!")

  if userChoice == '3':
    pet.nap()
    os.system('clear')
    print(f"\n{pet.name} enjoyed their \'cat\' nap.")

  if userChoice == '4':
    pet.play()
    pet.checkIsAlive()
    os.system('clear')
    if pet.isAlive == False:
      breakpoint
    else:
      if pet.health < 10 or pet.hunger < 10 or pet.thirst < 10:
        action = [
          f"\n{pet.name} didn't go fetch the tennis ball.",
          f"\n{pet.name} laid down and doesn't seem excited to move."
        ]
        random_action = random.choice(action)
        print(random_action)
      else:
        action = [
          f"\n{pet.name} caught the tennis ball and brought it back to you!",
          f"\n{pet.name} loves running around the doggo park and playing with their friends!"
        ]
        random_action = random.choice(action)
        print(random_action)

  if userChoice == '5':
    pet.heal()
    os.system('clear')
    print(f"{pet.name} is feeling much better!")

  if userChoice != '1' and userChoice != '2' and userChoice != '3' and userChoice != '4' and userChoice != '5':
    os.system('clear')
    print(
      "Invalid option entered. Please enter a number using the options below:")

  pet.endTurn()
  pet.checkIsAlive()

  time.sleep(1)
  os.system('clear')

  if (pet.health < 10
      and pet.health > 0) or pet.hunger < 10 or pet.thirst < 10:
    action = [
      f"\n{pet.name} doesn't seem to be feeling well.",
      f"\n{pet.name} laid down and isn't interested in playing."
    ]
    random_action = random.choice(action)
    print(random_action)

  if pet.isAlive == True:
    pet.getStatus()
  else:
    breakpoint
