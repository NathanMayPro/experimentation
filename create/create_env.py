""" This file will be used to create a .env file. """

import os


if __name__ == "__main__":
    # set new env variables
    os.environ["TEST"] = "1"
    os.environ["TEST_TEST"] = "2"
    # get env variables
    print(os.environ.get("TEST"))
    print(os.environ["TEST_TEST"])
    
    
 
    
    # to write in .env file
    with open(".env", "w") as f:
        for key, value in os.environ.items():
            f.write(f"{key}={value}\n")

    os.system("cat .env")
    
    