from constants.shared import FieldTypes

class FieldMappings:
    def __init__(self, selector: str, field_type: str):
        self.selector = selector
        self.field_type = field_type
        self.field_name: str  = ''

    def __set_name__(self, owner, name):
        # Called automatically when the class is created
        # name == the attribute name to lower snake_case
        self.field_name = name.lower()

class RegistrationFields:
    """
    Encapsulates all registration form field mappings.

    Every field is automatically scoped to the parent form, ensuring that
    every selector references the correct element. The auto-generated dictionary
    (via get_all_fields()) converts attribute names to lower-case (snake_case)
    keys for consistency.
    """
    ROOT_SELECTOR = "form#account-create"

    # UI field mappings
    TITLE_CODE = FieldMappings(
        selector   = f"{ROOT_SELECTOR} #titleCode",
        field_type = FieldTypes.DROPDOWN
    )
    FIRST_NAME = FieldMappings(
        selector   = f"{ROOT_SELECTOR} #firstName",
        field_type = FieldTypes.STRING
    )
    LAST_NAME  = FieldMappings(
        selector   = f"{ROOT_SELECTOR} #lastName",
        field_type = FieldTypes.STRING
    )
    DATE_OF_BIRTH = FieldMappings(
        selector   = f"{ROOT_SELECTOR} div.form-block.text-input-block.date-picker-wrapper input",
        field_type = FieldTypes.STRING
    )
    EMAIL = FieldMappings(
        selector   = f"{ROOT_SELECTOR} #email",
        field_type = FieldTypes.STRING
    )
    POSTAL_CODE = FieldMappings(
        selector   = f"{ROOT_SELECTOR} #postalCode",
        field_type = FieldTypes.NUMBER
    )
    CITY = FieldMappings(
        selector   = f"{ROOT_SELECTOR} #city",
        field_type = FieldTypes.STRING
    )
    STREET = FieldMappings(
        selector   = f"{ROOT_SELECTOR} #street",
        field_type = FieldTypes.STRING
    )
    HOUSE_NUMBER = FieldMappings(
        selector   = f"{ROOT_SELECTOR} #houseNumber",
        field_type = FieldTypes.NUMBER
    )
    ADDRESS = FieldMappings(
        selector   = f"{ROOT_SELECTOR} #Address",
        field_type = FieldTypes.STRING
    )
    PASSWORD = FieldMappings(
        selector   = f"{ROOT_SELECTOR} #password",
        field_type = FieldTypes.STRING
    )
    PASSWORD_REPEAT = FieldMappings(
        selector   = f"{ROOT_SELECTOR} #passwordRepeat",
        field_type = FieldTypes.STRING
    )
    MARKETING_CONSENT = FieldMappings(
        selector   = f"{ROOT_SELECTOR} label[for='CZ_MARKETING_CONSENT']",
        field_type = FieldTypes.CHECKBOX
    )
    REGISTRATION_CONSENT = FieldMappings(
        selector   = f"{ROOT_SELECTOR} label[for='CZ_REGISTRATION_CONSENT']",
        field_type = FieldTypes.CHECKBOX
    )

    @classmethod
    def get_all_fields(cls) -> dict:
        """
        Returns a dict mapping each field_name (snake_case) to its FieldMappings.
        """
        return {
            field_mapping.field_name: field_mapping
            for field_mapping in cls.__dict__.values()
            if isinstance(field_mapping, FieldMappings)
        }
