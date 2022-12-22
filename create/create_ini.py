""" This file will be used to create a .ini file. """

import configparser

if __name__ == "__main__":
    # Create the config file
    config = configparser.ConfigParser()
    # Add the sections
    config.add_section("Settings")
    config.add_section("Database")
    # Add the settings
    config.set("Settings", "debug", "True")
    config.set("Settings", "port", "8080")
    config.set("Settings", "secret_key", "12345")
    
    # save to a file
    with open("config.ini", "w") as config_file:
        config.write(config_file)