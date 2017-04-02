# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 08:20:17 2017

backtracking using the minimum remaining value heuristic

@author: vc185059
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
                    
                if len(self.sudokudomain[key])==1:
                    self.sudoku[key]=self.sudokudomain[key][0]
        
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


def Backtracking_search(sudokuobject):
    
    return Backtrack(sudokuobject)
    
def Backtrack(sudokuobject):
    
    if Isassignmentcomplete(sudokuobject):
        return 'success'
        
    keytoassign=findanunassignedvar(sudokuobject)
    
    for value in sudokuobject.sudokudomain[keytoassign]:
        
        if isvalueconsistent(value,keytoassign,sudokuobject):
            
            sudokuobject.sudoku[keytoassign]=value
            
            if not Forwardcheck(value,keytoassign,sudokuobject):
                sudokuobject.sudoku[keytoassign]=0
                continue
            
            result=Backtrack(sudokuobject)
            
            if result=='failure':
                sudokuobject.sudoku[keytoassign]=0
            else:
                sudokuobject.sudokudomain[keytoassign]=[value]
                return 'success'
                
    return 'failure'
        
def Isassignmentcomplete(sudokuobject):
    for i in sudokuobject.alpha:
            for j in range(1,10):
                key=i+str(j)
                if int(sudokuobject.sudoku[key])==0:# or len(sudokuobject.sudokudomain[key])>1:
                    return False
    return True
    
def findanunassignedvar(sudokuobject):
    finalkeywithmindomain=''
    for i in sudokuobject.alpha:
        for j in range(1,10):
            key=i+str(j)
            if int(sudokuobject.sudoku[key])==0 and len(sudokuobject.sudokudomain[key])>=1:
                if finalkeywithmindomain=='':
                    finalkeywithmindomain=key
                else:
                    if len(sudokuobject.sudokudomain[key])<len(sudokuobject.sudokudomain[finalkeywithmindomain]):
                        finalkeywithmindomain=key
    return finalkeywithmindomain
    
def isvalueconsistent(value,keytoassign,sudokuobject):
    for i in 'ABCDEFGHI':
        for j in range(1,10):
            if i==keytoassign[0] or j==int(keytoassign[1]) or sudokuobject.getbox(i,int(j))==sudokuobject.getbox(keytoassign[0],int(keytoassign[1])):
                if not (i==keytoassign[0] and j==int(keytoassign[1])):
                    key=i+str(j)
                    if value==sudokuobject.sudoku[key]:
                        return False
    return True

def Forwardcheck(value,keytoassign,sudokuobject):
    for i in 'ABCDEFGHI':
        for j in range(1,10):
            if i==keytoassign[0] or j==int(keytoassign[1]) or sudokuobject.getbox(i,int(j))==sudokuobject.getbox(keytoassign[0],int(keytoassign[1])):
                if not (i==keytoassign[0] and j==int(keytoassign[1])):
                    key=i+str(j)
                    if sudokuobject.sudoku[key]==0 and len(sudokuobject.sudokudomain[key])==1 and sudokuobject.sudokudomain[key][0]==value:
                        return False
    return True
    
import sys

def main():
    
    startstr=sys.argv[1]
    
#    with open('sudokus_start.txt') as f:
#        sudokustarts=f.readlines()
#        
#    for i in range(len(sudokustarts)):
#        print(sudokustarts[i])
    
    #startstr='250007001000004050010020367000600000000081030080040706620100070009400008800006003'
    

    #print(startstr+'\n')
    #startstr=sudokustarts[i]
    board=Sudokuboard(startstr)
    
    alpha='ABCDEFGHI'
    k=0     
    #Isconstraintsatisfied(board)
#    for i in alpha:
#        for j in range(1,10):
#            key=i+str(j)
#            print(board.sudoku[key],end='  ')
#            k+=1
#        print('\n')
        
#    for i in alpha:
#        for j in range(1,10):
#            key=i+str(j)
#            print(board.sudokudomain[key],end='  ')
#            k+=1
#        print('\n')
        
    if Backtracking_search(board)=='success':
        print('Found solution')
    else:
        print('no solution')
              
    fout=open('sudokus_finish.txt','w')
    solvable=True
    for i in alpha:
        for j in range(1,10):
            key=i+str(j)
            if len(board.sudokudomain[key])!=1 and solvable:
                solvable=False
                break
            #key=i+str(j)
            #print(board.sudokudomain[key],end='  ')
            #fout.write(str(board.sudokudomain[key][0]))
        #print('\n')
        
#    for i in alpha:
#        for j in range(1,10):
#            key=i+str(j)
#            print(board.sudoku[key],end='  ')
#            k+=1
#        print('\n')
    
    if solvable:
        print('solvable')
        for i in alpha:
            for j in range(1,10):
                key=i+str(j)
                #print(board.sudokudomain[key],end='  ')
                fout.write(str(board.sudoku[key]))
    else:
        print('didnt solve')
    
    fout.write('\n')
    
    fout.close()
    
        
if __name__ == "__main__":
    #print(sys.argv)
    main()