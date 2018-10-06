def lcsubstring(X, Y, m, n):
    LCSuff = [[None]*m+1 for i in n+1]
    # To store length of the longest common substring
    len = 0
    # To store the index of the cell which contains the
    # maximum value. This cell's index helps in building
    # up the longest common substring from right to left.
    row = col = 0
    # TIME COMPLEXITY : O(m*n)
    for i in range(m+1):
        for j in range(n+1):
            # base case
            if i == 0 or j == 0:
                LCSuff[i][j] = 0
            else if X[i-1] == Y[j-1]:
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                if len < LCSuff[i][j]:
                    len = LCSuff[i][j]
                    row = i 
                    col = j
            else:
                LCSuff[i][j] = 0

    # Print the substring
    while LCSuff[row][col] != 0:
        result += X[row - 1]
        row-=1
        col-=1
