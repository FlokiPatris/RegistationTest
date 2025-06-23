from datetime import datetime

def is_date_ddmmyyyy(value: str) -> bool:
    """
    Parameters:
        value (str): The date string to validate.

    Returns:
        bool: True if the string is a valid date in 'DDMMYYYY' format, False otherwise.
    """
    if not isinstance(value, str):
        return False
    try:
        datetime.strptime(value, "%d%m%Y")
        return True
    except ValueError:
        return False