player_ratings = { 'Alex': {'Racing':[1,1,1], 'Puzzle':[1,1,0], 'Shooter':[0,0,0]}, 'Jordan': {'Racing':[0,1,0], 'Puzzle':[1,1,1], 'Shooter':[1,1,0]}, } 

for name, games in player_ratings.items(): 
	print('\nFor', name) 
	for game, votes in games.items(): 
		score = sum(votes) / len(votes) 
		print(' ', game, '->', round(score, 2)) 
