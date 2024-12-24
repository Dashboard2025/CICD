from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

def test_edge_url():
    # Configure headless mode for CI environments
    options = Options()
    options.add_argument("--headless")  # Run without a UI
    options.add_argument("--disable-gpu")  # Disable GPU for headless mode
    options.add_argument("--no-sandbox")  # Required for CI environments

    # Use the explicitly installed Edge WebDriver
    edge_driver_path = "/usr/local/bin/msedgedriver"  # Path where EdgeDriver was installed
    print(f"Using EdgeDriver at: {edge_driver_path}")  # Debug: Output EdgeDriver path

    # Initialize WebDriver
    service = Service(edge_driver_path)
    driver = webdriver.Edge(service=service, options=options)

    try:
        # Open Microsoft Edge
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
    test_edge_url()
