turns = 2

import copy
def SHIFTS(turns):
    if turns >= 2:
        return 2
    else:
        return 1
SHIFTS = SHIFTS(turns)

def main():

    TEAMS = teams_to_list()                 # Teams now is a Python List

    shuffle_teams(TEAMS)                    # Shuffle Teams (1st shuffle)

    Table = init_table(len(TEAMS))          # To Generate Zeros Table

    all_Rounds(Table, TEAMS)                # To Generate all Rounds

    shuffle_all_rounds(Table)               # Shuffle all game Rounds (2nd shuffle)

    is_fixed = fix_rule_3(Table, TEAMS)     # Fix Home/Away Games (Rule 3)

    if SHIFTS >= 2:
        Table += mirror_Rounds(Table, TEAMS)    # To add the mirror Rounds

    all_checked = all_checks(Table, TEAMS, SHIFTS)

    if turns >= 3:
        rd = 38
        
        for turn in range(2, turns):
            if turn % 2 == 0:
                newTempTable = copy.deepcopy(Table[0:19])
                fix_new_rounds_nums(newTempTable, rd)
                Table += newTempTable

            else:
                newTempTable = copy.deepcopy(Table[19:38])
                fix_new_rounds_nums(newTempTable, rd)
                Table += newTempTable
            
            rd += 19

    if all_checked and is_fixed:
        print_table(Table)                  # Show Games Schedule
    
    else:
        raise ValueError("Something is Wrong with the Table")


main()