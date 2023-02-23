"""
Introduction to Programming: Coursework 1
@author: Isaac Ng Wen Shen
"""
# Reminder: You are not allowed to import any modules.

def wordsearch(puzzle: list, wordlist: list) -> None:
    final_list = []
    if valid_puzzle(puzzle) and valid_wordlist(wordlist): # Check if both valid
        for word in wordlist: # Looping through the list
            temp = get_positions(puzzle, word.upper()) # Convert all to upper
            if temp is not None: # Make sure its not empty
                final_list.append(temp)
        coloured_display(puzzle, final_list)
    else:
        print("ValueError, invalid puzzle or wordlist")
        
        
def valid_puzzle(puzzle: list) -> bool:
    temp = len(puzzle[0]) # Storing Length
    for value in puzzle:
        if len(value) != temp: # Comparing if each value is the same length
            return False
    return True
    
        
def valid_wordlist(wordlist: list) -> bool:
    return all(isinstance(value, str) for value in wordlist)
   
       
def get_positions(puzzle: list, word: str) -> list:
    def checker(word_position) -> bool: # Make sure searches dont go outisde of the grid
        for i, value in enumerate(word_position):
            for j in range(2):
                if word_position[i][j] == -1:
                    return False
        return True
    
    def horizontal_finder(current_pos) -> list:
        word_position = [current_pos]
        for i in range(1, length_of_word):
            if (puzzle[current_pos[0]][current_pos[1] + i]) != word.upper()[i]: # Checking Right
                break
            word_position.append(tuple([int(current_pos[0]), int(current_pos[1]) + i]))
            if len(word_position) == length_of_word: # Check if the size of list is = length
                word_position[0] = tuple(current_pos) # Converting List to wanted Tuple
                return word_position
    
        word_position = [current_pos]
        for i in range(1, length_of_word):
            if (puzzle[current_pos[0]][current_pos[1] - i]) != word.upper()[i]: # Checking Left
                break
            word_position.append(tuple([int(current_pos[0]), int(current_pos[1]) - i]))
            if len(word_position) == length_of_word:
                word_position[0] = tuple(current_pos)
                return word_position
        word_position = []
        return word_position
  
    def vertical_finder(current_pos) -> list:
        word_position = [current_pos]
        for i in range(1, length_of_word):
            if (puzzle[current_pos[0] - i][current_pos[1]]) != word.upper()[i]: # Checking Up
                break
            word_position.append(tuple([int(current_pos[0] - i), int(current_pos[1])]))
            if len(word_position) == length_of_word:
                word_position[0] = tuple(current_pos)
                return word_position
    
        word_position = [current_pos]
        for i in range(1, length_of_word):
            if (puzzle[current_pos[0] + i][current_pos[1]]) != word.upper()[i]: # Checking Down
                break
            word_position.append(tuple([int(current_pos[0] + i), int(current_pos[1])]))
            if len(word_position) == length_of_word:
                word_position[0] = tuple(current_pos)
                return word_position
        word_position = []
        return word_position
  
    def diagonal_finder_right(current_pos) -> list: # To check Diganoally right
        word_position = [current_pos]
        for i in range(1, length_of_word):
            if (puzzle[current_pos[0] - i][current_pos[1] + i]) != word.upper()[i]: # Checking up right
                break
            word_position.append(tuple([int(current_pos[0] - i), int(current_pos[1] + i)]))
        if len(word_position) == length_of_word:
            word_position[0] = tuple(current_pos)
            return word_position
        
        word_position = [current_pos]
        for i in range(1, length_of_word):
            if (puzzle[current_pos[0] + i][current_pos[1] - i]) != word.upper()[i]: # Checking down left
                break
            word_position.append(tuple([int(current_pos[0] + i), int(current_pos[1] - i)]))
        if len(word_position) == length_of_word:
            word_position[0] = tuple(current_pos)
            return word_position
        word_position = []
        return word_position
  
    def diagonal_finder_left(current_pos) -> list: # To check Diganoally left
        word_position = [current_pos]
        for i in range(1, length_of_word):
            if (puzzle[current_pos[0] - i][current_pos[1] - i]) != word.upper()[i]: # Checking up left
                break
            word_position.append(tuple([int(current_pos[0] - i), int(current_pos[1] - i)]))
        if len(word_position) == length_of_word:
            word_position[0] = tuple(current_pos)
            return word_position

        word_position = [current_pos]
        for i in range(1, length_of_word):
            if (puzzle[current_pos[0] + i][current_pos[1] + i]) != word.upper()[i]: # Checking down right
                break
            word_position.append(tuple([int(current_pos[0] + i), int(current_pos[1] +i)]))
        if len(word_position) == length_of_word:
            word_position[0] = tuple(current_pos)
            return word_position
        word_position = []
        return word_position
    
    # Getting Puzzle index size & word length
    height_of_board = len(puzzle)
    width_of_board = len(puzzle[0])
    length_of_word = len(word)
    word_position = []
    final_word_positions = []

    for row in range(height_of_board): # Loop through puzzle for rows
        for column in range(width_of_board): # Loop through puzzle for column
            if puzzle[row][column] == word[0]: # Checking for for matchin 1st char
                current_pos = [row, column]
                try: # Try Block to catch out of index error
                    word_position = horizontal_finder(current_pos)
                    if len(word_position) != 0:
                        if checker(word_position):
                            final_word_positions.append(word_position)
                            continue
                except IndexError: # Catching any IndexError so it dont go out of bounds
                    pass
                try:
                    word_position = vertical_finder(current_pos)
                    if len(word_position) != 0:
                        if checker(word_position):
                            final_word_positions.append(word_position)
                            continue
                except IndexError:
                    pass
                try:
                    word_position = diagonal_finder_right(current_pos)
                    if len(word_position) != 0:
                        if checker(word_position):
                            final_word_positions.append(word_position)
                            continue
                except IndexError:
                    pass
                try:
                    word_position = diagonal_finder_left(current_pos)
                    if len(word_position) != 0:
                        if checker(word_position):
                            final_word_positions.append(word_position)
                            continue
                    else:
                        continue
                except IndexError:
                    continue
        
    if len(final_word_positions) != 0: # To check there was a match found
        return final_word_positions
    return print(f"{word} not found")
 
 
def basic_display(grid: list) -> None:
    str_value = "" # Initialising String line
    for value in grid:
        for letter in value:
            # Concatenating strings & whitespaces
            str_value = str_value + " " + letter + " "
        print(str_value)
        str_value = ""
    
        
def coloured_display(grid: list, positions: list) -> None:
    place = [] # To store all the position in a list
    for i in positions:
        for j in i:
            for k in j:
                k = list(k) # Converting tuple position
                place.append(k)
    
    for i, value in enumerate(grid):
        newline = ""
        for char in range(len(value)):
            if char == 10:
                newline = "\n"
            pos = [i, char]
            if pos not in place: # Checking if the position is in the position list
                print(f" {grid[i][char]} ", end=newline)
            else:
                print(f"\033[42m {grid[i][char]} \033[0m", end=newline) # Color Char
    
                
# =============================================================================
# Do not remove the followings. To test your functions
# =============================================================================


def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print("puzzle is", valid_puzzle(good_puzzle))
    print("puzzle is", valid_puzzle(bad_puzzle1))
    print("puzzle is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    basic_display(puzzle1)
    basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    get_positions(puzzle1, "TESTING")
    print(get_positions(puzzle1, "LVA"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    final_list = []
    for word in good_wordlist2:
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    coloured_display(puzzle1, final_list)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # uncomment the test function individually
    # basic solution
    # test_valid_puzzle()
    # test_valid_wordlist()
    # test_basic_display()

    # full solution
    # test_coloured_display()
    # test_get_positions()
    test_wordsearch()
    