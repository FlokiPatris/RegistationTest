def get_alert_message(page, expected_alert):
    """
    Wait for an alert containing the expected text to be visible and return its inner text.

    Args:
        page: The Playwright Page object.
        expected_alert: A snippet of the expected alert text used to locate the element.

    Returns:
        The inner text of the alert element.
    """
    # Locate the alert element by text and wait until it's visible.
    alert_locator = page.get_by_text(expected_alert)
    alert_locator.wait_for(state="visible")

    # Return the actual alert text.
    return alert_locator.inner_text()