line1 = raw_input('enter equation of first line:')
line2 = raw_input('enter equation of second line:')

#                     0123456789
# equation of a line: y = mx + b

def m(line):	# slope
	x = line.index('x')
	if line[x - 1] == ' ':	# if x = 1
		return 1
	elif line[x - 1] == '-':	# if x = -1
		return -1
	else:
		return float(line[4:x])

def b(line):	# y-intercept
	if line[-1] == 'x':    # if no b
		return 0
	elif '+' in line:	# if b is positive
		plus = line.index('+')
		return float(line[plus + 2:])
	elif '-' in line[5:]:	# if b is negative
		b_part = line[5:]
		return -float(b_part[b_part.index('-') + 2:])

m1 = m(line1)
b1 = b(line1)
m2 = m(line2)
b2 = b(line2)

if m2 != m1:	# if slopes are different
	coefficient_x = m2 - m1
else:	# if slopes are same
	coefficient_x = 1	# doesnt matter
x_equals = b1 - b2

x = x_equals / coefficient_x
y = m1 * x + b1

if m1 == m2 and b1 == b2:
	print('infinite POI')
elif m1 == m2:
	print('lines are parallel')
else:
	print('POI(' + str(x) + ',' + str(y) + ')')





