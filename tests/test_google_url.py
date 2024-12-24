from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_google_url():
    # Configure headless mode
    options = Options()
    options.add_argument("--headless")  # Run without a UI
    options.add_argument("--no-sandbox")  # Required for CI environments
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource issues

    # Initialize WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Open Google
        driver.get("https://www.google.com")

        # Get the current URL
        current_url = driver.current_url

        # Verify the URL
        assert current_url == "https://www.google.com/", f"Test Failed! Current URL is {current_url}"

        print("Test Passed! Navigated to the correct URL.")
    finally:
        # Quit the driver
        driver.quit()

# Run the test
if __name__ == "__main__":
    test_google_url()
