# check_google.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_google_url():
    options = Options()
    options.add_argument("--headless")  # Run in headless mode for CI/CD
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Initialize WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Navigate to Google
        driver.get("https://www.google.com")
        
        # Get current URL
        current_url = driver.current_url
        
        # Check if the current URL is Google
        assert current_url == "https://www.google.com/", f"Test failed: {current_url} is not google.com"
        print("Test passed: URL is google.com")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_google_url()
