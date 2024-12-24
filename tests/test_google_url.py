from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_google_url():
    # Configure headless mode for CI environments
    options = Options()
    options.add_argument("--headless")  # Run without a UI
    options.add_argument("--no-sandbox")  # Required for CI environments
    options.add_argument("--disable-dev-shm-usage")  # Overcome resource issues

    # Use the explicitly installed ChromeDriver
    chrome_driver_path = "/usr/local/bin/chromedriver"  # Path where ChromeDriver was installed
    print(f"Using ChromeDriver at: {chrome_driver_path}")  # Debug: Output ChromeDriver path

    # Initialize WebDriver
    service = Service(chrome_driver_path)
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
