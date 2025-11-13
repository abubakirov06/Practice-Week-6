def sort_leaderboard(leaderboard):
    copy_of_leaderboard = []
    new_order = []
    for element in leaderboard:
        copy_of_leaderboard.append((element[1], element[0]))
    copy_of_leaderboard.sort()
    copy_of_leaderboard.reverse()
    for _ in range(len(leaderboard)):
        for i in range(1, len(copy_of_leaderboard)):
          if copy_of_leaderboard[i-1][0] == copy_of_leaderboard[i][0]:
                new_order.append(copy_of_leaderboard[i-1])
                new_order.append(copy_of_leaderboard[i])
                new_order.sort()
                copy_of_leaderboard[i-1] = new_order[0]
                copy_of_leaderboard[i] = new_order[1]
                new_order = []
    for element in copy_of_leaderboard:
        new_order.append((element[1], element[0])) 
    return new_order

leaderboard = [
    ('Alice', 88),
	('Bob', 92),
	('Charlie', 92),
	('David', 85)
]

print(sort_leaderboard(leaderboard))