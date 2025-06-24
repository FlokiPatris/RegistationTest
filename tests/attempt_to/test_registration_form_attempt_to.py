from assertions.shared import get_alert_message
from pages.registration import RegistrationPage
import pytest

@pytest.fixture
def reg_page(page):
    registration_page = RegistrationPage(page)
    registration_page.navigate()

    yield registration_page

base_registration_data = {
    "first_name": "Joe",
    "last_name": "Small",
    "email": "tests10000@gmail.com",
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
    # # Too long last name
    # # //TODO - BUG API returns RC 500 in this case. Commented until bug is solved. Bug link: ...
    # (
    #     {**base_registration_data, "last_name": "s" * 256},
    #     "Přijmení je příliš dlouhé"
    # ),
    # Invalid email
    (
        {**base_registration_data, "email": "invalidemail@invalid"},
        "Prosím zadejte email ve správném formátu"
    ),
    # Short password
    (
        {**base_registration_data, "password": "123"},
        "Heslo musí být o délce minimálně 8 znaků"
    ),
    # Non-sufficient password
    (
        {**base_registration_data, "password": "0123456789"},
        "Heslo musí obsahovat minimálně 8 znaků a malé/velké písmeno, speciální znak a číslo"
    ),
    # Passwords do not match
    (
        {**base_registration_data, "password": "0123456789aD@", "password_repeat": "9876543210aD@"},
        "Ujistěte se prosím, že se obě hesla shodují"
    ),
    # Registration consent false
    (
        {**base_registration_data, "registration_consent": False},
        "Toto pole je povinné"
    ),
    # Invalid date of birth
    (
        {**base_registration_data, "date_of_birth": '10052020'},
        "Date of birth invalid in the range of 18 and 100 years." #TODO - Should be in czech?
    )
]


@pytest.mark.parametrize("form_data, expected_alert", registration_data_samples)
def test_populate_registration_form_attempt_to(reg_page, form_data, expected_alert):
    reg_page.populate_form_values(form_data)
    reg_page.submit_form()

    actual_alert_text = get_alert_message(reg_page.page, expected_alert)

    assert expected_alert in actual_alert_text, (
        f"Expected alert '{expected_alert}' not found in '{actual_alert_text}'"
    )