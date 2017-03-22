from xmlrpc.server import SimpleXMLRPCServer
import subprocess


def execute(command):
    result = subprocess.check_output(command, stderr=subprocess.STDOUT)
    return result.decode('utf-8')

s = SimpleXMLRPCServer(("", 8888))
s.register_function(execute)
s.serve_forever()
