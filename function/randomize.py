import random

def shuffle_teams(TEAMS):           # Shuffle teams
    random.shuffle(TEAMS)

def shuffle_single_round(Round):    # Shuffle games in single round
    round_games = Round[1:]
    random.shuffle(round_games)
    Round = [Round[0]]+round_games
    return Round

def shuffle_all_rounds(Table):      # Shuffle games around the rounds in TB
    for rd in range(len(Table)):
        Table[rd] = shuffle_single_round(Table[rd])

def fix_rule_3(Table, TEAMS):
    TEAMS_QTY = len(TEAMS)
    checklist = []

    for rd in range(1, TEAMS_QTY-1):
        g = 1
        if rd%2 == 1:
            for game in Table[rd][1:]:
                Table[rd][g] = (game[1], game[0])
                g = (g % (TEAMS_QTY//2) ) + 1

    for rd in range(1,TEAMS_QTY-2):

        previous_home_teams = teams_home(Table[rd-1])
        previous_away_teams = teams_away(Table[rd-1])

        home_teams = teams_home(Table[rd])
        away_teams = teams_away(Table[rd])

        next_home_teams = teams_home(Table[rd+1])
        next_away_teams = teams_away(Table[rd+1])



        for team in home_teams:
            if team in previous_home_teams and team in home_teams and team in next_home_teams:
                checklist += [(team, rd)]
        
        for team in away_teams:
            if team in previous_away_teams and team in away_teams and team in next_away_teams:
                checklist += [(team, rd)]

    #print(checklist)
    if checklist:
        return False
    else:
        return True

def fix_new_rounds_nums(newTable, rd):
    i = 0
    for round in newTable:
        rd += 1
        newTable[i][0] = f'Rodada {rd:02}'
        i += 1
