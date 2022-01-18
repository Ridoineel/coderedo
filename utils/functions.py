import argparse
import re
from math import ceil

def parser():
	parse = argparse.ArgumentParser()
	parse.add_argument("--file", "-f", help="python file path (.py)", type=str)

	return parse.parse_args()

def getFileContent(path: str) -> [str]:
	file = open(path, "r") 
	contents = file.readlines()

	return contents

def getFilePath():
	file_path = parser().file

	return file_path

def isPythonFile(file_path):
	return ".py" in file_path and file_path.index(".py") == len(file_path) - 3 # 3 for length of ".py"

def whitespacesToTabs(string):
	""" Replace all start whitespaces (with tab) to tabulations once 

	"""

	wspaces = int()

	for char in string:
		if char == " ":
			wspaces += 1
		elif char == "\t":
			wspaces += 4
		else:
			break

	tabs = round(wspaces/4)

	new_string = re.sub(r"^(( |\t)+)", "\t" * tabs, string)

	return new_string

def createNewFile(file_path, contents: [str]):
	file = open(file_path, "w")

	for line in contents:
		file.write(line)

	file.close()