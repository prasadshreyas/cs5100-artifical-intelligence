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

fp=open(sys.argv[1],'r')
line=read_line(fp)
n=int(line[1])			
m=int(line[2])
line=fp.readline()
grid=[]			
Moves=['L','R','U','D']
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

index=1
while(index<=max_moves):
	if Decimal(grid[x][y])>0 :
		P=P+Decimal(grid[x][y])
		print('Suck\t'+str(P))
		grid[x][y]='0'
	else :
		if x==n-1:			
			Moves.remove('D')
		if x==0:
			Moves.remove('U')
		if y==m-1:
			Moves.remove('R')
		if y==0:
			Moves.remove('L')
		move=random.choice(Moves)
		if move == 'L':
			print('Left\t'+str(P))
			y=y-1
		if move == 'R':
			print('Right\t'+str(P))
			y=y+1
		if move == 'U':
			print('Up\t'+str(P))
			x=x-1
		if move == 'D':
			print('Down\t'+str(P))
			x=x+1
	Moves=['L','R','U','D']
	if index%N==0:	
		print_grid(grid,x,y)	
	index=index+1
print('The total performance of the bot in '+str(max_moves)+' moves is : ' + str(P))



