import random
from constants import RoutineConstants, BoxingMovesConstants

def generate_random_routine(moves):
    if type(moves) is not int:
        raise TypeError("Only integers are allowed")

    routine = ["Start"]

    for x in range(0, moves):
        option = random.random()
        if option > RoutineConstants.ATTACK_WEIGHT:
            attack_option = int(random.random() * len(BoxingMovesConstants.ATTACK_MOVES))
            routine.append(BoxingMovesConstants.ATTACK_MOVES[attack_option])
        elif option > RoutineConstants.DEFENSE_WEIGHT:
            defense_option = int(random.random() * len(BoxingMovesConstants.DEFENSE_MOVES))
            routine.append(BoxingMovesConstants.DEFENSE_MOVES[defense_option])
        elif option > RoutineConstants.PAUSE_WEIGHT:
            silence_option = int(random.random() * len(BoxingMovesConstants.SILENCE_OPTIONS))
            routine.append(BoxingMovesConstants.SILENCE_OPTIONS[silence_option])
            
    routine.append("finish")

    return routine