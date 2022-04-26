for _ in xrange(input()):
    n, m = map(int, raw_input().split())
    board = []
    rev_board = []
    for x in xrange(n):
        board.append(raw_input())
    for i in xrange(m):
        rev_board.append("".join([x[i] for x in board]))
    for i in xrange(m):
        work_on = rev_board[i]
        prev_row = 0;
        while work_on != prev_row:
            prev_row = work_on
            work_on = work_on.replace("*.", ".*")
        rev_board[i] = prev_row
    ans_board = []
    for i in xrange(n):
        ans_board.append("".join([x[i] for x in rev_board]))
    for b in ans_board:
        print (b)