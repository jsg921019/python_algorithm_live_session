from copy import deepcopy

def remove_bingo(board):
    
    bingo_row = None
    for i in range(4):
        is_bingo = True
        for j in range(4):
            if board[i][j] == 0:
                is_bingo = False
                break
        if is_bingo:
            bingo_row = i
            
    bingo_col = None
    for j in range(4):
        is_bingo = True
        for i in range(4):
            if board[i][j] == 0:
                is_bingo = False
                break
        if is_bingo:
            bingo_col = j
            
    if bingo_row is not None:
        for j in range(4):
            board[bingo_row][j] = 0
            
    if bingo_col is not None:
        for i in range(4):
            board[i][bingo_col] = 0
            
    is_bingo = not (bingo_row is None and bingo_col is None)
    return board, is_bingo
    
    
def get_next_nodes(node):
    
    board, can_add = node
    
    next_nodes = []
    
    if can_add:
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    new_board = deepcopy(board)
                    new_board[i][j] = 1
                    new_board, is_bingo = remove_bingo(new_board)
                    if is_bingo:
                        next_nodes.append((new_board, False))
                    
    for i in range(4):
        for j in range(4):
            if board[i][j] == 1:
                for _i, _j in [(i+1, j), (i-1, j ), (i, j+1), (i, j-1)]:
                    if 0 <= _i < 4 and 0 <= _j < 4 and board[_i][_j] == 0:
                        new_board = deepcopy(board)
                        new_board[i][j] = 0
                        new_board[_i][_j] = 1
                        new_board, is_bingo = remove_bingo(new_board)
                        next_nodes.append((new_board, can_add))
    
    return next_nodes

def to_tuple(board):
    return tuple(board[0]) + tuple(board[1]) + tuple(board[2]) + tuple(board[3])

def solution(board):
    
    visited = set(to_tuple(board))
    step = 1
    curr_nodes = [(board, True)]
    
    while curr_nodes:
        next_nodes = []
        for node in curr_nodes:
            for next_node in get_next_nodes(node):
                next_board, next_can_add = next_node
                tuple_board = to_tuple(next_board)
                num_ones = sum(tuple_board)
                if num_ones == 0:
                    return step
                if tuple_board not in visited:
                    if next_can_add:
                        if num_ones % 4 != 1:
                            visited.add(tuple_board)
                            next_nodes.append(next_node)
                    else:
                        if num_ones % 4 == 0:
                            visited.add(tuple_board)
                            next_nodes.append(next_node)
        curr_nodes = next_nodes
        step += 1
        
    return -1