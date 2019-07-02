'''
This program tests if three number inputs can form a triangle.
'''

# The three sides of a triangle are classibally called a, b, and c.
a = int(input("Input A: "))
b = int(input("Input B: "))
c = int(input("Input C: "))

def value_reorder(one, two, three):
	'''
	Forms an array from elements and orders them according to value.
	'''
	value_array = [one, two, three]
	value_array.sort()
	return value_array

def traingle_inequality_theorem(test_array):
	'''
	Assumes that the test array has already been ordered to have its third element as max.
	'''
	triangle = False
	if test_array[0] + test_array[1] >= test_array[2]:
		triangle = True
		print("Triangle")
		right_triangle(test_array)
	else:
		print("Not Triangle")
	return triangle

def right_triangle(triangle):
	'''
	Tests if triangle can form a right triangle
	'''
	right = False
	if (triangle[0] ** 2 + triangle[1] ** 2 == triangle[2] ** 2):
		right = True
		print("Right Triangle")
	return right

ordered = value_reorder(a, b, c)
traingle_inequality_theorem(ordered)
