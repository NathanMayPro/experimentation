""" This file will check the yml file and return the data in the file. """
import yaml

if __name__ == "__main__":
    with open("config.yml", "r") as ymlfile:
        cfg = yaml.load(ymlfile)
    print(cfg)