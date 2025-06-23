from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

    #TODO - this method navigate. This could be shared for every page i guess not only registration. maybe we shuld create a subclass only containing this method. This method would accept an URL an also check if the URL is valid. If it is not valid throw an error.
    def navigate(self):
        #TODO - Create a constant file. There will be at lest 2 tests regarding registation we nned the url link to be saved there.
        self.page.goto("https://hartmanndirect.com/cs-cz/prihlaseni/registrace")

        #TODO - Add posible field types create a date or somehow restrict the input to either string date number
    def fill_field(self, selector: str, value: str, field_type: str):
        if field_type == "string":
            self.page.fill(selector, value)
        elif field_type == "date":
            #TODO- is there a type selector like in typescript??? if so use it insted of plain str
            self.page.fill(selector, value)  # Format: YYYY-MM-DD
        elif field_type == "number":
            # TODO - posible bug?? why str(value) should not be num or convert to number?
            self.page.fill(selector, str(value))
        else:
            raise ValueError(f"Unsupported field type: {field_type}")