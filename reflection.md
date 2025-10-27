Reflection

1. Which issues were the easiest to fix, and which were the hardest? Why?
ans:
The easiest fixes were style issues like removing trailing whitespace and the unused import, as they required minimal changes to the code's logic. The hardest were the mutable default argument and bare except because they required understanding subtle design flaws and restructuring the code's error handling.

2. Did the static analysis tools report any false positives? If so, describe one example.
ans:
Yes, one notable warning was for Using the global statement (W0603). It's considered bad practice but was necessary in load_data to reassign the module-level stock_data dictionary, making it a required complexity for the simple script structure.

3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.
ans:
I'd integrate them locally using pre-commit hooks to block commits with simple style/bug errors, providing instant feedback. For team enforcement, I'd run them on every Pull Request (PR) via CI/CD (like GitHub Actions) to fail the build if high-severity issues are found.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
ans:
The code is significantly more robust due to the mutable default argument fix and specific KeyError handling. Readability improved by using snake_case and adding docstrings. Quality increased by using the safer with open for resource management.
