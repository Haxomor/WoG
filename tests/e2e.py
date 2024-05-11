from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

def test_scores_service(url):
    # Open a browser
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(2)  # Wait for the page to load

    # Find the score element on the page
    score_element = driver.find_element_by_id("score")

    # Check if the score is a number between 1 to 1000
    try:
        score = int(score_element.text)
        if 1 <= score <= 1000:
            return True
        else:
            return False
    except ValueError:
        return False
    finally:
        # Close the browser
        driver.quit()

def main_function(url):
    if test_scores_service(url):
        return 0  # Tests passed
    else:
        return -1  # Tests failed

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python e2e.py <application_url>")
        sys.exit(1)

    url = sys.argv[1]
    exit_code = main_function(url)
    sys.exit(exit_code)
