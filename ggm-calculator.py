import csv

# "Get Good Metric" #
# GGM = ((H+BB+IBB)/(AB+BB))-((SO+SF+SH+(2*GIDP))/AB)

# Attempts to calculate how "good" a batter actually is by rewarding plate discipline and "intimidation" (IBB) 
# and punishing what I believe are "bad" things, like strike outs, sacrifice flies, sacrifice hits, 
# and especially ground into double plays.

# uses data from Sean Lahman: http://www.seanlahman.com/
# note: This program only requires Batting.csv and People.csv

GGM_dictionary = {}
people_dictionary = {}

with open('People.csv') as people:
    read = csv.reader(people, delimiter=',')
    line_count = 0
    for row in read:
        if(line_count == 0):
            line_count += 1
        else:
            player_id = row[1]
            player_first_name = row[14]
            player_last_name = row[15]
            people_dictionary[player_id] = (player_first_name + ' ' + player_last_name)
            line_count += 1
    
with open('Batting.csv') as batting_stats:
    read = csv.reader(batting_stats, delimiter=',')
    line_count = 0
    previous_player_id = ''
    
    AB = 0
    H = 0
    BB = 0
    SO = 0
    GIDP = 0
    SH = 0
    SF = 0
    IBB = 0
    
    for row in read:
        if(line_count == 0):
            line_count += 1
        else:
            player_id = row[0]
            
            if(player_id == previous_player_id):
                try:
                    AB += int(row[7])
                except:
                    AB += 0
                try:
                    H += int(row[9])
                except:
                    H += 0
                try:
                    BB += int(row[16])
                except:
                    BB += 0
                try:
                    SO += int(row[17])
                except:
                    SO += 0
                try:
                    GIDP += int(row[22])
                except:
                    GIDP += 0
                try:
                    SH += int(row[20])
                except:
                    SH += 0
                try:
                    SF += int(row[21])
                except:
                    SF += 0
                try:
                    IBB += int(row[18])
                except:
                    IBB += 0
            else:
                if(AB != 0 and AB >= 100):
                    GGM = ((H+BB+IBB)/(AB+BB))-((SO+SF+SH+(2*GIDP))/AB)
                else:
                    GGM = 'Discard'
                
                if(GGM == 'Discard'):
                    pass
                else:
                    GGM_dictionary[previous_player_id] = GGM
                    
                previous_player_id = player_id
                
                try:
                    AB = int(row[7])
                except:
                    AB = 0
                try:
                    H = int(row[9])
                except:
                    H = 0
                try:
                    BB = int(row[16])
                except:
                    BB = 0
                try:
                    SO = int(row[17])
                except:
                    SO = 0
                try:
                    GIDP = int(row[22])
                except:
                    GIDP = 0
                try:
                    SH = int(row[20])
                except:
                    SH = 0
                try:
                    SF = int(row[21])
                except:
                    SF = 0
                try:
                    IBB = int(row[18])
                except:
                    IBB = 0
            
            line_count += 1

with open('data.csv', mode='w', newline='') as csv_file:
    fieldnames = ['Player Name', 'GGM']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    #writer.writeheader()
    for x in GGM_dictionary.keys():
        writer.writerow({'Player Name': people_dictionary[x], "GGM": GGM_dictionary[x]})
    