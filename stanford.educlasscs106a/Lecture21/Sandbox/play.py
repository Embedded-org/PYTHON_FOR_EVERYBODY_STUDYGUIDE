class Dog:
	def __init__(self, name):
		print(self)
		self.name = name
		print(self.name)

# put in another file...

def main():
	first = Dog('jupiter')	
	print(first)
	print(type(first))
	print(id(first))
	print(first.__dict__)

if __name__ == '__main__':
	main()
