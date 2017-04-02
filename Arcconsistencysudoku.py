"""

ARC Consistency algorithm for solving Sudoku

"""

class Sudokuboard():
    
    def __init__(self,startstr):
        
        self.alpha='ABCDEFGHI'
        k=0
        self.sudoku={}        
        for i in self.alpha:
            for j in range(1,10):
                key=i+str(j)
                self.sudoku[key]=int(startstr[k])
                k+=1
         
        self.sudokudomain={}
        for i in self.alpha:
            for j in range(1,10):
                key=i+str(j)
                l1=[]
                for k in range(1,10):
                    checkkey=i+str(k)
                    if int(self.sudoku[checkkey]) is not 0:
                        l1+=[int(self.sudoku[checkkey])]   
                for k in self.alpha:
                    checkkey=k+str(j)
                    if int(self.sudoku[checkkey]) is not 0 and int(self.sudoku[checkkey]) not in l1:
                        l1+=[int(self.sudoku[checkkey])]
                
                tup=self.getbox(i,j)
                #print(tup)
                for a in tup[0]:
                    for b in tup[1]:
                        checkkey=a+str(b)
                        #print(checkkey)
                        if int(self.sudoku[checkkey]) is not 0 and int(self.sudoku[checkkey]) not in l1:
                            l1+=[int(self.sudoku[checkkey])]
                
                if self.sudoku[key]==0:
                    for num in range(1,10):
                        if num not in l1:
                            try:                        
                                self.sudokudomain[key]+=[num]
                            except KeyError:
                                self.sudokudomain[key]=[num]
                else:
                    self.sudokudomain[key]=[int(self.sudoku[key])]
        
    def getbox(self,i,ji):
        
        b1=''
        b2=[]

        alphaindex=self.alpha.index(i)
        
        k=alphaindex-alphaindex%3
        
        b1=self.alpha[k:k+3]
        
        if ji%3==0:
            temp=ji-2
        else:
            
            temp=ji-ji%3+1
        for k in range(temp,temp+3):
            b2.append(k)
        
        return (b1,b2)
        
def AC3(sudokuobject):
    
    (arcsqueue,neighbors)=buildarcs(sudokuobject)
    
    while len(arcsqueue)!=0:
        (key1,key2)=arcsqueue.pop()
        if Revise(sudokuobject,key1,key2):
            if len(sudokuobject.sudokudomain[key1])==0:
                return False
            for n in neighbors[key1]:
                arcsqueue.add((n,key1))
    return True
          
        
def buildarcs(sudokuobject):
    listofarcs=set()
    neighbors={}
    for i in 'ABCDEFGHI':
        for j in range(1,10):
            for ii in 'ABCDEFGHI':
                for jj in range(1,10):
                    if i==ii or j==jj or sudokuobject.getbox(i,int(j))==sudokuobject.getbox(ii,int(jj)):
                        if not (i==ii and j==jj):
                            key1=i+str(j)
                            key2=ii+str(jj)
                            try:
                                neighbors[key1]+=[key2]
                            except KeyError:
                                neighbors[key1]=[key2]
                            listofarcs.add((key1,key2))
    return (listofarcs,neighbors)
            
                

def Revise(sudokuobject,key1,key2):
    revised=False
    for i in sudokuobject.sudokudomain[key1]:
        if not checkconstraintforkey2(i,key1,key2,sudokuobject):
            sudokuobject.sudokudomain[key1].remove(i)
            revised=True
    return revised
    
def checkconstraintforkey2(i,key1,key2,sudokuobject):
    if key1[0]==key2[0] or key1[1]==key2[1] or sudokuobject.getbox(key1[0],int(key1[1]))==sudokuobject.getbox(key2[0],int(key2[1])):
        found=False
        for j in sudokuobject.sudokudomain[key2]:
            if i!=j:
                found=True
        return found
    else:
        return True
        

import sys


    

def main():
    
    #startstr=sys.argv[1]
    
#    with open('sudokus_start.txt') as f:
#        sudokustarts=f.readlines()
#        
#    for i in range(len(sudokustarts)):
#        print(sudokustarts[i])
    
    startstr='250007001000004050010020367000600000000081030080040706620100070009400008800006003'
    

    #print(startstr+'\n')
    #startstr=sudokustarts[i]
    board=Sudokuboard(startstr)
    
    alpha='ABCDEFGHI'
    k=0     
    #Isconstraintsatisfied(board)
    for i in alpha:
        for j in range(1,10):
            key=i+str(j)
            print(board.sudoku[key],end='  ')
            k+=1
        print('\n')
        
#    for i in alpha:
#        for j in range(1,10):
#            key=i+str(j)
#            print(board.sudokudomain[key],end='  ')
#            k+=1
#        print('\n')
        
    if AC3(board):
        print('Arc consistency achieved')
    else:
        print('inconsistent')
              
    fout=open('sudokus_finish.txt','w')
    solvable=True
    for i in alpha:
        for j in range(1,10):
            if len(board.sudokudomain[key])!=1 and solvable:
                solvable=False
            key=i+str(j)
            print(board.sudokudomain[key],end='  ')
            fout.write(str(board.sudokudomain[key][0]))
        print('\n')
        
    if solvable:
        print('solvable')
    else:
        print('didnt solve')
    
    fout.write('\n')
    
    fout.close()
    
        
if __name__ == "__main__":
    #print(sys.argv)
    main()