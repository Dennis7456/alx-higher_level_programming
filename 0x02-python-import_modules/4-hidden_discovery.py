#!/usr/bin/python3
if __name__ == "__main__":
	import hidden_4
	for s in dir(hidden_):
		if s[:2] != "__":
			print("{:s}".format(s))