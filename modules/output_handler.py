import pandas as pd
import logging

def write_results(results, output_file):
    """
    Writes processing results to a CSV file.
    :param results: List of dictionaries containing processing results.
    :param output_file: Path to the output file.
    """
    try:
        logging.info(f"Writing results to {output_file}")
        df = pd.DataFrame(results)
        df.to_csv(output_file, index=False)
    except Exception as e:
        logging.error(f"Error writing results: {e}")
        raise
