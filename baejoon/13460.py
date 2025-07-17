from collections import deque

n, m = map(int, input().split()) # n : 세로, m : 가로

board = []
for r in range(n):
    row = input()
    ro = []
    for c in range(m):
        ro.append(row[c]) 
        if row[c] == 'R': red = (r,c)
        if row[c] == 'B': blue = (r,c)
        if row[c] == 'O': hole = (r,c)
    board.append(ro)

red_r,red_c = red
blue_r, blue_c = blue



def move(board, d):
    global done
    done = 0
    
    def _updown(dr):
        while board[red_r][red_c] != '#':
            board[red_r][red_c] ='.'
            red_r = red_r + dr
            if board[red_r][red_c] == 'O':
                done = 1
            board[red_r][red_c] ='R'
        
        
        while board[blue_r][blue_c] != '#':
            board[blue_r][blue_c] ='.'
            blue_r = red_r + dr
            if board[blue_r][blue_c] == "O":
               done = -1
            board[blue_r][blue_c] ='B'
    
    def _leftright(dc):
        while board[red_r][red_c] != '#':
            board[red_r][red_c] ='.'
            red_c = red_c + dc
            if board[red_r][red_c] == 'O':
                done = 1
            board[red_r][red_c] ='R'
        
        
        while board[blue_r][blue_c] != '#':
            board[blue_r][blue_c] ='.'
            blue_c = red_c + dc
            if board[blue_r][blue_c] == "O":
               done = -1
            board[blue_r][blue_c] ='B'

    if d == 1:
        dr = 1
        _updown(dr)
    elif d == 2:
        dr = -1
        _updown(dr)
    elif d == 3:
        dc = 1
        _leftright(dc)
    else:
        dc = -1
        _leftright(dc)
    
    return board
        
queue = deque()
queue.append((board, []))
end = set()
state, action = queue.popleft()


while queue < 10:
    for i in range(1,5):
        action.append(i)
        if action not in end:
            b = move(state, i)
            queue.append((b,action))
            if done == 1:
                print(len(action))
            if done == -1:
                end.append(action)