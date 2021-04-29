import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
chess_board =  [list(input().rstrip()) for _ in range(n)]
change_num = None
for i in range(m-7):
    for j in range(n-7):
        cnt1, cnt2 = 0,0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 ==0:
                    if chess_board[l][k] == 'W': cnt1 += 1
                    if chess_board[l][k] == 'B': cnt2 += 1
                else:
                    if chess_board[l][k] == 'B' : cnt1 += 1
                    if chess_board[l][k] == 'W' : cnt2 += 1
        new_result = min(cnt1, cnt2)
        if change_num is None:
            change_num = new_result
        else:
            change_num =  new_result if change_num > new_result else change_num
print(change_num)
