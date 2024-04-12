from generate_audio.build_routine_audio import build_instruction_set_audio
from generate_moves import generate_random_routine
import sys

def show_menu_options():
    print("\n" +
        "1. Generate Shadowboxing Routine\n" +
        "2. Quit" +
        "\n")

def option_shadowboxing_routine():
    user_input = input("Enter number of moves: ")
    moves = int(user_input)
    if moves == 0:
        print("\nError: not a number, returning to main menu\n")
        
    move_routine = generate_random_routine(moves)
    
    print("Saving routine . . . ")
    build_instruction_set_audio(move_routine)
    print(f"Finished routine with {moves} moves!")    

while True:
    show_menu_options()

    user_input = input("Option: ")
    match user_input:
        case "1":
            option_shadowboxing_routine()
        case "2":
            break