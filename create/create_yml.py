""" This file will create a yml file. """
import yaml


if __name__ == "__main__":
    # Create some data to write to the file
    data = {'name': 'John Smith', 'age': 30, 'city': 'New York',"children": ["John", "Jane"]}

    # Open the file in write mode
    with open('config.yml', 'w') as outfile:
        # Write the data to the file
        yaml.dump(data, outfile)
