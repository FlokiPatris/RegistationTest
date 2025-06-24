from registration.constants.urls.shared import Urls
from registration.constants.shared import WaitTimes, FieldTypes
from registration.helpers.utils import is_date_ddmmyyyy, get_tittle
from registration.models.registration import RegistrationFields

class RegistrationPage:
    def __init__(self, page):
        self.page = page
        self.url = Urls.REGISTRATION_URL

    def _fill_input(self, selector: str, value: str) -> None:
        element = self.page.wait_for_selector(selector, timeout=WaitTimes.LONG)
        element.fill(value)

    def navigate(self) -> None:
        self.page.goto(self.url)
        self.wait_until_loaded()

    def wait_until_loaded(self) -> None:
        self.page.wait_for_selector(RegistrationFields.FORM_SELECTOR, timeout=WaitTimes.LONG)

    def validate_and_fill_field(self, selector: str, field_type: FieldTypes, value) -> None:
        if field_type == FieldTypes.STRING:
            if selector.endswith(RegistrationFields.FIRST_NAME.selector) and value:
                # Special handling for the title case.
                self.select_title_by_name(value)
            if not isinstance(value, str):
                raise ValueError(f"Expected a string for {selector}, got {type(value)}.")
        elif field_type == FieldTypes.DATE:
            if not is_date_ddmmyyyy(value):
                raise ValueError(f"Expected a date for {selector}, got {type(value)} instead.")
        elif field_type == FieldTypes.NUMBER:
            try:
                value = str(int(value))
            except (ValueError, TypeError):
                raise ValueError(f"Expected a number for {selector}, got {value}.")
        elif field_type == FieldTypes.CHECKBOX:
            if not isinstance(value, bool):
                raise ValueError(f"Expected a boolean for checkbox {selector}, got {type(value)}.")
            if value:
                self.page.locator(selector).click()
            return  # Skip _fill_input for checkboxes.
        else:
            raise ValueError("Unsupported field type.")

        self._fill_input(selector, value)

    def select_title_by_name(self, name: str) -> None:
        """
        Determine the appropriate title ('Pan', 'Paní') based on the provided name.
        """
        title = get_tittle(name)
        title_selector = RegistrationFields.TITLE_CODE.selector

        self.page.click(title_selector)
        self.page.select_option(title_selector, title)

    def fill_form_field(self, field_key: str, value) -> None:
        mapping = RegistrationFields.get_all_fields().get(field_key)
        if not mapping:
            raise ValueError(f"Unknown field key: '{field_key}'")

        self.validate_and_fill_field(mapping.selector, mapping.field_type, value)

    def populate_form_values(self, data: dict) -> None:
        """
        Fills all fields on the registration form using the provided dictionary.
        The keys must correspond to the camelCase names generated from RegistrationField.
        """
        for field_key, value in data.items():
            self.fill_form_field(field_key, value)

    def submit_form(self) -> None:
        locator = self.page.get_by_role("button", name="Zaregistrovat se")
        # Scroll the element into view using center alignment.
        # The screen was going up and down when I was using self.page.get_by_role("button", name="Zaregistrovat se").click()
        locator.evaluate("node => node.scrollIntoView({ block: 'center', inline: 'center' })")
        locator.click()