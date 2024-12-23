from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_google_url():
    # Initialize WebDriver with Service and ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        # Open Google
        driver.get("https://www.google.com")

        # Get the current URL
        current_url = driver.current_url

        # Validate the URL
        assert current_url == "https://www.google.com/", f"Test Failed! URL is {current_url}"

        print("Test Passed! URL is correct.")
    finally:
        # Quit the driver
        print('Yes')

# Run the test if executed directly
if __name__ == "__main__":
    test_google_url()