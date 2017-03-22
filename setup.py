# from setuptools import setup
from cx_Freeze import setup, Executable

setup(name='remote_exec',
      version='0.1.0',
      executables=[Executable('remote_exec/server.py'), Executable('remote_exec/client.py')],
      )
