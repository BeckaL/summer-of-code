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
        if land[vcoord][hcoord] == 1:
            known_land.append((vcoord, hcoord))
            return 1

def land_to_test(current_square):
    for move in possible_movements:
        square_to_test = tuple(map(operator.add, current_square, move))
        if in_range(square_to_test):
            if square_to_test not in known_land and square_to_test not in known_sea and square_to_test not in land_to_be_tested:
                land_to_be_tested.add(square_to_test)

def movement(current_square):
    land_to_test(current_square)
    print("Land to be tested is:")
    print(land_to_be_tested)
    tested_squares = []
    for move in possible_movements:
        new_square = tuple(map(operator.add, current_square, move))
        tested_squares.append(new_square)
        print("Testing square:")
        print(new_square)
        if new_square not in known_land and land_test(int(new_square[0]), int(new_square[1])):
            print("Land! Moving to square")
            print(new_square)
            print("This is the land I currently know about:")
            print(known_land)
            print("Here are the squares I've tested:")
            print(tested_squares)
            cleaned_land = land_to_be_tested - set(known_land) - set(known_sea)
            if not cleaned_land:
                print("Done! This is the final set of land I know about:")
                print(known_land)
                print("This is the final set of sea I know about:")
                print(known_sea)
                finished = True
            else:
                finished = False
                return movement(new_square)
        elif new_square not in known_land and in_range(new_square):
            finished = False
            known_sea.add(new_square)
            print("nah-uh: sea. This is the sea I know about")
            print(known_sea)
    if not finished:
        for square in tested_squares:
            if square in known_land:
                print("Going back to a square I already know about:")
                print(square)
                cleaned_land = land_to_be_tested - set(known_land) - set(known_sea)
                if not cleaned_land:
                    print("Done! This is the final set of land I know about:")
                    print(known_land)
                    print("This is the final set of sea I know about:")
                    print(known_sea)
                else:
                    return movement(square)



movement(starting_coordinates)
# print(known_land)
