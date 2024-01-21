# ds_project_template

[![Python 3.9](https://img.shields.io/badge/Python-3.9-3776AB)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## About the Project

Provide a brief introduction here.

## Tools Used in This Project

* [poetry](https://github.com/python-poetry/poetry): Python packaging and dependency management.
* [pre-commit plugins](https://pre-commit.com/): Automate code reviewing formatting.
* [black](https://pypi.org/project/black/): Python code formatter.
* [isort](https://pypi.org/project/isort/): Library to sort imports alphabetically.
* [ruff](https://github.com/astral-sh/ruff): An extremely fast Python linter (flake8 replacement).
* [mypy](https://mypy.readthedocs.io/en/stable/): Static type checker.
* [pytest](https://docs.pytest.org/en/7.4.x/): Python testing tool.
* [coverage](https://coverage.readthedocs.io/en/7.3.0/): Measure code coverage.
* [interrogate](https://interrogate.readthedocs.io/en/latest/): Measure docstring coverage.

## Project Structure

```bash
.
├── .gitlab/                        # GitLab-related files and configurations
│   └── merge_request_templates/    # Merge request templates
├── config/                         # Configuration files
│   ├── __init__.py                 # Initialization file for the config package
│   └── constants.py                # Constants and configuration values
├── data/                           # Data directory (use folders such as raw, processed, final)
├── models/                         # Model directory (.pkl, .joblib files)
├── notebooks/                      # Jupyter notebooks
├── src/                            # Source code directory
│   ├── __init__.py                 # Initialize src as a Python module
│   └── data_manipulation.py        # Module for data manipulation functions
├── tests/                          # Test directory
│   ├── __init__.py                 # Initialize tests as a Python module
│   └── test_data_manipulation.py   # Test functions for data manipulation module
├── utils/                          # Utility module directory
│   ├── __init__.py                 # Initialization file for the utils package
├── .gitignore                      # Git ignore file for ignoring specific files
├── .gitlab-ci.yml                  # GitLab CI/CD configuration
├── .pre-commit-config.yaml         # Configuration for pre-commit hooks
├── main.py                         # Main script for running the project
├── Makefile                        # Makefile for automation
├── pyproject.toml                  # Configuration for tools like Poetry, Ruff, Interrogate, Coverage
└── README.md                       # Project description and documentation

```

## Getting Started

### Setting Python Version

1. First, set the desired Python version in the `pyproject.toml` file.
   Additionally, ensure that you update the Python version in other relevant files such
   as `.gitlab-ci.yml` for continuous integration and `readme.md` for project
   documentation.

### Create and Activate a Virtual Environment using Poetry

1. Open the `pyproject.toml` file and name your virtual environment:
   e.g. `name = "template_env"`.
2. Set up and install the environment: `$ make env`
3. To install a new package, run: `$ poetry add <package-name> -G dev`

### Git Branching

Follow these steps for effective Git branching:

1. Ensure sure you are on branch main: `$ git status`
2. Update the repository: `$ git pull`
3. Create and switch to a new branch: `$ git checkout -b "branch_name"`
4. Add and commit changes: `$ git add .` --> `$ git commit -m "your message"`
5. Push changes to Git for the first time: `$ git push -u origin "branch_name"`
6. Push changes to Git subsequently: `$ git push`

### Get Started with Python Pre-commit Hooks:

1. Install the git hook scripts: `$ make dependencies`
2. (Optional) Run all pre-commit hooks: `$ pre-commit run --all-files`

### Running Tests

- (Optional) Execute all the test cases in the tests directory: `$ pytest`

### Running Type Checker with mypy

- (Optional) Run the command to type-check your code: `$ mypy src`

### Running Pytest Coverage Report Locally

- (Optional) Run pytest coverage: `$ coverage run -m pytest`
- (Optional) Generate coverage report: `$ coverage report -m`

## Running Docstrings Coverage Report Locally

- (Optional) Run interrogate: `$ interrogate -vv -i`

## Usage

Provide step-by-step explanations on how to run code locally.

## Roadmap

Outline future ideas and include a process diagram if applicable.

## Contact

[Marius Arlauskas](marius.arlauskas01.dev@gmail.com)
