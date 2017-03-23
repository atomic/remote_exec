# remote_exec

Remote exec utility function


----------------------
Installation
----------------------
```
$ pip install -r requirements.txt
$ python setup.py build
```

----------------------
Usage
----------------------
Executable server and client are located in `build/../`
For server, copy config.default to `build/../`

# Example:  

    Server machine: ./server config-file
    format:
    ```
    [username]
    password=1234
    permissions=ls,tree,ps
    ```

    Client machine:  ./client 
                        --server <server ip> 
                        --user <username> 
                        --password <password> 
                        --exec <program to execute>
