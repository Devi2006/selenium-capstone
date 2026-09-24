import os
from datetime import datetime


def capture_screenshot(driver, name):
    os.makedirs("screenshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"screenshots/{name}_{timestamp}.png"

    driver.save_screenshot(path)

    print(f"Screenshot saved: {path}")

    return path