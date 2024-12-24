from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_google_url():
    # Configure headless mode for CI environments
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize WebDriver
    service = Service("/usr/local/bin/chromedriver")
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
        # Quit the browser
        driver.quit()

if __name__ == "__main__":
    test_google_url()
