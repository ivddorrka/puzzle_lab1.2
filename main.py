def validate_board(board):
    pass

def number_row_check(lst):

    list_board = []
    for i in lst:
        list_board.append(list(i))
    
    for j in list_board:
        for _ in j:
            if _ != '*' and _ != ' ' and j.count(_) > 1:
                return False
            if _ != '*' and _ != ' ' and j.count(_) < 2:
                return True

# print(number_row_check(['**** ****', '***1 ****', '**  3****', '* 4 1****', '     9 5 ', ' 6  83  *', '3   1  **', '  8  2***', '  2  ****']))

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
    if var1 is True and var2 is True:
        return True
    else:
        return False
# print(column_check(['**** ****', '***1 ****', '**  3****', '* 4 1****', '     9 5 ', ' 6  83  *', '3   1  **', '  8  2***', '  2  ****']))

def squ_check(board):
    setted = [' ', '*', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in board:
        for j in list(i):
            if j not in setted:
                return False
            else:
                return True
        
print(squ_check(['**** ****', '***1 ****', '**  3****', '* 4 1****', '     9 5 ', ' 6  83  *', '3   1  **', '  8  2***', '  2  ****']))