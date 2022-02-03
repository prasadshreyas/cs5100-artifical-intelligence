import sys
from decimal import *
import random

def read_line(file):		
	line=file.readline()
	line=line.rstrip()
	line=line.split(' ')
	return line

def print_grid(list,currentx,currenty):	
	list[currentx].insert(currenty,'[')
	list[currentx].insert(currenty+2,']')	
	for x in list:
		print('  '.join(x))
		print('\n')
	list[currentx].remove('[')		
	list[currentx].remove(']')	

def Update_current(a,x,y,n,m):		
	C={}
	if x!=0:
		C['U']=Decimal(a[x-1][y])
	if y!=0:
		C['L']=Decimal(a[x][y-1])
	if x!=n-1:
		C['D']=Decimal(a[x+1][y])
	if y!=m-1:
		C['R']=Decimal(a[x][y+1])
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
	return L


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
index=1
while(index<=max_moves):
	value=Decimal(grid[x][y])
	if value>0 :
		P=P+value
		print('Suck\t'+str(P))
		grid[x][y]='0'
	else :
		maxm=max(CURRENT.values())	
		if list(CURRENT.values()).count(maxm)==1:	
			move=keyFromValue(CURRENT,maxm)
		else :
			move=random.choice(keysFromValue(CURRENT,maxm))	
		if move == 'L':
			print('Left\t'+str(P))
			y=y-1
		elif move == 'R':
			print('Right\t'+str(P))
			y=y+1
		elif move == 'U':
			print('Up\t'+str(P))
			x=x-1
		elif move == 'D':
			print('Down\t'+str(P))
			x=x+1
		CURRENT=Update_current(grid,x,y,n,m)	
	if index%N==0:	
		print_grid(grid,x,y)	
	index=index+1
print('The total performance of the bot in '+str(max_moves)+' moves is : '+str(P))

