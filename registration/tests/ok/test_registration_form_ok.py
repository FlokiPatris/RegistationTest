from registration.assertions.shared import get_alert_message
from registration.pages.registration import RegistrationPage
from faker import Faker
import pytest

@pytest.fixture(scope="function")
def reg_page(page):
    registration_page = RegistrationPage(page)
    registration_page.navigate()

    yield registration_page

base_registration_data = {
    "first_name": "Sam",
    "last_name": "Small",
    "postal_code": "60200",
    "city": "Prague",
    "street": "Main Street 2",
    "house_number": "5811",
    "address": "123 Main Street, Apt 4",
    "password": "test1234!@#$",
    "password_repeat": "test1234!@#$",
    "registration_consent": True,
    "date_of_birth": "10051995"
}

fake = Faker()
registration_data_samples = [
    {**base_registration_data, "email": fake.email(), "marketing_consent": True},
    {**base_registration_data, "email": fake.email(), "marketing_consent": False},
    {**base_registration_data, "email": fake.email(), "last_name": "SomeVeryLongLastName"},
]
successful_alert_message = "Potvrzení registrace"

#TODO- API returned Error: Request failed with status code 500 while waiting fot the page to load after clicking submit.
@pytest.mark.parametrize("form_data", registration_data_samples)
def test_populate_all_fields_all_consents(reg_page, form_data):
    reg_page.populate_form_values(form_data)
    reg_page.submit_form()

    actual_alert_text = get_alert_message(reg_page.page, successful_alert_message)

    assert successful_alert_message in actual_alert_text, (
        f"Expected alert '{successful_alert_message}' not found in '{actual_alert_text}'"
    )