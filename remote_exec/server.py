from xmlrpc.server import SimpleXMLRPCServer
import sys, subprocess, configparser


def execute(user, password, command):
    """

    :param command: str
    :param password: str
    :type user: str
    """
    print(user,password,command)

    config = configparser.RawConfigParser()
    config.read('config.default')

    try:
        user_pass = config.get(user, 'password')
        perm_string = config.get(user, 'permissions')
        permissions = perm_string.split(',')
        print('database: userpass= ', user_pass, ' permissions=',permissions)
    except configparser.NoSectionError as e:
        print(e)
        return "User not found"

    if password != user_pass:
        return "Incorrect password"
    if command not in permissions:
        return "User has no permission"


    result = subprocess.check_output(command, stderr=subprocess.STDOUT)
    return result.decode('utf-8')


def main(argv):
    if argv is None:
        argv = sys.argv
    # read from config and serve

    s = SimpleXMLRPCServer(("", 8888))
    s.register_function(execute)
    s.serve_forever()


if __name__ == "__main__":
    main(sys.argv)
