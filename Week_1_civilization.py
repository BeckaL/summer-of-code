import operator

land = [[1, 0, 1],
        [1,1,1],
        [1,0,1]]
starting_coordinates = ((len(land)+1)/2-1, (len(land[0])+1)/2-1)
known_land = [starting_coordinates]
completed_moves = []
known_sea = []
land_to_be_tested = []

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
                land_to_be_tested.append(square_to_test)
#blooper comment
#
# def test_land_cleanup():
#     for square in land_to_be_tested:
#         if square in known_land or square in known_sea:
#             land_to_be_tested.remove(square)

def movement(current_square):
    land_to_test(current_square)
    print("Land to be tested is:")
    print(land_to_be_tested)
    if current_square != (2, 0):
        tested_squares = []
        for move in possible_movements:
            new_square = tuple(map(operator.add, current_square, move))
            tested_squares.append(new_square)
            print("Testing square:")
            print(new_square)
            if new_square not in known_land and land_test(int(new_square[0]), int(new_square[1])):
                land_to_be_tested.remove(new_square)
                print("Land! Moving to square")
                print(new_square)
                print("This is the land I currently know about:")
                print(known_land)
                print("Here are the squares I've tested:")
                print(tested_squares)
                return movement(new_square)
            else:
                known_sea.append(new_square)
                print("nah-uh: sea. This is the sea I know about")
                print(known_sea)
        for square in tested_squares:
            if square in known_land:
                print("Going back to a square I already know about:")
                print(square)
                return movement(square)
    else:
        print ("current square is (2,0) which is my terminal square. Breaking loop")
        print(current_square)
        print("This is the final set of land I know about")
        print(known_land)


movement(starting_coordinates)
# print(known_land)
