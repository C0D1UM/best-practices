import sys
while True:
	try:
		year=int(input('Enter year: '))
	except KeyboardInterrupt:
		print()
		sys.exit()
	if year==0:
		print('Enter number> 0')
	if year%400==0:
		print(year,True,sep='->')
	elif year%100!=0 and year%4==0 :
		print(year,True,sep='->')
	else:
		print(year,False,sep='->')
