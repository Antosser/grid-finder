import json

def generate(p):
	file = open('grid.html', 'r')
	html = file.read()
	file.close()

	params = {"x": 0, "y": 0, "lang": 0}
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

	table = '<table>\n'
	for j in range(y):
		table += '\t\t<tr>\n'
		for i in range(x):
			table += '\t\t\t<td id="' + '0' * (2 - len(str(i))) + str(i) + '0' * (2 - len(str(j))) + str(j) + '" '
			table += 'onkeypress = "javascript:tab(this.id)">\n'
			table += '\t\t\t\t<input style="width:20px;height:20px;" />\n'
			table += '\t\t\t</td>\n'
		table += '\t\t</tr>\n'
	table += '\t</table>'

	try:
		html = html.replace('{{x}}', str(x))
		html = html.replace('{{x}}', str(x))
		html = html.replace('{{y}}', str(y))
		html = html.replace('{{y}}', str(y))
		html = html.replace('{{lang}}', params['lang'])
		html = html.replace('{{lang}}', params['lang'])
		html = html.replace('{{table}}', table)

		return html
	except Exception as ex:
		return 'Error: Could not compile html\n'