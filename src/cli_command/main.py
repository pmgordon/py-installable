"""This is a main file"""
from cli_command import arguments
from cli_command import configs

def main():
    """This is the main Function"""
    #args = arguments.parse_args()
    config = configs.parse_config()
    print("This is the main")
    return 0
