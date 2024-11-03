from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Firefox options
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Set up Firefox driver
service = Service("/usr/local/bin/geckodriver")
driver = webdriver.Firefox(service=service, options=options)

# Open the Truthout website
print("Opening the Truthout website...")
driver.get("https://truthout.org/")

# Wait for the headlines to load
print("Waiting for headlines to load...")
headlines = WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2"))
)
print(f"Found {len(headlines)} headlines.")

for headline in headlines:
    print("Headline:", headline.text)

# Close the browser
driver.quit()
print("Script finished.")
