import operator

land = [[1, 0, 1],
        [1,1,1],
        [1,0,1]]
starting_coordinates = ((len(land)+1)/2-1, (len(land[0])+1)/2-1)
known_land = [starting_coordinates]
completed_moves = []


def land_test(hcoord, vcoord):
    if land[hcoord][vcoord] == 1:
        known_land.append((hcoord, vcoord))
        return 1

coords = (0,0)


possible_movements = [(0,-1), (-1, -1), (-1, 0),(-1,1), (0, 1), (1, 1), (1, 0), (1, -1)]

def movement(current_square):
    for move in possible_movements:
        new_square = tuple(map(operator.add, starting_coordinates, move))
        if new_square not in known_land and land_test(int(new_square[0]), int(new_square[1])) and current_square+move not in completed_moves:
            completed_moves.append(starting_coordinates + move)
            return movement(new_square)
#fake comment
movement(starting_coordinates)
print(known_land)
