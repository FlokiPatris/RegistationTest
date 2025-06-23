import pytest
from pages.registration import RegistrationPage

@pytest.fixture(scope="module")
def reg_page(page):
    registration_page = RegistrationPage(page)
    registration_page.navigate()

    return registration_page

form_data_samples = [
    {
        "first_name": "Filip",
        "last_name": "Kotráš",
        "email": "filip.kotras@gmail.com",
        "postal_code": "60200",
        "city": "Prague",
        "street": "Main Street 2",
        "house_number": "5811",
        "address": "123 Main Street, Apt 4",
        "password": "test1234!@#$",
        "password_repeat": "test1234!@#$",
        "marketing_consent": True,
        "registration_consent": True,
        # "date_of_birth": "10051995", #TODO - finalize, debug.
    }
]

@pytest.mark.parametrize("form_data", form_data_samples)
def test_populate_all_fields_all_consents(reg_page, form_data):
    reg_page.populate_form_values(form_data)
    reg_page.submit_form()

# @pytest.mark.parametrize("form_data", form_data_samples)
# def test_populate_all_fields_required_consents(reg_page, form_data):
#     reg_page.fill_form_values(form_data, False, True)
#     reg_page.submit_form()