dataOne = ['hello', 10,234.345]
dataTwo = 100

def funOne():
	print(f'funOne()...{__name__}')

def funTwo():
	print(f'funTwo()...{__name__}')		
	
def funThree():
	print(f'funThree()...{__name__}')	

if __name__ =='__main__':
	funOne()