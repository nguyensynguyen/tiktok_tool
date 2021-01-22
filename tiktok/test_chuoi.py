def TestChuoi():
	f= open('amthuc1.txt','r',encoding="utf8")
	str1 = f.readlines()
	print(len(str1))
	for x in str1:
		for item in x.split(sep=' '):
			if (item.__contains__('http')):
				print(item)
   #  	for item in x.split(sep = ' '):
			# if(item.__contains__('http')):
			# 	print(item)
	
		
TestChuoi()