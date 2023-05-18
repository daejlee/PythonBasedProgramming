class Rectangle():
	def __init__(self, length, width):
		self.__length = length
		self.__width = width
		print("Rectangle 생성")
	def set_dimension(self, length, width):
		self.__length = length
		self.__width = width
	def get_length(self):
		return self.__length
	def get_width(self):
		return self.__width
	def perimeter(self):
		return 2 * (self.__length + self.__width)
	def print(self):
		print(f'Length = {self.__length}, Width = {self.__width}, Area = {self.__length * self.__width}, Perimeter = {self.perimeter()}')

class Box(Rectangle):
	def __init__(self, length, width, height):
		self.__length = length
		self.__width = width
		self.__height = height
		print("Box 생성")
	def set_dimension(self, length, width, height):
		self.__length = length
		self.__width = width
		self.__height = height
	def area(self):
		return 2 * (self.__length * self.__width + self.__width * self.__height + self.__height * self.__length)
	def volume(self):
		return self.__length * self.__width * self.__height
	def print(self):
		print(f'Length = {self.__length}, Width = {self.__width}, Height = {self.__height}, Area = {self.area()}, Volume = {self.volume()}')


A = Rectangle(10, 20)
A.print()

B = Box(10, 20, 30)
B.print()