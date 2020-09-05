import argparse
import codecs
from pwn import *


def clean_output(output):
	return output.decode('utf-8').strip('\n').split('<<')[1].split('>>')[0]


def solve(ip,port):

	conn = remote(ip,port)

	# Solve 1st question: transform input in hex
	first_q = conn.recvline()
	first_q = hex(int(clean_output(first_q)))
	conn.sendline(first_q)

	# Solve 2nd question: transform hex input in ascii
	second_q = conn.recvline()
	second_q = codecs.decode(clean_output(second_q).encode(),'hex').decode()
	conn.sendline(second_q)

	# Solve 3rd question: transform octal input in ascii
	third_q = conn.recvline()
	third_q = "".join([chr(int(octal_char,8)) for octal_char in clean_output(third_q).split(' ')])
	conn.sendline(third_q)

	# Get flag
	flag = conn.recvline()
	flag = flag.decode('utf-8').strip('\n').split('Input:')[1]
	
	return flag


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