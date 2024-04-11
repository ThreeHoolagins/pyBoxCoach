import random

attack = ["Jab", "Cross", "Hook", "Uppercut"]
defense = ["Slip", "Parry", "Duck", "Backup"]
actions = ["Start", "Stop"]
silence = ["halfSecondSilence", "secondSilence"]
class Boxing_Move:
    def __init__(self, move, has_LR):
        self.move = move
        self.has_LR = has_LR

thisList = []
for x in defense:
    thisList.append(Boxing_Move(x, True))

# for x in thisList:
#     LR = ""
#     if x.has_LR:
#         z = random.randint(0,1)
#         if z == 0:
#             LR = "Left"
#         else:
#             LR = "Right"
#     print(f"{LR} {x.move}")
