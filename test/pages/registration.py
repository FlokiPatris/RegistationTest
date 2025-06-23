from test.constants.selectors.registration import SUBMIT_BUTTON
from test.constants.urls.shared import Urls
from test.helpers.utils import is_date_ddmmyyyy, get_tittle
from test.models.registration import RegistrationField
from dataclasses import dataclass
from typing import Literal

FieldType = Literal["string", "date", "dropdown", "checkbox", "number"]

@dataclass
class FieldMapping:
    selector: str
    data_type: FieldType

FORM_SELECTOR = "form#account-create"

FIELD_MAPPING = {
    RegistrationField.TITLE_CODE: FieldMapping(selector=f"{FORM_SELECTOR} #titleCode", data_type="dropdown"),
    RegistrationField.FIRST_NAME: FieldMapping(selector=f"{FORM_SELECTOR} #firstName", data_type="string"),
    RegistrationField.LAST_NAME: FieldMapping(selector=f"{FORM_SELECTOR} #lastName", data_type="string"),
    RegistrationField.DATE_OF_BIRTH: FieldMapping(
        selector=f"//form[@id='account-create']//div[@class='form-block text-input-block date-picker-wrapper']//input",
        data_type="date"
    ),
    RegistrationField.EMAIL: FieldMapping(selector=f"{FORM_SELECTOR} #email", data_type="string"),
    RegistrationField.POSTAL_CODE: FieldMapping(selector=f"{FORM_SELECTOR} #postalCode", data_type="number"),
    RegistrationField.CITY: FieldMapping(selector=f"{FORM_SELECTOR} #city", data_type="string"),
    RegistrationField.STREET: FieldMapping(selector=f"{FORM_SELECTOR} #street", data_type="string"),
    RegistrationField.HOUSE_NUMBER: FieldMapping(selector=f"{FORM_SELECTOR} #houseNumber", data_type="number"),
    RegistrationField.ADDRESS: FieldMapping(selector=f"{FORM_SELECTOR} #Address", data_type="string"),
    RegistrationField.PASSWORD: FieldMapping(selector=f"{FORM_SELECTOR} #password", data_type="string"),
    RegistrationField.PASSWORD_REPEAT: FieldMapping(selector=f"{FORM_SELECTOR} #passwordRepeat", data_type="string"),
    RegistrationField.MARKETING_CONSENT: FieldMapping(selector="label[for='CZ_MARKETING_CONSENT']", data_type="checkbox"),
    RegistrationField.REGISTRATION_CONSENT: FieldMapping(selector="label[for='CZ_REGISTRATION_CONSENT']", data_type="checkbox"),
}

class RegistrationPage:
    def __init__(self, page):
        self.page = page
        self.url = Urls.REGISTRATION_URL

    def navigate(self) -> None:
        self.page.goto(self.url)
        self.wait_until_loaded()

    def wait_until_loaded(self) -> None:
        self.page.wait_for_selector(FORM_SELECTOR, timeout=5000)

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
        elif field_type == "string" and selector.endswith("#firstName") and value:
            self.select_title_by_gender(value)
        else:
            raise ValueError("Unsupported field type.")

        self._fill_input(selector, value)

    def select_title_by_gender(self, name: str) -> None:
        title = get_tittle(name)
        title_selector = FIELD_MAPPING[RegistrationField.TITLE_CODE].selector
        self.page.click(title_selector)
        self.page.select_option(title_selector, title)

    def fill_form_field(self, field_key: str, value) -> None:
        mapping = FIELD_MAPPING.get(field_key)
        if not mapping:
            raise ValueError(f"Unknown field key: '{field_key}'")

        self.validate_and_fill_field(mapping.selector, mapping.data_type, value)

    def populate_form_values(self, data: dict) -> None:
        """
        Fills all fields with the registration form using the provided data dictionary.
        Keys in the dictionary must correspond to valid RegistrationField constants.
        """
        for field_key, value in data.items():
            self.fill_form_field(field_key, value)

    def submit_form(self) -> None:
        self.page.click(SUBMIT_BUTTON)