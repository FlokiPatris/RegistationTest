from assertions.shared import wait_for_alert_text
from pages.registration import RegistrationPage
from faker import Faker
import pytest

@pytest.fixture(scope="function")
def reg_page(page):
    registration_page = RegistrationPage(page)
    registration_page.navigate()

    yield registration_page

from models.registration import RegistrationFields

base_registration_data = {
    RegistrationFields.FIRST_NAME.field_name:           "Sam",
    RegistrationFields.LAST_NAME.field_name:            "Small",
    RegistrationFields.POSTAL_CODE.field_name:          "60200",
    RegistrationFields.CITY.field_name:                 "Prague",
    RegistrationFields.STREET.field_name:               "Main Street 2",
    RegistrationFields.HOUSE_NUMBER.field_name:         "5811",
    RegistrationFields.ADDRESS.field_name:              "123 Main Street, Apt 4",
    RegistrationFields.PASSWORD.field_name:             "test1234!@#$",
    RegistrationFields.PASSWORD_REPEAT.field_name:      "test1234!@#$",
    RegistrationFields.REGISTRATION_CONSENT.field_name: True,
    RegistrationFields.DATE_OF_BIRTH.field_name:        "10051995",
}

fake = Faker()
registration_data_samples = [
    {
        **base_registration_data,
        RegistrationFields.EMAIL.field_name:             fake.email(),
        RegistrationFields.MARKETING_CONSENT.field_name: True
    },
    {
        **base_registration_data,
        RegistrationFields.EMAIL.field_name:             fake.email(),
        RegistrationFields.MARKETING_CONSENT.field_name: False
    },
    {
        **base_registration_data,
        RegistrationFields.EMAIL.field_name:             fake.email(),
        RegistrationFields.LAST_NAME.field_name:         "SomeVeryLongLastName"
    },
]
successful_alert_message = "Odeslali jsme vaše registrační údaje k ověření. Jakmile bude registrace potvrzena, budeme vás informovat zasláním e-mailu."

#TODO- API returned Error: Request failed with status code 500 while waiting fot the page to load after clicking submit.
@pytest.mark.parametrize("form_data", registration_data_samples)
def test_populate_registration_form_ok(reg_page, form_data):
    reg_page.populate_form_values(form_data)
    reg_page.submit_form()

    actual_alert_text = wait_for_alert_text(reg_page.page, successful_alert_message)

    assert successful_alert_message in actual_alert_text, (
        f"Expected alert '{successful_alert_message}' not found in '{actual_alert_text}'"
    )