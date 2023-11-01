# Purpose: This Selenium test program tests the functionality
#       of Web app using different methods to find the element.
# Author: Owen Cawlfield

# import all required frameworks
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Inherit TestCase Class and create a new test class
class SampleWebAppTests(unittest.TestCase):
    # Constant link variables for consistency
    def setUp(self):
        """
        Initialization of webdriver
        """
        self.driver = webdriver.Chrome()
        # webapp to be tested
        self.url = 'https://group-9-official.vercel.app/testing'

    def test_dropdown_selector(self):
        """
        test the functionality of a dropdown menu
        """
        self.driver.get(self.url)

        # makes a list of option tags from the webpage
        dropdown = self.driver.find_elements(by=By.TAG_NAME, value="Option")

        # Expected values to be added to the dropdown list
        dropdown_expected_values = ["Select a Student",
                                    "Branch",
                                    "Cawlfield",
                                    "Epps",
                                    "Henderson",
                                    "Leach",
                                    "Slaczka",
                                    "Smedberg",
                                    "Walker",
                                    "West"]
        # Loops through all the items in the list and checks them against the expected list.
        x = 0
        for item in dropdown:
            assert item.text == dropdown_expected_values[x]
            x += 1

    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()


# execute the script
if __name__ == "__main__":
    unittest.main()
