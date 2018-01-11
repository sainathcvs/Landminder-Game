from Tkinter import *
import string
import random

# def show_grid(grid,grid_size):

# 	for i in range(grid_size):
# 		for j in range(grid_size):
# 			if grid[i][j]['status']=='s' or grid[i][j]['status']=='si':
# 				button=Button(width="3",height="3",bg='red',state=NORMAL,text='Sale',command=lambda row=i,col=j: btn_callback(row,col))
# 			elif grid[i][j]['status']=='b':
# 				button=Button(width="3",height="3",bg='green',state=NORMAL,text='Sold',command=lambda row=i,col=j: btn_callback(row,col))
# 			elif grid[i][j]['status']=='c':
# 				button=Button(width="3",height="3",bg='blue',state=NORMAL,text='Flat',command=lambda row=i,col=j: btn_callback(row,col))
# 			elif grid[i][j]['status']=='i':
# 				button=Button(width="3",height="3",bg='grey',state=NORMAL,text='Land',command=lambda row=i,col=j: btn_callback(row,col))
# 			# button.bind('<ButtonPress-1>', lambda event, row=i,col=j: btn_callback(row,col))
# 			button.grid(row=i,column=j)
# 	mainloop()

# def btn_callback(row,col):
# 	# if not gameover:
# 	flag=False

#value is (2*no. of constructed sites(c)+1*no. of bought flats(b)+0*unbought sites(i)-1*on sale sites(s))
def get_sum(row,col):
	constructed_sites_no = 0
	sites_no = 0

	return value

len_grid=8
cnt=0
blocks = [[{} for i in range(len_grid)] for i in range(len_grid)]

#initialize the block elements
for i in range(len_grid):
	for j in range(len_grid):
		blocks[i][j]['cost']=1
		blocks[i][j]['owner']=None
		blocks[i][j]['status']='i'
# show_grid(blocks,len_grid)
players_no=input('Enter the number of players:')

balances=[20 for i in range(players_no)]
print balances
print len(blocks)

while 1:
	player_name=cnt%players_no
	input_cell = input('Enter the block you want to buy/construct/put on sale/sell:')
	row,col,option = input_cell
	print row
	print col
	print option
	if option.lower()=='b':
		#logic for buying
		#check if the land is either on sale/initial stage
		if blocks[row-1][col-1]['status']=='i' or blocks[row-1][col-1]['status']=='s' or blocks[row-1][col-1]['status']=='si':
			#check if player has enough balance
			if balances[player_name-1]-blocks[row-1][col-1]['cost']>0:
			#if initial/on sale, decrease the cost from player balance
				balances[player_name-1]-=blocks[row-1][col-1]['cost']
			# if onsale, add the amount to the original player
				if blocks[row-1][col-1]['status']=='s':
					balances[blocks[row-1][col-1]['owner']-1]+=blocks[row-1][col-1]['cost']
			# increase the cost of block by 1
				blocks[row-1][col-1]['cost']+=1
			# update the owner field with the player
				blocks[row-1][col-1]['player_name']=player_name
			# change the status to bought b
				blocks[row-1][col-1]['status']='b'
				cnt+=1
			else:
				print 'Not enough balance to buy the site. Please sell a flat and try again.'
	elif option.lower()=='si':
		#logic for selling
		# check if given block belongs to current player or not
		if blocks[row-1][col-1]['owner']==player_name:
			blocks[row-1][col-1]['status']='si'
			#existing cost plus surrounding blocks cost
			blocks[row-1][col-1]['cost']=blocks[row-1][col-1]['cost']
			blocks[row-1][col-1]['owner']=None
			print player_name,' before sell immediately bal---',balances[blocks[row-1][col-1]['owner']-1]
			balances[blocks[row-1][col-1]['owner']-1]+=blocks[row-1][col-1]['cost']
			print player_name,' after sell immediately bal---',balances[blocks[row-1][col-1]['owner']-1]
			# cnt+=1
		# change the status to 'on sale' s by updating the cost to the sum of surrounding blocks value
	elif option.lower()=='s':
		#logic for selling
		# check if given block belongs to current player or not
		if blocks[row-1][col-1]['owner']==player_name:
			# change the status to bought s
			blocks[row-1][col-1]['status']='s'
			#existing cost plus surrounding blocks cost
			blocks[row-1][col-1]['cost']=blocks[row-1][col-1]['cost']+get_sum(row,col)
			cnt+=1
		# change the status to 'on sale' s by updating the cost to the sum of surrounding blocks value

	elif option.lower()=='c':
		# logic for constructing
		# check if given block belongs to current player or not
		if blocks[row-1][col-1]['owner']==player_name:
			# change the status to bought c
			blocks[row-1][col-1]['status']='c'
		# increase the cost by 1
			blocks[row-1][col-1]['cost']+=1
			cnt+=1
	# show_grid(blocks,len_grid)
print blocks_status

# initial-1
# bought-2
# construct-3
#if immediate sell, gets only the cost
#if kept on sale, gets the cost plus the cost of surrounding flats
