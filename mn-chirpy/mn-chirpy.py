# Imports for authorization by twitter
import authorization
import json
import requests
from urls import *

# Imports for Argparse command line thingy
import logging, csv
import argparse
import sys

# Create logging output file and the log level.
logging.basicConfig(filename="output.log", level=logging.DEBUG)

# Creating the parser
def make_parser():
	""" Construct a command line parser """
	logging.info("Creating Tweet Parser")
	description = "Command line tool to create tweets"
	parser = argparse.ArgumentParser(description=description)
	subparsers = parser.add_subparsers(dest="command", help="Available commands")

	# Creating post sub-parser
	logging.debug("Creating Post Parser for Chirpy")
	post_parser = subparsers.add_parser("post", help="post a tweet to your account")
	post_parser.add_argument("status", help="the message you want to post", nargs="?")
	return parser

# Main function
def main():
	""" Main function """
	auth = authorization.authorize()
	
	# Uncomment these lines to show that the auth is actually there and working.
	# response = requests.get(TIMELINE_URL, auth=auth)
	# print json.dumps(response.json(), indent=4)

	# Since we're already logged on at this point I can use the 
	# argparser to read the positional arguments and execute
	# what the user wants to do...

	# Command line parser here
	parser = make_parser()
	arguments = parser.parse_args()
	arguments = vars(arguments)
	command = arguments.pop("command")

	if command == "post":
		print "This is the command named status", arguments

if __name__ == '__main__':
	main()
