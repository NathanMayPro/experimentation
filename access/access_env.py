""" This file will test the access to the environment variables. """

from decouple import config

if __name__ == "__main__":
    print(config('TEST'))
    print(config('TEST_TEST'))