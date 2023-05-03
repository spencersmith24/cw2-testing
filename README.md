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