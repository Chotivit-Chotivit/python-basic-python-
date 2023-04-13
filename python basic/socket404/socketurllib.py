#socketเเบบurllib
import urllib.request,urllib.parse,urllib.error
html = urllib.request.urlopen("https://webserv.kmitl.ac.th/socialblog/text.txt")
for line in html:
	print(line.decode().strip())

	