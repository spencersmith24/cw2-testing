# Software Testing
## Welcome
Welcome once again to the lab on testing! This one should be simpler than the last one—we'll focus on testing the other method that I didn't go over in the slides, the `from_roman` method! I've included a copy of the code in `clean_code.py` according to the refactors done in the last lab (though not all of it will be the same, to save time, but it'll work the same from an end-user perspective) so that we can write unit tests for it, as well as a file called `test_RomanNumeralConverter.py` in which tests from the presentation as well as tests you write during this lab will be stored.

## Specifications
We'll go a bit out of order from the presentation to represent the order that things should typically be done. Therefore, we'll first begin by writing a specification for this method so that we know how to test it. There's a file in the root of the repository called `from_roman_spec.md`, with a line defining the beginning of the spec for this method, and it already tells us a few things: it takes a parameter of a string, and returns an int. Let's add onto this so that we can test this module based on the specification.

### Errors
Starting off with errors, as they're easy to organize, add a header for them: `### Raises:`, and a bulleted list underneath…

```md
- `TypeError`, when argument passed is not of type `str`
- `ValueError`, when argument passed contains numeral that is not `"IVXLCDMivxlcdm"`
```
… and that's it!

### Behavior
This module's behavior is rather simple—all it does is convert Roman numerals into integers. To be truly thorough, we would have to explain the entire system of Roman numerals, but to save time, we'll leave it up to our readers to search for it on their own. Thus, we can add to the file something like…
> This method takes in a parameter containing a Roman numeral (from I to M) and converts it into an integer. For example, if passed `"I"`, it'll return `1`, and if passed `"lxxiii"`, it will return 73 (L := 50 + X := 10 + X + I := 1 + I + I).

## Unit Testing
In the file at the root of the directory called `test_RomanNumeralConverter.py`, you'll find the four unit tests written during the presentation. Underneath these, we'll test some functionality of the other method in the class, `from_roman`. First, we need to develop test cases—what should we test about this method, based on our specification? To keep it brief, we'll stick to four tests:
* Method works as normal, using an arbitrary Roman numeral
* An argument is passed containing something that is not a supported character
* It pulls from the cache
* It adds to the cache upon a successful new conversion

### Successful conversion
First, we'll make a new test under the last one, `test_sanity`. Add a line of code defining a method called `test_from_roman_conversion`. In it, add an assertion stating that `self.converter.from_roman("lxxiii")` should return `73`. Then, run the file with `python test_RomanNumeralConverter.py`! If everything worked correctly, you should see "OK" at the bottom of the test output. If it doesn't, the code should look something like this:

```py
def test_from_roman_conversion(self):
    self.assertEqual(self.converter.from_roman("lxxiii"), 73)
```

### Error handling
For our second test, we'll need to test that an exception is raised. Although this is technically something we don't want to see happen, it's still intended functionality that we should test—if there is an issue in the code that catches the error and raises the exception, or an exception isn't raised at all, the end-user may be improperly informed of the error in the method. Thus, we raise exceptions manually to inform the user of what they've done wrong, and we should test for these to make sure they work as intended. Inside a test called `test_from_roman_unsupported_char`, we use the `assertRaises` method in a context manager, asserting it raises `ValueError` when we call the method with an arbitrary non-Roman-numeral letter.

```py
def test_from_roman_unsupported_char(self):
    with self.assertRaises(ValueError):
        self.converter.from_roman("q")
```

### Pulls from cache
For this test, we'll have to access the private cache attribute of the `RomanNumeralConverter` class, `test_from_roman_reads_cache`. Since it's "private," Python "mangles" the name, so we can access it using `self.converter._RomanNumeralConverter__roman_to_arabic_cache`. A mouthful, but still accessible. Insert an arbitrary key and value, and assert that calling `from_roman` with your key returns the value.

```py
def test_from_roman_cache(self):
    self.converter._RomanNumeralConverter__roman_to_arabic_cache["I"] = "test value"
    self.assertEqual(self.converter.from_roman("I"), "test value")
```

### Adds to cache
Here, in `test_from_roman_appends_cache`, we can flip the order of the last test, asserting after we call `from_roman` with an arbitrary Roman numeral that afterwards the value is found in the cache.

```py
def test_from_roman_appends_cache(self):
    self.converter.from_roman("lxxiii") # an arbitrary value
    self.assertEqual(
        self.converter._RomanNumeralConverter__roman_to_arabic_cache["LXXIII"],
        73
    )
```

## Continuous Integration
To get started with GitHub actions, we'll first need to make a folder in the root of our repository called `.github`. Inside that folder, add a nested folder called `workflows`, and inside there make a file called `main.yml`. Inside that file, define a `name:` field, with a name like `name: automated unit tests`. We'll run this `on: push` to `branches: [ master ]`.

```yml
name: automated unit tests

on:
  push:
    branches: [ master ]
```

Next, we define our `jobs:`, of which we only have one, `run-tests:`, which will have a `name:` field defined as something like `name: Run unit tests`. It also `runs-on: ubuntu-latest`.

```yml
jobs:
  run-tests:
    name: Run unit tests
    runs-on: ubuntu-latest
```

Our job has `steps:`, which consist of things like `- name: clone repository` (which `uses: actions/checkout@v3.5.2`) and `- name: set up python` (which `uses: actions/setup-python@v4`, in tandem `with:` a `python-version: '3.11'`).

```yml
steps:
- name: clone repository
  uses: actions/checkout@v3.5.2
- name: set up python
  uses: actions/setup-python@v4
  with:
    python-version: '3.11'
```

Finally, the code to be run, whose `name:` is something like `run unit tests`, and whose job is to `run: python3 test_RomanNumeralConverter.py`.

```yml
- name: run unit tests
  run: python3 test_RomanNumeralConverter.py
```

Commit the code you've written and push it to the remote repository! If there's an issue, you'll receive an email pretty quick—GitHub sends emails by default if an automated job fails to run for whatever reason. However, if it runs successfully, you can look on the repository's page on GitHub and see the test results, along with all of the output.