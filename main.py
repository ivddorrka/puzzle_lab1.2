"""
Puzzle.py checks whether the given field is ready to play with
github repository:
https://github.com/ivddorrka/puzzle_lab1.2.git
"""
def number_row_check(lst):
    """
    Function to check all rows for correct numbers
    >>> number_row_check(['***', ' * 1', '123', '111'])
    False
    """
    list_board = []
    for i in lst:
        list_board.append(list(i))
    
    for j in list_board:
        for _ in j:
            if _ != '*' and _ != ' ' and j.count(_) > 1:
                return False
    return True
# print(number_row_check(['***', ' * 1', '123', '111']))

def rebuilding(lst):
    """
    This function rebuilds columns into new row
    >>> rebuilding(['111', '234', '123'])
    [['1', '2', '1'], ['1', '3', '2'], ['1', '4', '3']]
    """
    prom_res = []
    for i in lst:
        prom_res.append(list(i))

    result = []
    for _ in range(len(prom_res[0])):
        prom_here =[]
        for j in range(len(prom_res)):
            var = prom_res[j][_]
            prom_here.append(var)
        result.append(prom_here)

    return result
# print(rebuilding(['111', '234', '123']))

def column_check(lst):
    """
    Function check's whether columns have right numbers, according to the given rows
    >>> column_check(['***', ' * 1', '123', '111'])
    False
    """
    var1 = rebuilding(lst)
    var2 = number_row_check(var1)
    if var2 is True:
        return True
    return False
# print(column_check(['***', ' * 1', '123', '111']))

def block_reb(board):
    """
    Function to make list of tuples with needed blocks
    >>> block_reb(['***', ' * 1', '123', '111'])
    [(['1', '1', '1'], ['1', '1', ' ', '*']), (['2', '3'], ['2', '*', '*']), ([' '], [' ', '*'])]
    """
    columns = rebuilding(board)
    norma = rebuilding(columns) # to make it a list of lists
    res = []
    for i in range(len(columns)):
        prom = []
        for j in range(len(columns[i])):
            a = columns[i][::-1][j:]
            b = norma[::-1][i][j:]
            tuplik = b, a
            prom.append(tuplik)
        res.append(prom)
    result = []
    # for t in range(len(res[0])):
    # t = 0
    for _ in range(len(res)):
        # t += 1
        result.append(res[_][_])
    
    return result

def block_check(lst):
    """
    >>> block_check(['***', ' * 1', '123', '111'])
    False
    """
    all_blocks = block_reb(lst)
    result = []
    for i in range(len(all_blocks)):
        var1 = ''.join(all_blocks[i][0][1:])
        var2 = ''.join(all_blocks[i][1])
        var3 = var1 + var2
        result.append(var3)

    if number_row_check(result) is True:
        return True
    return False
# print(block_check(['***', ' * 1', '123', '111']))

def validate_board(board):
    """
    Main function which checks whether field is correct
    >>> validate_board(['***', ' * 1', '123', '111'])
    False
    """
    check_1 = number_row_check(board)
    check_2 = column_check(board)
    check_4 = block_check(board)
    if check_1 is True and check_2 is True and check_4 is True:
        return True
    return False
# print(validate_board(['***', ' * 1', '123', '111']))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
