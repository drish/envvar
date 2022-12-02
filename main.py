import os

from envvar import load

x = load(os.getcwd() + "/examples/config.yaml")
print(x)
