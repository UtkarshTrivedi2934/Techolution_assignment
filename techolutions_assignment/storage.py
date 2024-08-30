import json
from typing import Dict, List, Union

def save_to_file(filename: str, data: Union[List[Dict], Dict]) -> None:
    """
    Save data to a JSON file.

    Parameters:
    - filename (str): The name of the file to save data to.
    - data (Union[List[Dict], Dict]): The data to be saved.
    
    Returns:
    - None
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_from_file(filename: str) -> Union[List[Dict], Dict]:
    """
    Load data from a JSON file.

    Parameters:
    - filename (str): The name of the file to load data from.
    
    Returns:
    - Union[List[Dict], Dict]: The loaded data.
    """
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if the file does not exist
    except json.JSONDecodeError:
        print("Error decoding JSON. Returning empty data.")
        return []
