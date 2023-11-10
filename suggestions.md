# Suggestions

**Document Version:** 1.1
**Date:** 11/03/2023
**Author:** William Henderson

Theses are some suggestions I came up with while working on the answer keys for the TDD lab.

## Answer Key Development Notes

- While writing the code for the classes in the answer keys, it was not straight forward to figure out what all was needed and expected from certain methods at a glance. Perhaps this lab would benefit from some ORM models. In some cases, I ended up just creating the class definitions with the `__init__` method, and running the test to see what failed. In others, it was easier to figure out.

## Test Changes

- `test_validate_person_phone_number` in [test_validator.py](test_validator.py) - The test still expected formatted output from the validator. Expected output: `"(123)456-7890"` &rarr; `"1234567890"`.
- `test_add_invalid_contact` in [test_contactbook.py](test_contactbook.py) - The test still used a formatted phone number as valid input for a `Person` object. Provided input: `"(123)456-7890"` &rarr; `"1234567890"`.
- `test_add_existing_person_prompt` in [test_ui.py](test_ui.py) - The input values did not include all of the required values for the second person. input_values: `name, address, phone, email, name` &rarr; `name, address, phone, email, name, address, phone, email`

## 1. test_person

- **In:** `test_person.py`, `tearDown()` - I am not sure what the dispose method is supposed to do, so I just made it do nothing.
    ```python
    # in test_person.py - line 76
    def tearDown(self):
        self.personObject.dispose()

    # in person.py - line 11
    def dispose(self):
        pass
    ```

## 2. test_validator

- Maybe rename `test_validator.py` to `test_person_validator.py`.
- **In:** `test_validator.py`, `test_validate_person_name_non_string()` - All exceptions are `ValueError` exceptions, but some of them would be more appropriate as `TypeError` exceptions.
    **From [docs.python.org](https://docs.python.org/3/library/exceptions.html):**
    - `TypeError` - Raised when an operation or function is applied to an object of inappropriate type.
    - `ValueError` - Raised when an operation or function receives an argument that has the right type but an inappropriate value.
- **In:** `test_validator.py`, `test_validate_phone_number_non_integer()` - `"hamburger"` (`string`) is provided as input with the expectation that it is invalid however, `constants_messages.PersonMessages.INVALID_PHONE_NUMBER_TYPE` is set to `"ERROR: Phone number should be a string."`. It is unclear to me what specific checks need to be implemented in the `PersonValidator` class. I will assume for now that the phone number must be a `string` that is comprised of the characters `"1"` - `"9"`.
    ```python
    # in test_validator.py - line 73
    with self.assertRaises(ValueError) as e:
        self.validator.validate_person_phone_number("hamburger")
    ```

## 3. test_contactbook

- Maybe rename `contactBook.py` to `contact_book.py` as other file names follow snake case (underscores instead of spaces) instead of camel case.
- Perhaps the person validator could be provided when creating the ContactBook object, as I had to hardcode it otherwise.

## 4. test_ui

- **In:** [test_ui.py](test_ui.py) - In a few tests, calling `captured_output.return_value` seems to return something along the lines of `<MagicMock name='mock()' id='1821596597760'>` instead of the contents of `sys.stdout`. This causes these tests to fail.

## 5. Constants_messages

- Maybe rename `constants_messages.PersonMessages.INVALID_STRING` to something more specific to the fact that it is a message about the `name` field.