def edit_distance(source,target):
    N = len(source)
    M = len(target)
    D = [[0 for j in range(M+1) ] for i in range(N+1)]
    P = [['' for j in range(M+1) ] for i in range(N+1)]
    path = []
    ins = 1
    dele= 1
    operations = {'↖':'sub','↑':'del','←':'ins','':''}
    for i in range(N+1):
        D[i][0] = i
    for j in range(M+1):
        D[0][j] = j
    for i in range(N):
        for j in range(M):
            sub = 0 if source[i]==target[j] else 1
            DP = [D[i][j] + sub , D[i][j+1] + dele,D[i+1][j] + ins]
            minimum = min(DP)
            D[i+1][j+1] = minimum
            idx = DP.index(minimum)
            if idx == 0 :
                P[i+1][j+1] = '↖'
            elif idx == 1:
                P[i+1][j+1] = '↑'
            else:
                P[i+1][j+1] = '←'
    i, j = N, M
    while i > 0 or j > 0:
        if P[i][j] == '↖':
            if source[i - 1] == target[j - 1]:
                path.append(f"MATCH({source[i - 1]})")
            else:
                path.append(f"SUB({source[i - 1]}->{target[j - 1]})")
            i -= 1
            j -= 1
        elif P[i][j] == '↑':
            path.append(f"DEL({source[i - 1]})")
            i -= 1
        elif P[i][j] == '←':
            path.append(f"INS({target[j - 1]})")
            j -= 1

    path.reverse()   

    return D[N][M],path 


print(edit_distance('leda','deal'))
        
