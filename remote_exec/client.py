import xmlrpc.client
import sys


def main(argv):
    if argv is None:
        argv = sys.argv
    ip = argv[1]
    port = argv[2]

    with xmlrpc.client.ServerProxy("http://"+ip+":"+port) as proxy:
        result = proxy.execute('ls')
        print(result)

if __name__ == "__main__":
    main(sys.argv)