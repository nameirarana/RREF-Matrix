def MatrixChallenge(strArr):
# code goes here
    rows = strArr.count(">")
    try:
        cols = strArr.index("<>")
    except:
        cols = len(strArr)
    M = {}
    for i in range(0, rows):
        M[i] = 0
    for j in range(0, cols):
        M[i][j] = float(strArr.pop(0) )
    if (strArr): strArr.pop(0)

    for pivot in range(0, min(cols, rows)):
        rmax = pivot
        for i in range(pivot + 1, min(cols, rows)) :
            if abs (M[i][pivot]) > abs (M[rmax][pivot]):
                rmax=i
        if rmax != pivot:
            M[pivot], M[rmax] = M[rmax], M[pivot]

        for k in range(pivot, cols):
            if M[pivot][k]!= 0:
                break

        if M[pivot][k] == 0:
            break
        for j in range(cols - 1, k - 1, -1):
            M[pivot][i] /= M[pivot][k]

        for i in range (pivot + 1, rows):
            for j in range(cols - 1, pivot -1, -1):
                M[i][j] -= M[i][pivot] * M[pivot][i]

        for i in range(0, pivot) :
            for j in range(0, cols):
                M[i][j] -= M[pivot][i] * M[i][j]

    result = ''
    for i in range(0, rows) :
        result += ''.join([str(int (M[i][j])) for j in range (0, cols)])

    final_result = result.replace("O","")

    return final_result

print (MatrixChallenge (input ()))