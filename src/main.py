from src.additional_module import print_current_filepath
from src.settings import CONFIG

def main():

    print_current_filepath()

    # update the class
    CONFIG.update(scenario="new_scenario", verbose=True)

    # validate that it gets updated downstream
    print_current_filepath()

if __name__ == "__main__":

    main()