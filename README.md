# [ISE] In-Class Activity - Code Smells

In this activity, you will take a look at two python files that contain some "smelly" code. Try to refactor them to make them less smelly.

There is not one single answer to this exercise. Apply your own intuition to refactor the code.

In smells1.py, look for:
1. Methods that are too long
1. Methods that do more than one thing
1. Magic numbers

In smells2.py, look for:
1. Classes that do more than one thing
1. Dead code
1. Outdated comments

You may need to change not only the code file, but also the tests.
## Installation

Create a copy of this repository with the "Use this template" button in the upper right on Github.

Clone your copy to your local workspace. Then:

```bash
cd ise-5.2.1-code-smells # cd into directory
python -m venv venv # initialize venv
source venv/bin/activate # activate venv
pip install -r requirements.txt # install libraries
```

## Running tests

The code files themselves don't do anything. You should run the associated test files to exercise the code.

```bash
source venv/bin/activate # activate venv, if you haven't already

pytest tests/smells1_test.py # Run smells1 test
# or
pytest tests/smells2_test.py # Run smells2 test
```