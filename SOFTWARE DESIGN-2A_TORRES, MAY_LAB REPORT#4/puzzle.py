def solves(S):
	return S == ['d','b','c']
def PuzzleSolver(k, S, U):
    for e in sorted(U).copy():
        S.append(e)
        U.remove(e)
        if k==1:
            print(S)
            if solves(S):
                print( f'Solution found: {S}')
        else:
            PuzzleSolver(k-1, S, U)
        U.add(S.pop())
PuzzleSolver(3, [], {'a','b','c','d'})
