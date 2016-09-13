#!/usr/bin/env python

import sys
import time
from socket import *


MAX_BUFFER_SIZE = 1024
UDP_IP = "0.0.0.0"

def print_str(str, addr):
    print "[DEBUG] (%s) recv message from %s(%s):" % (time.asctime(), addr[0], addr[1])
    for c in str:
        if '\r' == c:
            sys.stdout.write("\\r")
        elif '\n' == c:
            sys.stdout.write("\\n")
        else:
            sys.stdout.write(c)
    sys.stdout.write("\n\n")
    sys.stdout.flush()


def print_in_hex(str, addr):
    print "[DEBUG] (%s) recv message(%d bytes) from %s(%s):" % (time.asctime(), len(str), addr[0], addr[1])
    index = 0
    for c in str:
        if 0 == index % 4:
            print "\t%04X " % index,
        print "%02X" % ord(c),
        if 3 == index % 4:
            print
        index += 1
    print
    sys.stdout.flush()


# ./print_recv_bytes.py [port]
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "USAGE :", sys.argv[0], "[Port]"
        sys.exit()

    UDP_PORT = int(sys.argv[1])
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print "[DEBUG] (%s) Linstening port %d ..." % (time.asctime(), UDP_PORT)

    while True:
        data, addr = sock.recvfrom(MAX_BUFFER_SIZE)
        print_in_hex(data, addr)


