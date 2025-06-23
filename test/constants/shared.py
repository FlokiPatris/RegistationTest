from typing import Final

class WaitTimes:
    VERY_SHORT: Final[int] = 100       # 100 ms
    SHORT: Final[int] = 500            # 500 ms
    MEDIUM: Final[int] = 2000          # 2 seconds
    LONG: Final[int] = 5000            # 5 seconds
    VERY_LONG: Final[int] = 10000      # 10 seconds
    EXTRA_LONG: Final[int] = 100000    # 100 seconds

class FieldTypes:
    STRING: Final[str] = "string"
    DATE: Final[str] = "date"
    DROPDOWN: Final[str] = "dropdown"
    CHECKBOX: Final[str] = "checkbox"
    NUMBER: Final[str] = "number"