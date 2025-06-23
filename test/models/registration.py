from dataclasses import dataclass
from test.constants.shared import FieldTypes

@dataclass
class FieldMapping:
    selector: str
    field_type: str

# Base form selector that scopes all fields.
FORM_SELECTOR = "form#account-create"

class RegistrationField:
    """
    Encapsulates all registration form field mappings.

    Every field is automatically scoped to the parent form, ensuring that
    every selector references the correct element. The auto-generated dictionary
    (via get_all_fields()) converts attribute names to lower-case (snake_case)
    keys for consistency.
    """
    FORM_SELECTOR = FORM_SELECTOR

    # UI field mappings
    TITLE_CODE = FieldMapping(selector=f"{FORM_SELECTOR} #titleCode", field_type=FieldTypes.DROPDOWN)
    FIRST_NAME = FieldMapping(selector=f"{FORM_SELECTOR} #firstName", field_type=FieldTypes.STRING)
    LAST_NAME = FieldMapping(selector=f"{FORM_SELECTOR} #lastName", field_type=FieldTypes.STRING)
    DATE_OF_BIRTH = FieldMapping(
        # Even though this might be an XPath, we include the parent scope consistently.
        selector=f"{FORM_SELECTOR} //div[@class='form-block text-input-block date-picker-wrapper']//input",
        field_type=FieldTypes.DATE
    )
    EMAIL = FieldMapping(selector=f"{FORM_SELECTOR} #email", field_type=FieldTypes.STRING)
    POSTAL_CODE = FieldMapping(selector=f"{FORM_SELECTOR} #postalCode", field_type=FieldTypes.NUMBER)
    CITY = FieldMapping(selector=f"{FORM_SELECTOR} #city", field_type=FieldTypes.STRING)
    STREET = FieldMapping(selector=f"{FORM_SELECTOR} #street", field_type=FieldTypes.STRING)
    HOUSE_NUMBER = FieldMapping(selector=f"{FORM_SELECTOR} #houseNumber", field_type=FieldTypes.NUMBER)
    ADDRESS = FieldMapping(selector=f"{FORM_SELECTOR} #Address", field_type=FieldTypes.STRING)
    PASSWORD = FieldMapping(selector=f"{FORM_SELECTOR} #password", field_type=FieldTypes.STRING)
    PASSWORD_REPEAT = FieldMapping(selector=f"{FORM_SELECTOR} #passwordRepeat", field_type=FieldTypes.STRING)
    MARKETING_CONSENT = FieldMapping(
        selector=f"{FORM_SELECTOR} label[for='CZ_MARKETING_CONSENT']",
        field_type=FieldTypes.CHECKBOX
    )
    REGISTRATION_CONSENT = FieldMapping(
        selector=f"{FORM_SELECTOR} label[for='CZ_REGISTRATION_CONSENT']",
        field_type=FieldTypes.CHECKBOX
    )

    @classmethod
    def get_all_fields(cls) -> dict:
        """
        Dynamically generates and returns a dictionary of all field mappings.

        The dictionary keys are created by converting the attribute names to lower-case.
        This ensures that all keys are in snake_case.
        """
        return {
            attr_name.lower(): attr_value  # Convert the attribute name to lower-case.
            for attr_name, attr_value in cls.__dict__.items()
            if isinstance(attr_value, FieldMapping)
        }