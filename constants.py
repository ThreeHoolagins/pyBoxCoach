from boxing_move import BoxingMove

class FileLocationConstants:
    AUDIO_SRC_PATH = "./Audio Resources/Boxing Audio"

class BoxingMovesConstants:
    JAB = BoxingMove("Jab", False)
    CROSS = BoxingMove("Cross", False)
    HOOK = BoxingMove("Hook", True)
    UPPERCUT = BoxingMove("Uppercut", True)
    ATTACK_MOVES = [JAB, CROSS, HOOK, UPPERCUT]
    
    SLIP = BoxingMove("Slip", True)
    PARRY = BoxingMove("Parry", True)
    DUCK = BoxingMove("Duck", False)
    BACKUP = BoxingMove("Backup", False)
    DEFENSE_MOVES = [SLIP, PARRY, DUCK, BACKUP]
    
    ACTION_OPTIONS = ["Start", "Stop", "Finish"]
    SILENCE_OPTIONS = ["halfSecondSilence", "secondSilence"]

class RoutineConstants:
    ATTACK_WEIGHT = 1 - .6
    DEFENSE_WEIGHT = ATTACK_WEIGHT - .2
    PAUSE_WEIGHT = DEFENSE_WEIGHT - .1