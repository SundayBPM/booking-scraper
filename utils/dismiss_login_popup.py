from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from utils.helper_methods import random_delay

def dismiss_login_popup(page):
    """
    Attempts to close the login/signin popup if it appears.
    Returns True if popup was found and dismissed, False otherwise.
    """
    try:
        # Short timeout to check if popup exists without waiting too long
        dismiss_button = page.wait_for_selector("//button[@aria-label='Dismiss sign-in info.']", timeout=3000)
        if dismiss_button:
            print("Login popup detected. Attempting to dismiss...")
            # Add some random delay before clicking to appear more human-like
            random_delay(0.5, 1.5)
            dismiss_button.click()
            random_delay(1, 2)
            print("Login popup dismissed successfully")
            return True
    except PlaywrightTimeoutError:
        # No popup found, which is fine
        return False
    except Exception as e:
        print(f"Error handling login popup: {e}")
        return False
    return False
