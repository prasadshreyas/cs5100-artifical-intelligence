import sys
from decimal import *

def read_line(file):	
	line=file.readline()
	line=line.rstrip()
	line=line.split(' ')
	return line

def print_grid(list,currentx,currenty):
	list[currentx].insert(currenty,'[')	
	list[currentx].insert(currenty+2,']')	
	for x in list:
		print ('  '.join(x)	)
		print ('\n')
	list[currentx].remove('[')	
	list[currentx].remove(']')	

def Update_current(a,x,y,n,m):	
	C={}
	if y!=0:
		C['L']=Decimal(a[x][y-1])	
	if x!=0:
		C['U']=Decimal(a[x-1][y])
	if x!=n-1:
		C['D']=Decimal(a[x+1][y])
	if y!=m-1:
		C['R']=Decimal(a[x][y+1])
	C['M']=Decimal(a[x][y])
	return C

def keyFromValue(C,m):			
	for k,v in C.items():
		if v==m:
			return k
	return 0

def keysFromValue(C,m):			
	L=[]					
	for k,v in C.items():	
		if v==m:
			L.append(k)
	L.sort()
	return L[0]

def Update_MEMORY(a,x,y,MEMORY):		
	if x!=0 and MEMORY[x-1][y]==-1:		
		MEMORY[x-1][y]=Decimal(a[x-1][y])
	if y!=0 and MEMORY[x][y-1]==-1:			
		MEMORY[x][y-1]=Decimal(a[x][y-1])
	if x!=n-1 and MEMORY[x+1][y]==-1:
		MEMORY[x+1][y]=Decimal(a[x+1][y])
	if y!=m-1 and MEMORY[x][y+1]==-1:
		MEMORY[x][y+1]=Decimal(a[x][y+1])
	if MEMORY[x][y]==-1:
		MEMORY[x][y]=Decimal(a[x][y])
	return MEMORY

def calc_move(x,y,mx,my):	
	if mx>x:
		return 'D'
	if mx<x:
		return 'U'
	if my>y:
		return 'R'
	if my<y:
		return 'L'

def calc_bestmove(x,y,n,m):	
	if x==0 or x==1:
		return 'D'
	if x==n or x==n-1:
		return 'U'
	if y==0 or y==1:
		return 'R'
	if y==m or y==m-1:
		return 'L'

fp=open(sys.argv[1],'r')
line=read_line(fp)
n=int(line[1])		
m=int(line[2])
line=fp.readline()
grid=[]			
P=Decimal('0.0')	
N=5			
for i in range(n):
	line=read_line(fp)
	grid.append(line)
line=read_line(fp)
max_moves=int(line[1])
line=read_line(fp)
x=int(line[1])-1	
y=int(line[2])-1
print_grid(grid,x,y)
CURRENT=Update_current(grid,x,y,n,m)	
MEMORY=[]
for i in range(n):		 
	MEMORY.append([])
	for j in range(m):
		MEMORY[i].append(-1)
index=1
while(index<=max_moves):
	MEMORY=Update_MEMORY(grid,x,y,MEMORY)
	maxm=0
	for i, itemx in enumerate(MEMORY):	
		for j,itemy in enumerate(itemx):
			if itemy>=maxm:
				maxm=itemy
				maxx,maxy=i,j
	moves_needed=abs(maxx-x)+abs(maxy-y)	
	
	if maxm > 0:	
		if moves_needed==0:	
			P=P+maxm
			print ('Suck\t'+str(P))
			grid[x][y]='0'
			MEMORY[x][y]=0
			move='S'
		elif moves_needed==1:	

			if CURRENT['M']<Decimal('0.25')*maxm:	
				if list(CURRENT.values()).count(maxm)==1:	
					move=keyFromValue(CURRENT,maxm)
				else :						
					move=keysFromValue(CURRENT,maxm)
			else:
				P=P+CURRENT['M']	
				print ('Suck\t'+str(P))
				grid[x][y]='0'
				MEMORY[x][y]=0	
				move='S'
		else:			
			current_max=max(CURRENT.values())
			if current_max > maxm*2/Decimal(str(moves_needed)):
				if CURRENT.values().count(maxm)==1:		
					move=keyFromValue(CURRENT,current_max)
				else :							
					move=keysFromValue(CURRENT,current_max)		
			else :
				move=calc_move(x,y,maxx,maxy)		
	else: 	
		move=calc_bestmove(x,y,n,m)	
	if move == 'L':
		print ('Left\t'+str(P))
		y=y-1
	elif move == 'R':
		print ('Right\t'+str(P))
		y=y+1
	elif move == 'U':
		print ('Up\t'+str(P))
		x=x-1
	elif move == 'D':
		print ('Down\t'+str(P))
		x=x+1
	CURRENT=Update_current(grid,x,y,n,m)		
	if index%N==0:	
		print_grid(grid,x,y)	
	index=index+1
print ('The total performance of the bot in '+str(max_moves)+' moves is : '+str(P))

