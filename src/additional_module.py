from src.settings import CONFIG

def print_current_filepath():
    """Prints the current value of fp_data in CONFIG."""    
    
    print(f"{CONFIG.fp_data = }")

    return