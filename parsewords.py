import numpy as np

def parse(x, y, words, table):
	table = list(table)
	result = []
	table = np.reshape(table, (y, x))
	table = table.tolist()
	print(table)
	for i in range(y):
		row = ''
		for j in range(x):
			row += table[i][j]
		for j in range(x):
			for k in range(x):
				if k < j:
					continue
				k += 1
				if row[j:k] in words and not row[j:k] in result:
					result.append(row[j:k])
	for i in range(y):
		row = ''
		for j in range(x):
			row += table[i][x - j - 1]
		for j in range(x):
			for k in range(x):
				if k < j:
					continue
				k += 1
				if row[j:k] in words and not row[j:k] in result:
					result.append(row[j:k])
	for i in range(x):
		row = ''
		for j in range(y):
			row += table[j][i]
		for j in range(y):
			for k in range(y):
				if k < j:
					continue
				k += 1
				if row[j:k] in words and not row[j:k] in result:
					result.append(row[j:k])
	for i in range(x):
		row = ''
		for j in range(y):
			row += table[y - i - 1][j]
		for j in range(y):
			for k in range(y):
				if k < j:
					continue
				k += 1
				if row[j:k] in words and not row[j:k] in result:
					result.append(row[j:k])
	# Diagonal
	for i in range(x + y - 1):
		row = ''
		if True:
			j = 0
			k = 0
			if i < x:
				j = i
			else:
				k = i
			while j < x and k < y:
				row += table[k][j]
				j += 1
				k += 1
		for j in range(len(row)):
			for k in range(len(row)):
				if k < j:
					continue
				k += 1
				if row[j:k] in words and not row[j:k] in result:
					result.append(row[j:k])
	for i in range(x + y - 1):
		row = ''
		if True:
			j = 0
			k = 0
			if i < x:
				j = i
			else:
				k = i
			while j < x and k < y:
				row += table[k][j]
				j += 1
				k += 1
		row = row[::-1]
		for j in range(len(row)):
			for k in range(len(row)):
				if k < j:
					continue
				k += 1
				if row[j:k] in words and not row[j:k] in result:
					result.append(row[j:k])
	for i in range(x + y - 1):
		row = ''
		if True:
			j = 0
			k = 0
			if i < x:
				j = i
				k = y - 1
			else:
				k = i
			while j < x and k < y:
				row += table[k][j]
				j += 1
				k -= 1
		for j in range(len(row)):
			for k in range(len(row)):
				if k < j:
					continue
				k += 1
				if row[j:k] in words and not row[j:k] in result:
					result.append(row[j:k])
	for i in range(x + y - 1):
		row = ''
		if True:
			j = 0
			k = 0
			if i < x:
				j = i
				k = y - 1
			else:
				k = i
			while j < x and k < y:
				row += table[k][j]
				j += 1
				k -= 1
		row = row[::-1]
		for j in range(len(row)):
			for k in range(len(row)):
				if k < j:
					continue
				k += 1
				if row[j:k] in words and not row[j:k] in result:
					result.append(row[j:k])
	return str(len(result)) + ' found)</h1>\n' + '<br />\n'.join(result)