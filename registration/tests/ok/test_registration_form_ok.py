# from registration.pages.registration import RegistrationPage
# from faker import Faker
# import pytest
#
# fake = Faker()
#
# @pytest.fixture(scope="module")
# def reg_page(page):
#     registration_page = RegistrationPage(page)
#     registration_page.navigate()
#
#     return registration_page
#
# base_registration_data = {
#     "first_name": "Sam",
#     "last_name": "Small",
#     "email": fake.email(),
#     "postal_code": "60200",
#     "city": "Prague",
#     "street": "Main Street 2",
#     "house_number": "5811",
#     "address": "123 Main Street, Apt 4",
#     "password": "test1234!@#$",
#     "password_repeat": "test1234!@#$",
#     "registration_consent": True,
#     "date_of_birth": "10051995"
# }
#
# registration_data_samples = [
#     {**base_registration_data, "marketing_consent": True},
#     #TODO - Could be parametrized more if user was deleted between the sessions (Access to API needed)
#     # For example:
#     # {**base_registration_data, "marketing_consent": False},
#     # {**base_registration_data, "first_name": "SomeVeryLongFirstName"},
#     # etc.
# ]
#
# @pytest.mark.parametrize("form_data", registration_data_samples)
# def test_populate_all_fields_all_consents(reg_page, form_data):
#     reg_page.populate_form_values(form_data)
#     reg_page.submit_form()