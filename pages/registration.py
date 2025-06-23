from playwright.sync_api import Page, TimeoutError
from constants.registration import REGISTRATION_URL


class RegistrationPage:
    #TODO - add getters for the elements and add corresponding name to getters. Here are the IDs of the form fields.
    #TODO : titleCode (form field),firstName (form field), lastName  (form field), data-gtm-form-interact-field-id  (form field date of birth), (form field),, email (form field),, postalCode (form field),, city (form field),, street (form field),,houseNumber (form field),, Address (form field),, password (form field),, passwordRepeat (form field),, CZ_MARKETING_CONSENT (marking off), CZ_REGISTRATION_CONSENT (marking off), submit ( save button_)
    def __init__(self, page: Page):
        self.page = page
        self.url = REGISTRATION_URL

    def navigate(self):
        """
        Navigates to the registration page and waits for the registration form to load.
        """
        self.page.goto(self.url)
        try:
            self.page.wait_for_selector("form", timeout=5000)
        except TimeoutError:
            raise Exception("Registration form did not load within 5 seconds.")

    def _fill_input(self, selector: str, value: str):
        """
        Helper method to wait for and fill an input field. Ensures the element is present.
        """
        try:
            element = self.page.wait_for_selector(selector, timeout=5000)
            element.fill(value)
        except TimeoutError:
            raise Exception(f"Element with selector '{selector}' not found on page.")

    def fill_field(self, selector: str, value, field_type: str):
        """
        Fills an input field based on the field's type.

        Parameters:
          selector (str): CSS selector for the target field.
          value (str|int): The value to be input. Expected type depends on field_type.
          field_type (str): Type of the field ('string', 'date', 'number').
        """
        if field_type == "string":
            if not isinstance(value, str):
                raise ValueError(f"Expected a string for field '{selector}', got {type(value)}.")
            self._fill_input(selector, value)

        elif field_type == "date":
            # TODO - add a simple method isDateInMMDDYYYY into utils.py that checks the date format. Remove this.
            if not (isinstance(value, str) and len(value) == 10):
                raise ValueError(f"Date value '{value}' must be a string in 'YYYY-MM-DD' format.")
            self._fill_input(selector, value)

        elif field_type == "number":
            try:
                number_str = str(int(value))
            except (ValueError, TypeError):
                raise ValueError(f"Invalid number value provided for field '{selector}'.")
            self._fill_input(selector, number_str)

        else:
            raise ValueError(f"Unsupported field type: '{field_type}'.")

        #TODO Add a method fillForm
        #TODO In this method all the form fields are going to be populated with values. We are expecting an list of values we want to populate in the form. The leght of the list has to equal the total number of fields. If not throww error.

