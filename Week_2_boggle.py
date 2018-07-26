import random
import pprint
import operator
import itertools

dice = ['AAEEGN',
        'ELRTTY',
        'AOOTTW',
        'ABBJOO',
        'EHRTVW',
        'CIMOTU',
        'DISTTY',
        'EIOSST',
        'DELRVY',
        'ACHOPS',
        'HIMNQU',
        'EEINSU',
        'EEGHNW',
        'AFFKPS',
        'HLNNRZ',
        'DEILRX',
        ]

def dice_roll():
    letters = []
    for di in dice:
        letters.append(di[random.randint(0,5)])
    random.shuffle(letters)
    print(letters)

    grid = []
    for _ in range(4):
        row = []
        for _ in range(4):
            row.append(letters.pop())
        grid.append(row)
    print(grid)

# dice_roll()

static_letters = ['S', 'Q', 'W', 'R', 'R', 'C', 'O', 'O', 'T', 'H', 'I', 'N', 'R', 'S', 'N', 'E']
static_grid = [['E', 'N', 'S', 'R'], ['N', 'I', 'H', 'T'], ['O', 'O', 'C', 'R'], ['R', 'W', 'Q', 'S']]

'opens dictionary and puts each word into words list'
with open("dictionary.txt", "r") as f:
    s = f.read()
words = s.splitlines()

'filters dictionary by all possible words given letter counts'
def find_possible_words():
    possible_words = []
    for word in words:
        truth_tester = 1
        for letter in word:
            truth_tester = word.count(letter) <= static_letters.count(letter) * truth_tester
        if truth_tester == 1:
            possible_words.append(word)
    print(possible_words)
    print(len(possible_words))


static_possible_words = ['CESS', 'CHESS', 'CHESTS', 'CHEW', 'CHI', 'CHIT', 'CHOOSES', 'CHOOSIEST', 'CISTS', 'CITE', 'COHO', 'COHOSTS', 'CONNOTE', 'COO', 'COOT', 'COOTIE', 'ECHT', 'EH', 'ESS', 'ET', 'ETCH', 'ETH', 'ETHIC', 'ETIC', 'HE', 'HEISTS', 'HESTS', 'HET', 'HEW', 'HI', 'HIC', 'HIE', 'HISS', 'HISTS', 'HIT', 'HOOT', 'HORROR', 'ICE', 'ICH', 'INCENT', 'INN', 'IONONE', 'IT', 'ITCH', 'NEOCON', 'NINE', 'NINTH', 'NOON', 'NOTION', 'OHO', 'ONION', 'OOH', 'OOT', 'QI', 'SCHIST', 'SCOOTS', 'SECS', 'SECTS', 'SEIS', 'SENNITS', 'SETS', 'SEWS', 'SHES', 'SHEWS', 'SHIES', 'SHIEST', 'SHIST', 'SHITS', 'SHOOS', 'SHOOTS', 'SICES', 'SICS', 'SIS', 'SITES', 'SITS', 'SOOTHES', 'SOOTHS', 'SOOTS', 'SORROWERS', 'STEWS', 'STICHS', 'STIES', 'STIRRERS', 'SWISH', 'SWITCHES', 'SWOOSH', 'TECH', 'TEW', 'THE', 'THESIS', 'THEW', 'THINNESS', 'TI', 'TIC', 'TIE', 'TOO', 'TWICE', 'WE', 'WECHT', 'WESTS', 'WET', 'WHET', 'WHISTS', 'WHIT', 'WHITE', 'WHOOSIS', 'WICH', 'WISES', 'WISEST', 'WISHES', 'WISS', 'WISTS', 'WIT', 'WITCH', 'WITE', 'WITH', 'WITHE', 'WONTON', 'WOO', 'WOOSHES']

'gets coords for a word in list of letters'
raw_coords_path = []
test_word = 'COOS'
for letter in test_word:
    raw_coords = []
    locations = [i for i, x in enumerate(static_letters) if x == letter]
    for location in locations:
        raw_coords.append(location)
    raw_coords_path.append(raw_coords)
# print(raw_coords_path)

'gets all paths for a word (will be multiple paths if letter appears more than once'
all_paths = list(itertools.product(*raw_coords_path))
print(all_paths)
for path in all_paths:
    if len(set(path)) != len(path):
        all_paths.remove(path)
print(all_paths)


possible_movements = [(0,-1), (-1, -1), (-1, 0),(-1,1), (0, 1), (1, 1), (1, 0), (1, -1)]

'generates coords in 4*4 grid given number in list'
def generate_coordinates(location):
    coords = (location/4, location % 4)
    return coords

'checks if all moves legal'
def check_for_legal_moves(all_paths):
    any_path_checker = 0
    for num_path in range(len(all_paths)):
        path = []
        one_path_checker = 1
        for num_letter in range(len(all_paths[0])-1):
            path.append(all_paths[num_path][num_letter])
            coord1 = generate_coordinates(all_paths[num_path][num_letter])
            coord2 = generate_coordinates(all_paths[num_path][num_letter+1])
            movement = tuple(map(operator.sub, coord1, coord2))
            one_path_checker = one_path_checker * movement in possible_movements
        any_path_checker += one_path_checker
    return any_path_checker > 0


print(check_for_legal_moves(all_paths))
# truth_checker = 1
# for num_paths in range(len(all_paths)):
#     for num_letters in range(len(all_paths[0])-1):
#         coord1 = generate_coordinates(raw_coords_path[num_paths][num_letters])
#         coord2 = generate_coordinates(raw_coords_path[num_paths][num_letters])
#         movement = tuple(map(operator.sub, coord1, coord2))
#         truth_checker = truth_checker * movement in possible_movements
#     print(truth_checker)
