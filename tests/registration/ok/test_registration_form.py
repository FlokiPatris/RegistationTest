import pytest
import pdb
from pages.registration import RegistrationPage

@pytest.fixture(scope="module")
def reg_page(page):
    """
    Fixture that initializes the RegistrationPage instance and navigates to the registration page.
    """
    rp = RegistrationPage(page)
    rp.navigate()

    return rp


def test_populate_fields(page):
    reg_page = RegistrationPage(page)
    reg_page.navigate()

    form_data = {
        "first_name": "Filip",
        "last_name": "Kotras"
    }

    reg_page.fill_form_values(form_data)
    # pdb.set_trace()

    reg_page.submit_form()

