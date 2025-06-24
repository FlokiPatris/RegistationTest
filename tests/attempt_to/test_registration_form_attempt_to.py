from assertions.shared import wait_for_alert_text
from models.registration import RegistrationFields
from pages.registration import RegistrationPage
import pytest

@pytest.fixture
def reg_page(page):
    registration_page = RegistrationPage(page)
    registration_page.navigate()

    yield registration_page

base_registration_data = {
    RegistrationFields.FIRST_NAME.field_name:           "Joe",
    RegistrationFields.LAST_NAME.field_name:            "Small",
    RegistrationFields.EMAIL.field_name:                "tests10000@gmail.com",
    RegistrationFields.POSTAL_CODE.field_name:          "60200",
    RegistrationFields.CITY.field_name:                 "Prague",
    RegistrationFields.STREET.field_name:               "Main Street 2",
    RegistrationFields.HOUSE_NUMBER.field_name:         "5811",
    RegistrationFields.ADDRESS.field_name:              "123 Main Street, Apt 4",
    RegistrationFields.PASSWORD.field_name:             "test1234!@#$",
    RegistrationFields.PASSWORD_REPEAT.field_name:      "test1234!@#$",
    RegistrationFields.REGISTRATION_CONSENT.field_name: True,
    RegistrationFields.MARKETING_CONSENT.field_name:    True,
    RegistrationFields.DATE_OF_BIRTH.field_name:        "10051995",
}

from models.registration import RegistrationFields

registration_data_samples = [
    # Too long last name
    # TODO: BUG: API returns RC 500 in this case. Commented until bug is fixed.
    # (
    #     {
    #         **base_registration_data,
    #         RegistrationFields.LAST_NAME.key: "s" * 256
    #     },
    #     "Přijmení je příliš dlouhé"
    # ),

    # Invalid email
    (
        {
            **base_registration_data,
            RegistrationFields.EMAIL.field_name: "invalidemail@invalid"
        },
        "Prosím zadejte email ve správném formátu"
    ),

    # Short password
    (
        {
            **base_registration_data,
            RegistrationFields.PASSWORD.field_name: "123"
        },
        "Heslo musí být o délce minimálně 8 znaků"
    ),

    # Non-sufficient password
    (
        {
            **base_registration_data,
            RegistrationFields.PASSWORD.field_name: "0123456789"
        },
        "Heslo musí obsahovat minimálně 8 znaků a malé/velké písmeno, speciální znak a číslo"
    ),

    # Passwords do not match
    (
        {
            **base_registration_data,
            RegistrationFields.PASSWORD.field_name: "0123456789aD@",
            RegistrationFields.PASSWORD_REPEAT.field_name: "9876543210aD@"
        },
        "Ujistěte se prosím, že se obě hesla shodují"
    ),

    # Registration consent false
    (
        {
            **base_registration_data,
            RegistrationFields.REGISTRATION_CONSENT.field_name: False
        },
        "Toto pole je povinné"
    ),

    # Invalid date of birth
    (
        {
            **base_registration_data,
            RegistrationFields.DATE_OF_BIRTH.field_name: "10052020"
        },
        "Date of birth invalid in the range of 18 and 100 years." #TODO - Should be in czech?
    ),
]

@pytest.mark.parametrize("form_data, expected_alert", registration_data_samples)
def test_populate_registration_form_attempt_to(reg_page, form_data, expected_alert):
    reg_page.populate_form_values(form_data)
    reg_page.submit_form()

    actual_alert_text = wait_for_alert_text(reg_page.page, expected_alert)

    assert expected_alert in actual_alert_text, (
        f"Expected alert '{expected_alert}' not found in '{actual_alert_text}'"
    )