'''
User program that takes in two points from command line and outputs
the linear equation.
'''

point1 = raw_input('enter first coordinate:')
point2 = raw_input('enter second coordinate:')

def x(point):	
	comma = point.find(',')
	return float(point[1:comma])
	
def y(point):
	comma = point.find(',')
	return float(point[comma + 1:-1])

x1 = x(point1)
y1 = y(point1)
x2 = x(point2)
y2 = y(point2)

print('')
if y2 - y1 == 0:	# if horizontal line
	print 'y =', y1
elif x2 - x1 == 0:	# if vertical line
	print 'x =', x1
else:
	m = (y2 - y1) / (x2 - x1)
	b = y1 - m * x1
	if b > 0:
		print 'y =', m, 'x +', b, 
	elif b < 0:
		print 'y =', m, 'x -', -b, 
	else:
		print 'y =', m, 'x'