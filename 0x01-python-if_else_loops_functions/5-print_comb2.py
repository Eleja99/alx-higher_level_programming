for i in range (100):
	if i == 99:
		print(i)
	else:
		print(f"{'0' + str(i)}" if i < 10 else f"{i}" , end = ', ')
		#print('0' + str(i) if i < 10 else i, end = ', ')
