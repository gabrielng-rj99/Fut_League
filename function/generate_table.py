from tkinter import Tk, filedialog

POSSIBLE_CHARS = {
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', ' ', 'ç', 'Ç', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'Á', 'Â', 'Ã', 'À', 'Ä', 'á', 'â', 'ã', 'à', 'ä',
    'É', 'Ê', 'Ẽ', 'È', 'Ë', 'é', 'ê', 'ẽ', 'è', 'ë',
    'Í', 'Î', 'Ĩ', 'Ì', 'Ï', 'í', 'î', 'ĩ', 'ì', 'ï',
    'Ó', 'Ô', 'Õ', 'Ò', 'Ö', 'ó', 'ô', 'õ', 'ò', 'ö',
    'Ú', 'Û', 'Ũ', 'Ù', 'Ü', 'ú', 'û', 'ũ', 'ù', 'ü',
}

def teams_to_list():
    Teams = []

    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    
    if file_path:
        Teams_txt = open(file_path, mode='r+', encoding='UTF-8')
    
    for team in Teams_txt:    
        if team == '\n':
            break

            
        Teams += [team[:-1]]

    Teams_txt.close()

    for team in Teams:
        for char in team:
            if char not in possible_chars:
                raise ValueError("Teams must be alphanumeric or hifen (-)")

    if len(Teams)<=2:
        raise IndexError("The number of teams must be greater than 2")

    if len(Teams)%2 != 0:
        Teams += ["__Null__"]

    return Teams

def init_table(TEAMS_QTY):              # Table that all games are "0x0"
    Table_0 = list(range(TEAMS_QTY-1))
    
    for i in range(TEAMS_QTY-1):
        Table_0[i] = [f"Rodada {i+1:02}"]
        Table_0[i] += [[0,0]]*(TEAMS_QTY//2)

    return Table_0

def first_round(Table, TEAMS):          # Change the First Round
    TEAMS_QTY = len(TEAMS)
    g = 1  # Game Counter
    all_games_P = all_games(TEAMS) # [P]ossibility

    for team in TEAMS:
        round_teams = teams_that_played(Table[0])
        if team in round_teams:
            continue
        else:
            for game in all_games_P:
                team1 = game[0]
                team2 = game[1]

                if team in game:
                    if team1 not in round_teams and team2 not in round_teams:
                        Table[0][g] = game
                        round_teams = teams_that_played(Table[0])
                        g = (g % (TEAMS_QTY//2) ) + 1
                        continue
                
        continue

def teams_that_played(round):                    # Team list that played in the round
    teams_list = []
    
    for game in round:
        teams_list += [game[0], game[1]]

    teams_list = teams_list[2:]

    return teams_list

def teams_home(Round):
    teams_home = []
    
    for game in Round[1:]:
        teams_home += [game[0]]
    return teams_home

def teams_away(Round):
    teams_away = []
    
    for game in Round[1:]:
        teams_away += [game[1]]
    
    return teams_away
    
def rotation(home_teams, away_teams):

    axys = home_teams[0]

    AT_1st  = away_teams[0]         # First  [A]way [T]eam
    HT_2nd  = home_teams[1]         # Second [H]ome [T]eam
    HT_last = home_teams[-1]        # Last   [H]ome [T]eam

    new_home_teams = [axys] + [AT_1st] + [HT_2nd] + home_teams[2:-1]
    new_away_teams = away_teams[1:] + [HT_last]

    return new_home_teams, new_away_teams

# __________________________________________________________________________
# To Generate Next Rounds
def all_Rounds(Table, TEAMS):

    rd = 1  # Round Counter
    g = 1   # Game Counter
    TEAMS_QTY = len(TEAMS)


    while rd < TEAMS_QTY-1:

        Round = Table[rd][1:]
        
        home_teams = teams_home(Table[rd-1])
        away_teams = teams_away(Table[rd-1])

        new_home_teams = rotation(home_teams, away_teams)[0]
        new_away_teams = rotation(home_teams, away_teams)[1]

        for game in Round:
            game = (new_home_teams[g-1], new_away_teams[g-1])

            Table[rd][g] = game  
            
            g = (g % (TEAMS_QTY//2) ) + 1


        rd += 1

def mirror_Rounds(Table, TEAMS):

    TEAMS_QTY = len(TEAMS)
    newTable = Table_0(TEAMS_QTY)    

    rd = 0  # Round Counter
    g = 1   # Game Counter

    while rd < TEAMS_QTY-1:

        newTable[rd][0] = f"Rodada {rd+TEAMS_QTY}"
        Round = Table[rd][1:]

        for game in Round:                       
            newTable[rd][g] = tuple(reversed(game))            
            g = (g % (TEAMS_QTY//2) ) + 1


        rd += 1

    return newTable

# __________________________________________________________________________
# To Print the table
def print_table(Table):                     # Show Games Schedule    
    print()
    for Round in Table:
        print (Round[0])
        for game in Round[1:]:
            if "__Null__" in game:
                continue

            print (f"{game[0]} vs {game[1]}")

        print()
