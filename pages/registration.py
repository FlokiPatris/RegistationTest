# from playwright.sync_api import Page, TimeoutError
from constants.selectors.registration import SUBMIT_BUTTON
from constants.urls.registration import REGISTRATION_URL
from helpers.utils import is_date_ddmmyyyy

FIELD_MAPPING = {
    "title_code": ("#titleCode", "string"),
    "first_name": ("#firstName", "string"),
    "last_name": ("#lastName", "string"),
    "date_of_birth": ("[data-gtm-form-interact-field-id='dateOfBirth']", "date"),
    "email": ("#email", "string"),
    "postal_code": ("#postalCode", "number"),
    "city": ("#city", "string"),
    "street": ("#street", "string"),
    "house_number": ("#houseNumber", "number"),
    "address": ("#address", "string"),
    "password": ("#password", "string"),
    "password_repeat": ("#passwordRepeat", "string"),
}

class RegistrationPage:
    def __init__(self, page):
        self.page = page
        self.url = REGISTRATION_URL

    def navigate(self):
        self.page.goto(self.url)
        self.wait_until_loaded()

    def wait_until_loaded(self):
        self.page.wait_for_selector("form#account-create, form", timeout=5000)

    def _fill_input(self, selector: str, value: str):
        element = self.page.wait_for_selector(selector, timeout=5000)
        element.fill(value)

    def validate_and_fill_field(self, selector: str, value, field_type: str):
        if field_type == "string":
            if not isinstance(value, str):
                raise ValueError(f"Expected a string for {selector}, got {type(value)}.")
        elif field_type == "date":
            if not is_date_ddmmyyyy(value):
                raise ValueError("Date must be in 'DD-MM-YYYY' format.")
        elif field_type == "number":
            try:
                value = str(int(value))
            except (ValueError, TypeError):
                raise ValueError(f"Expected a number for {selector}, got {value}.")
        else:
            raise ValueError("Unsupported field type.")

        self._fill_input(selector, value)

    def fill_form_field(self, field_key: str, value):
        """
        Generic function to fill any registration form field by its key.
        The `field_key` must be defined in FIELD_MAPPING.
        """
        if field_key not in FIELD_MAPPING:
            raise ValueError(f"Field key '{field_key}' is not defined in FIELD_MAPPING.")

        selector, field_type = FIELD_MAPPING[field_key]
        self.validate_and_fill_field(selector, value, field_type)

    def fill_form_values(self, data: dict):
        """
        Fills all fields with the registration form from a dictionary.

        Parameters:
            data (dict): Key/value pairs where keys correspond to field names in FIELD_MAPPING.

        Example:
            data = {
                "first_name": "John",
                "last_name": "Doe",
                "date_of_birth": "1990-01-01",
                "email": "john.doe@example.com",
                // etc.
            }
        """
        for field_key, value in data.items():
            self.fill_form_field(field_key, value)

    def submit_form(self):
        self.page.click(SUBMIT_BUTTON)
