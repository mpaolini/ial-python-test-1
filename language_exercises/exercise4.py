import sys

def htmlStyle(argv):
	if(len(sys.argv) > 1):
		for word in sys.argv[1:]:
			print "<p> " + word +" </p>"

htmlStyle(sys.argv)