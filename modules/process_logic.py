import logging

def process_item(item):
    """
    Processes a single item.
    :param item: A dictionary or DataFrame row representing the item.
    :return: Dictionary with processing results.
    """
    try:
        logging.info(f"Processing item: {item}")
        # Add your business logic here
        result = {
            "item_id": item.get("id", "unknown"),
            "status": "success",
            "details": "Processed successfully"
        }
        return result
    except Exception as e:
        logging.error(f"Error processing item {item}: {e}")
        raise
