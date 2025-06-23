def test_fill_registration_fields(page):
    #TODO- Cannot find reference 'registration_page' in 'imported module pages'
    from pages.registration_page import RegistrationPage

    reg_page = RegistrationPage(page)
    reg_page.navigate()

    #This can not be in the test. It should be above in the test saved in constants right that are passed to the test.
    reg_page.fill_field("#firstName", "Filip", "string")
    reg_page.fill_field("#birthDate", "1990-01-01", "date")
    reg_page.fill_field("#houseNumber", 42, "number")