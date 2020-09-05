#!/usr/bin/python3

import subprocess

def clean_output(output):
    clean_output = output.decode('utf-8').split('\n')[:-2]
    return clean_output

def ascii_to_text(ascii_list):
    return ''.join([chr(int(i)) for i in ascii_list])

def solve(pcap_file):
    tshark_cmd = "tshark -nlr {}  -Y \"tcp.flags.syn==1 && tcp.flags.ack==0\" -T fields -e tcp.dstport | sed -r 's/^10//'".format(pcap_file)
    analyze_process = subprocess.Popen(tshark_cmd,shell=True,stdout=subprocess.PIPE)
    out,errors = analyze_process.communicate()
    flag = ascii_to_text(clean_output(out))
    return flag

def main():
    pcap_file = 'ping-pong.pcapng'
    flag = solve(pcap_file)
    print("Flag: {}".format(flag))


if __name__ == '__main__':
    main()
