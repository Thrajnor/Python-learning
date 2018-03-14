import webbrowser
import time
import sys

def youtube():
	time.sleep(4)
	print('jugyfjgf')
	webbrowser.open("https://www.youtube.com/watch?v=FCAoOlNh6sw")

def breaks():
	print "enough breaks !"
	time.sleep(4)
	sys.exit()

count = 0
while count < 3:
	youtube()
	count = count + 1
else:
	breaks()
