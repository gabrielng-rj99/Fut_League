def all_games(TEAMS, away=False):   # Creating all possible games for future check
    all_games_possibilities = []

    for i in range(len(TEAMS)):
        for j in range(i+1, len(TEAMS)):
            game_home = (TEAMS[i], TEAMS[j])
            all_games_possibilities += [game_home]
            if away:
                game_away = (TEAMS[j], TEAMS[i])
                all_games_possibilities += [game_away]

    return all_games_possibilities

# __________________________________________________________________________
## Checking/Verification Functions
def check_games_possibilities(TEAMS):
    teams_appearences = []
    all_games_P = all_games(TEAMS)  # [P]ossibilities

    for team in TEAMS:
        appears = 0
        for game in all_games_P:
            if team in game:
                appears += 1

        teams_appearences += [(team, appears)]

    # print(len(teams_appearences))

    # for check in teams_appearences:
    #     print(check)

    for i in range(len(teams_appearences)):
        if teams_appearences[i][1] != len(TEAMS)-1:
            return False
        
    return True

def check_game_number_each_team(Table, TEAMS, SHIFTS):   # Show if each team played
    flag = True                             # correct number of games
    TEAMS_QTY = len(TEAMS)
    for team in TEAMS:
        counter = 0

        if team == "R" or team=="o": # For "A", "B", "C",[...],"R",[...] scenario
            counter = (TEAMS_QTY-1)*-SHIFTS

        for Round in Table:
            for game in Round:
                if team in game:
                    counter += 1
        
        #print(team, counter)

        if counter != (TEAMS_QTY-1)*SHIFTS:
            flag = False
            break

    return flag

def check_IAGWP(Table, TEAMS):                  # [I]f [A]ll [G]ames [W]ere [P]layed	
    all_games_P = all_games(TEAMS)
    
    for Round in Table:
        for game in Round:
            game_back = tuple(reversed(game)) 

            if game in all_games_P:
                all_games_P.remove(game)

            elif game_back in all_games_P:
                all_games_P.remove(game_back)

        # print(len(all_games_P))

    if all_games_P:
        return False
    
    if not all_games_P:
        return True

def all_checks(Table, TEAMS, SHIFTS):
    chk_GP    = check_games_possibilities(TEAMS)
    chk_GNET  = check_game_number_each_team(Table, TEAMS, SHIFTS)
    chk_IAGWP = check_IAGWP(Table, TEAMS)

    return all([chk_GP, chk_GNET, chk_IAGWP])
