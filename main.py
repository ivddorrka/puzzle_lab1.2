
def number_row_check(lst):

    list_board = []
    for i in lst:
        list_board.append(list(i))
    
    for j in list_board:
        for _ in j:
            if _ != '*' and _ != ' ' and j.count(_) > 1:
                return False
    return True

# print(number_row_check(['**** ****', '***  ****', '**   ****', '*    ****', '         ', '        *', '       **', '      ***', '     ****']))

def rebuilding(lst):
    """
    This function rebuilds columns into new row
    >>> rebuilding(['**12*', '12345', '23456', '**23*'])
    [['*', '1', '2', '*'], ['*', '2', '3', '*'], ['1', '3', '4', '2'], ['2', '4', '5', '3'], ['*', '5', '6', '*']]
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
# print(rebuilding(['**** ****', '***1 ****', '**  3****', '* 4 1****', '     9 5 ', ' 6  83  *', '3   1  **', '  8  2***', '  2  ****']))

def column_check(lst):
    var1 = rebuilding(lst)
    var2 = number_row_check(var1)
    if var2 is True:
        return True
    return False
# print(column_check(['**** ****', '***1 ****', '**  3****', '* 4 1****', '     9 5 ', ' 6  83  *', '3   2  **', '  8  2***', '  2  ****']))

def squ_check(board):
    setted = [' ', '*', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in board:
        for j in list(i):
            if j not in setted:
                return False

    return True
        
# print(squ_check(['**** ****', '***1 ****', '**  3****', '* 4 1****', '     9 5 ', ' 6  83  *', '3   1  **', '  8  2***', '  2  ****']))

def block_reb(board):
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
# print(block_reb(['**** ****', '***1 ****', '**  3****', '* 4 1****', '    49 5 ', ' 6  83  *', '3   1  **', '  8  2***', '  2  ****']))

def block_check(lst):
    all_blocks = block_reb(lst)
    result = []
    for i in range(len(all_blocks)):
        var1 = ''.join(all_blocks[i][0][1:])
        var2 = ''.join(all_blocks[i][1])
        var3 = var1 + var2
        result.append(var3)

    # here_res = []
    # for j in result:
    #     if number_row_check(j) is True:
    #         here_res.append(j)
    
    if number_row_check(result) is True:
        return True
    return False
    # return result[0]
# print(block_check(['**** ****', '***1 ****', '**  3****', '* 4 1****', '    49 5 ', ' 6  83  *', '3   1  **', '  8  2***', '  2  ****']))

def validate_board(board):
    check_1 = number_row_check(board)
    check_2 = column_check(board)
    # check_3 = squ_check(board)
    check_4 = block_check(board)
    if check_1 is True and check_2 is True and check_4 is True:
        return True
    return False
    # return 
# print(validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "    49 5 ", " 6  83  *", "3   2  **", "  8  2***", "  2  ****"]))


print(validate_board(["****1****", "*** 2****", "**  3****", "*   4****", "    56781", "        *", "2      **", "      ***", "3 4  ****"]))