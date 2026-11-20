def solve_n_queens(n):
    solutions=[]; cols=set(); diag1=set(); diag2=set(); board=[-1]*n
    def backtrack(r):
        if r==n: solutions.append(board[:]); return
        for c in range(n):
            if c in cols or r-c in diag1 or r+c in diag2: continue
            board[r]=c; cols.add(c); diag1.add(r-c); diag2.add(r+c)
            backtrack(r+1)
            cols.remove(c); diag1.remove(r-c); diag2.remove(r+c); board[r]=-1
    backtrack(0)
    return solutions

if __name__ == "__main__":
    print(solve_n_queens(4))
