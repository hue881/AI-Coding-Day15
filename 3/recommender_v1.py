ratings = { 'Racing': [1, 1, 0, 1, 1], 'Puzzle': [1, 0, 0, 1, 0], 'Shooter': [0, 0, 1, 0, 0], 'Sports': [1, 1, 1, 1, 1], } 

averages = {} 

for game, votes in ratings.items(): 
    score = sum(votes) / len(votes) 
    averages[game] = score 
    print('Average scores:') 

for game, score in averages.items(): 
    print(game, '->', round(score, 2)) best_game = max(averages, key=averages.get) 
    print('Recommended first:', best_game) 
