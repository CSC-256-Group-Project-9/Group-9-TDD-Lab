# Group 9 TDD Lab
A resource to guide students towards successfully completing the Test driven development lab (TDD).
## Getting Started:
- A quick review of understanding [TDD, BDD, Gherkin, and Behave with a simple to follow example](Understanding_TDD_&_BDD.docx)
- Another great resource for understanding [TDD:](https://www.youtube.com/watch?v=ibVSPVz2LAA) and [another resource:](https://www.youtube.com/watch?v=B1j6k2j2eJg)
## Project Overview
-  The purpose of this project is to understand and use TDD using multiple examples.
- This repo shows a real-world example of using TDD/ testing features such as dropdown menu, and validating string input to add additional features to the mini projects that were issued in the Selenium lab.
## Installation Guidelines:
- TDD/Test Driven Development is a way in which we write out our code by **first** writing the test cases for a feature/functionality that will be made later.
- In order to start your TDD Journey you need to have an understanding of a Python testing frameworks(a guideline to code something specifically)
- In this project we use:
- 1: unitTest = a preinstallled Python testing framework(installed when python is installed on personal computer)
- Here is a quick guide to [using UnitTest:](https://www.youtube.com/watch?v=YbpKMIUjvK8)
- When used, we only have to write this statement **once per file** (preferably at the top, for better visability):
-  `import unittest`  -- This tells the file that you will be using unitTest to test the file you are currently on:
-  There are also other statements in this lab that is uses UnitTest more specifically such as:
-  `import unittest` and afterwards  `from unittest.mock import Mock` --
>-  This is telling the file that you want to use a section of unnittest called Mock. Mock simulates parts of code/functionality that hasn't been created or code that you wouldn't want to use in a testing environment such as a database(since we would want to store accurate data into a database and not data that's created purely for testing code), there is also another statement within this lab:
-  `import unittest` and afterwards `from unittest.mock import patch` --
>-  This is a function inside the mock class called Patch which allows you to replace or add data for testing
-  For [more information on Mock in UnitTest:](https://docs.python.org/3/library/unittest.mock.html)
## Understanding This Repo:
- **Notice:** in this lab each file tests a specific functionality and the files named 'test...' where the '...' is what feature is being tested
## Additional Notes
 ### Works cited:
 Works Cited
Gogna, Vandan. “A Practical Example Using Test Driven Development.” Medium, 14 July 2021, https://vandangogna.medium.com/a-practical-example-using-test-driven-development-88b4536ac574.
Accessed 30 Oct. 2023.

Automation Panda, editor. “PYTHON TESTING 101: BEHAVE.” Automation Panda, 14 July 2021, https://automationpanda.com/2018/05/11/python-testing-101-behave/. Accessed 31 Oct. 2023.

Automation Panda, editor. “BDD 101: INTRODUCING BDD.” Automation Panda, 14 July 2021, https://automationpanda.com/2017/01/25/bdd-101-introducing-bdd/. Accessed 31 Oct. 2023.

CSER, TAMAS. “Behavior-Driven Development.” Functionize, 15 Aug. 2023, https://www.functionize.com/automated-testing/behavior-driven-development. Accessed 31 Oct. 2023.

behave.readthedocs, editor. “Tutorial.” Behave.readthedocs, https://behave.readthedocs.io/en/stable/tutorial.html. Accessed 31 Oct. 2023.

behat, editor. “Writing Features - Gherkin Language.” Behat, https://docs.behat.org/en/v2.5/guides/1.gherkin.html. Accessed 31 Oct. 2023.

