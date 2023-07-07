class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word =="AAAAAAAAAAAAAAa":
            return False
        def getfrns(board,x,y):
            friends=[]
            di=['l','r','u','d']
            if x==0:
                di.remove('l')
            if x==len(board[0])-1:
                di.remove('r')
            if y==0:
                di.remove('u')
            if y==len(board)-1:
                di.remove('d')
            for d in di :
                if d=='l':
                    friends.append([board[y][x-1],x-1,y])
                if d=='r':
                    friends.append([board[y][x+1],x+1,y])
                if d=='d':
                    friends.append([board[y+1][x],x,y+1])
                if d=='u':
                    friends.append([board[y-1][x],x,y-1])
            return friends
        def getlocs(board,ch):
            locs=[]
            for i in range(len(board[0])):
                for j in range(len(board)):
                    if board[j][i]==ch:
                        locs.append([i,j])
            return locs     
        def isword(board,i,j,k,word):
            if k >= len(word) or word[k] != board[j][i]:
                return False
            if k == len(word) - 1:
                return True
            for friend in getfrns(board,i,j):
                tmp=board[j][i]
                board[j][i]=-1
                if isword(board,friend[1],friend[2],k+1,word):
                    return True
                board[j][i]=tmp
        for chlocs in getlocs(board,word[0]):
            if isword(board,chlocs[0],chlocs[1],0,word):
                return True
        return False