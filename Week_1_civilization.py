import operator

land = [[1, 0, 1],
        [1,1,1],
        [1,0,1]]
starting_coordinates = ((len(land)+1)/2-1, (len(land[0])+1)/2-1)
known_land = [starting_coordinates]
completed_moves = []


def land_test(vcoord, hcoord):
    if -1 < vcoord < len(land) and -1 < hcoord < len(land[0]):
        if land[vcoord][hcoord] == 1:
            known_land.append((vcoord, hcoord))
            return 1

coords = (0,0)


possible_movements = [(0,-1), (-1, -1), (-1, 0),(-1,1), (0, 1), (1, 1), (1, 0), (1, -1)]

def movement(current_square):
    if current_square != (2, 0):
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
                return movement(new_square)
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
