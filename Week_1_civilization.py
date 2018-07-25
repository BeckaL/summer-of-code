import operator

land = [[0, 0, 0,0, 0],
        [0, 0, 1, 1, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]]
starting_coordinates = ((len(land)+1)/2-1, (len(land[0])+1)/2-1)
known_land = [starting_coordinates]
completed_moves = []
known_sea = set()
land_to_be_tested = set()

possible_movements = [(0,-1), (-1, -1), (-1, 0),(-1,1), (0, 1), (1, 1), (1, 0), (1, -1)]

def in_range(square):
    if -1< int(square[0]) < len(land) and -1 < int(square[1]) < len(land[0]):
        return 1

def land_test(vcoord, hcoord):
    if in_range((vcoord, hcoord)):
        if land[vcoord][hcoord]:
            known_land.append((vcoord, hcoord))
            return 1

def land_to_test(current_square):
    for move in possible_movements:
        square_to_test = tuple(map(operator.add, current_square, move))
        if in_range(square_to_test):
            if all([
                square_to_test not in known_land,
                square_to_test not in known_sea,
                square_to_test not in land_to_be_tested,
            ]):
                land_to_be_tested.add(square_to_test)

def movement(current_square):
    land_to_test(current_square)
    tested_squares = []
    for move in possible_movements:
        new_square = tuple(map(operator.add, current_square, move))
        tested_squares.append(new_square)
        if new_square not in known_land and land_test(int(new_square[0]), int(new_square[1])):
            cleaned_land = land_to_be_tested - set(known_land) - set(known_sea)
            if not cleaned_land:
                return known_land
                finished = True
            else:
                finished = False
                return movement(new_square)
        elif new_square not in known_land and in_range(new_square):
            finished = False
            known_sea.add(new_square)
    if not finished:
        for square in tested_squares:
            if square in known_land:
                cleaned_land = land_to_be_tested - set(known_land) - set(known_sea)
                if not cleaned_land:
                    return known_land
                else:
                    return movement(square)

print(movement(starting_coordinates))
