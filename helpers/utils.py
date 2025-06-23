import gender_guesser.detector as gender
from datetime import datetime

def is_date_ddmmyyyy(value: str) -> bool:
    """
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

def is_male(name: str) -> str:
    d = gender.Detector()
    result = d.get_gender(name)

    if result in ("male", "mostly_male"):
        return 'Pan'
    elif result in ("female", "mostly_female"):
        return 'Paní'
    raise ValueError(f"Could not determine gender for name: {name} (detected: {result})")