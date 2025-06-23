from constants.selectors.registration import SUBMIT_BUTTON
from constants.urls.registration import REGISTRATION_URL
from helpers.utils import is_date_ddmmyyyy, is_male
from dataclasses import dataclass
from typing import Literal

FieldType = Literal["string", "date", "dropdown", "checkbox", "number"]

@dataclass
class FieldMapping:
    selector: str
    data_type: FieldType

PARENT_SELECTOR = "form#account-create"

FIELD_MAPPING = {
    "title_code": FieldMapping(selector=f"{PARENT_SELECTOR} #titleCode", data_type="dropdown"),
    "first_name": FieldMapping(selector=f"{PARENT_SELECTOR} #firstName", data_type="string"),
    "last_name": FieldMapping(selector=f"{PARENT_SELECTOR} #lastName", data_type="string"),
    "date_of_birth": FieldMapping(
        selector=f"//form[@id='account-create']//div[@class='form-block text-input-block date-picker-wrapper']//input",
        data_type="date"
    ),
    "email": FieldMapping(selector=f"{PARENT_SELECTOR} #email", data_type="string"),
    "postal_code": FieldMapping(selector=f"{PARENT_SELECTOR} #postalCode", data_type="number"),
    "city": FieldMapping(selector=f"{PARENT_SELECTOR} #city", data_type="string"),
    "street": FieldMapping(selector=f"{PARENT_SELECTOR} #street", data_type="string"),
    "house_number": FieldMapping(selector=f"{PARENT_SELECTOR} #houseNumber", data_type="number"),
    "address": FieldMapping(selector=f"{PARENT_SELECTOR} #Address", data_type="string"),
    "password": FieldMapping(selector=f"{PARENT_SELECTOR} #password", data_type="string"),
    "password_repeat": FieldMapping(selector=f"{PARENT_SELECTOR} #passwordRepeat", data_type="string"),
    "marketing_consent": FieldMapping(selector="label[for='CZ_MARKETING_CONSENT']", data_type="checkbox"),
    "registration_consent": FieldMapping(selector="label[for='CZ_REGISTRATION_CONSENT']", data_type="checkbox"),
}

class RegistrationPage:
    def __init__(self, page):
        self.page = page
        self.url = REGISTRATION_URL

    def navigate(self) -> None:
        self.page.goto(self.url)
        self.wait_until_loaded()

    def wait_until_loaded(self) -> None:
        self.page.wait_for_selector("form#account-create, form", timeout=5000)

    def _fill_input(self, selector: str, value: str) -> None:
        element = self.page.wait_for_selector(selector, timeout=5000)
        element.fill(value)

    def validate_and_fill_field(self, selector: str, field_type: FieldType, value) -> None:
        if field_type == "string":
            if not isinstance(value, str):
                raise ValueError(f"Expected a string for {selector}, got {type(value)}.")
        elif field_type == "date":
            if not is_date_ddmmyyyy(value):
                raise ValueError(f"Expected a date for {selector}, got {type(value)} instead.")
        elif field_type == "number":
            try:
                value = str(int(value))
            except (ValueError, TypeError):
                raise ValueError(f"Expected a number for {selector}, got {value}.")
        elif field_type == "checkbox":
            if not isinstance(value, bool):
                raise ValueError(f"Expected a boolean for checkbox {selector}, got {type(value)}.")
            if value:
                self.page.locator(selector).click()
            return  # ⬅ skip _fill_input for checkboxes!
        else:
            raise ValueError("Unsupported field type.")

        self._fill_input(selector, value)

    def select_title_by_gender(self, name: str) -> None:
        is_male_or_female = is_male(name)
        self.page.click(FIELD_MAPPING["title_code"].selector)
        self.page.select_option(FIELD_MAPPING["title_code"].selector, is_male_or_female)

    def fill_form_field(self, field_key: str, value) -> None:
        if field_key not in FIELD_MAPPING:
            raise ValueError(f"Field key '{field_key}' is not defined in FIELD_MAPPING.")

        mapping = FIELD_MAPPING[field_key]

        self.validate_and_fill_field(mapping.selector, mapping.data_type, value)

    def populate_form_values(self, data: dict) -> None:
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
            if field_key == "first_name" and value:
                self.select_title_by_gender(value)

            self.fill_form_field(field_key, value)

    def submit_form(self) -> None:
        self.page.click(SUBMIT_BUTTON)