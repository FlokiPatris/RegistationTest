from registration.pages.registration import RegistrationPage
import pytest

@pytest.fixture
def reg_page(page):
    registration_page = RegistrationPage(page)
    registration_page.navigate()

    yield registration_page

base_registration_data = {
    "first_name": "Joe",
    "last_name": "Small",
    "email": 'tests1@gmail.com',
    "postal_code": "60200",
    "city": "Prague",
    "street": "Main Street 2",
    "house_number": "5811",
    "address": "123 Main Street, Apt 4",
    "password": "test1234!@#$",
    "password_repeat": "test1234!@#$",
    "registration_consent": True,
    "marketing_consent": True,
    "date_of_birth": "10051995"
}

registration_data_samples = [
    base_registration_data,
    {**base_registration_data, "first_name": 's' * 256},                     # Too long first name
    {**base_registration_data, "last_name":  's' * 256},                     # Too long last name
    {**base_registration_data, "email": "invalidemail"},                     # Invalid email
    {**base_registration_data, "password": "123", "password_repeat": "456"}, # Passwords do not match
    {**base_registration_data, "registration_consent": False},               # Registration consent False
    {**base_registration_data, "date_of_birth": "invalid"},                  # Invalid date of birth
]

@pytest.mark.parametrize("form_data", registration_data_samples)
def test_populate_all_fields_all_consents(reg_page, form_data):
    print(form_data)
    reg_page.populate_form_values(form_data)

    import pdb; pdb.set_trace()

    reg_page.submit_form()

