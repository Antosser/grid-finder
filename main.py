from http.server import HTTPServer, BaseHTTPRequestHandler
from time import time
from datetime import datetime
import requests
import json
import grid, getwords

class Serv(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/favicon.ico':
			self.send_response(200)
			self.send_header("Content-type", "image/png")
			self.end_headers()
			file = open('favicon.png', 'rb')
			image = file.read()
			file.close()
			self.wfile.write(image)
		else:
			self.send_response(200)
			self.send_header("Content-type", "text/html")
			self.end_headers()
			if self.path == '/':
				file = open('index.html', 'r')
				html = file.read()
				file.close()
				self.wfile.write(bytes(html, 'utf-8'))
			elif self.path in ('/index', '/index.html'):
				self.wfile.write(bytes('<script>location.pathname = "/"</script>', 'utf-8'))
			elif self.path.split('?')[0] == '/grid':
				self.wfile.write(bytes(grid.generate(self.path.split('?')[1].split('&')), 'utf-8'))
			elif self.path.split('?')[0] == '/getwords':
				self.wfile.write(bytes(getwords.generate(self.path.split('?')[1].split('&')), 'utf-8'))
			elif self.path in ('/english', '/german', '/russian'):
				file = open(self.path[1:] + '.txt', 'r')
				html = '<br />\n'.join(file.read().split('\n'))
				file.close()
				self.wfile.write(bytes(html, 'utf-8'))
			else:
				file = open('404.html', 'r')
				html = file.read()
				file.close()
				self.wfile.write(bytes(html, 'utf-8'))
httpd = HTTPServer(('localhost',8080), Serv)
httpd.serve_forever()