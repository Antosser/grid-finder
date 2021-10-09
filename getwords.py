import parsewords

def generate(p):
	html = '<h1>Results ('

	params = {"x": 0, "y": 0, "lang": 0, "table": 0}
	try:
		for i in p:
			params[i.split('=')[0]] = i.split('=')[1]
	except Exception:
		return 'Error: Could not parse parameters (p1)\n'
	for i in params:
		if i in (0, '0'):
			return 'Error: Could not parse parameters (p2)'
	x = int(params['x'])
	y = int(params['y'])
	lang = params['lang']
	if not len(params['table']) == x * y:
		return 'Table length is ' + str(len(params['table'])) + ' but ' + str(x * y) + ' was expected.'

	if not lang in ('english', 'german', 'russian'):
		return 'Error: Invalid language'
	file = open(lang + '.txt', 'r')
	words = file.read().split('\n')
	file.close()

	html += parsewords.parse(x, y, words, params['table'])

	return html