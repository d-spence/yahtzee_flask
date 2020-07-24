
from random import SystemRandom

def roll_dice(dice=[0,0,0,0,0], held=[]):
    """Roll a set of 5 virtual dice

    dice: current set of dice to be rolled (default is all zeroes)
    held: index of dice not being rolled (default is blank list)"""

    for i in range(5):
        if i not in held or dice[i] == 0:
            dice[i] = SystemRandom().randint(1, 6)

    return dice


def get_dice_imgs(dice=[0,0,0,0,0], held=[]):
    """Return a list of dice images in place of numbers
    
    If dice index is in held list, an alternate dice img name is used"""

    d_imgs = []
    for pos, d in enumerate(dice):
        if pos not in held:
            d_imgs.append(f"dice{d}.png")
        else:
            d_imgs.append(f"dice{d}_h.png")

    return d_imgs
