player_ratings = { 'Alex': {'Racing':[1,1,1], 'Puzzle':[1,1,0], 'Shooter':[0,0,0]}, 'Jordan': {'Racing':[0,1,0], 'Puzzle':[1,1,1], 'Shooter':[1,1,0]}, } 

for name, games in player_ratings.items(): 
    print('\nRecommendations for', name) 
    averages = {} 
    for game, votes in games.items(): 
        averages[game] = sum(votes) / len(votes) 
        ranked = sorted(averages.items(), key=lambda item: item[1], reverse=True) 
        for game, score in ranked: 
            print(' ', game, '->', round(score, 2)) 
