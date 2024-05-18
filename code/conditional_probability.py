import enum
import random

class Kid(enum.Enum):
    Boy = 0
    Girl = 1
    
def random_kid() -> Kid:
    return random.choice([Kid.Boy, Kid.Girl])

both_girls = 0
either_girls = 0
older_girls = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    if older == Kid.Girl:
        older_girls+=1
    if older == Kid.Girl and younger == Kid.Girl:
        both_girls+=1
    if older == Kid.Girl or younger == Kid.Girl:
        either_girls+=1

print("P(both | older):", both_girls / older_girls)
print("P(both | either):", both_girls / either_girls)
