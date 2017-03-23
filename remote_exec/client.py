#!/usr/bin/env python
import xmlrpc.client
import sys, getopt


# Client machine: ./client --server <server ip> --user <username> --password <password> --exec <program to execute>

def main(argv):
    global command, ip
    try:
        opts, args = getopt.getopt(argv[1:], "hsupx", ["server=", "user=", "password=", "exec="])
    except getopt.GetoptError:
        print('./client --server <server ip> --user <username> --password <password> --exec <program to execute>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-s", "--server"):
            ip = arg
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-x", "--exec"):
            command = arg

    port = "8888"

    with xmlrpc.client.ServerProxy("http://" + ip + ":" + port) as proxy:
        result = proxy.execute(command)
        print(result)


if __name__ == "__main__":
    main(sys.argv)
