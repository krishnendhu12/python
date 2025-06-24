name=input("Krishnendhu: ")
USN=input("1AY24bt023: ")
import random
dice = ['brain', 'footsteps', 'shotgun']
brains = 0
shotguns = 0
print("Bot's turn:")
for _ in range(3):
    roll = random.choice(dice)
    print("Rolled:", roll)
    if roll == 'brain':
        brains += 1
    elif roll == 'shotgun':
        shotguns += 1
print("Brains collected:", brains)
print("Shotguns hit:", shotguns)
if shotguns >= 3:
    print("Turn over due to shotguns!")
