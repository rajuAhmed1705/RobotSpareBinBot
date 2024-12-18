import pandas as pd
import logging

def load_items(file_path):
    """
    Loads input items from a CSV file.
    :param file_path: Path to the input file.
    :return: DataFrame containing the items.
    """
    try:
        logging.info(f"Loading input file from {file_path}")
        items = pd.read_csv(file_path)
        if items.empty:
            raise ValueError("Input file is empty.")
        return items
    except FileNotFoundError:
        logging.error(f"Input file not found at {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error loading input file: {e}")
        raise
