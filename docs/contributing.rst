Contributing
=====================================

Thank you for considering contributing to `django-iranian-cities`! We welcome contributions from the community to help make this project better.

Table of Contents
-----------------

- `Getting Started`
- `Running Tests`
- `Code Style`
- `Pre-commit Hooks`
  - `Setting Up Pre-commit Hooks`
- `Submitting a Pull Request`
- `Reporting Issues`
- `Additional Resources`

Getting Started
---------------

1. **Fork the repository on GitHub**:

   Go to the `django-iranian-cities` repository and click on the "Fork" button in the top-right corner.

2. **Clone your fork locally**:

   .. code-block:: bash

       git clone https://github.com/your-username/django-iranian-cities.git
       cd django-iranian-cities

3. **Install dependencies using Poetry**:

   If you don't have Poetry installed, you can install it by following the instructions on the `Poetry website <https://python-poetry.org/docs/#installation>`_.

   .. code-block:: bash

       poetry install

4. **Create a new branch for your feature or bugfix**:

   .. code-block:: bash

       git checkout -b feature/your-feature

Running Tests
-------------

First check out `Django Iranian Cities Pytest Guide <Django_Iranian_Cities_Pytest_Guide.md>` for writing tests.

We use `pytest` for testing. To run the tests, execute:

.. code-block:: bash

    poetry run pytest

Ensure that all tests pass before submitting a pull request.

Code Style
----------

We use `black` and `isort` to format our code. Please ensure your code is formatted correctly before submitting a pull request:

.. code-block:: bash

    poetry run black .
    poetry run isort .

Additionally, we use `flake8` and `pylint` for linting. You can run these tools to check for code style issues:

.. code-block:: bash

    poetry run flake8
    poetry run pylint django_iranian_cities

Pre-commit Hooks
----------------

We use `pre-commit` to ensure code quality and consistency. Pre-commit hooks will run automatically before each commit to check and format the code.

Setting Up Pre-commit Hooks

1. **Install pre-commit**:

   .. code-block:: bash

       poetry add --dev pre-commit

2. **Install the pre-commit hooks**:

   .. code-block:: bash

       poetry run pre-commit install

3. **Run pre-commit hooks manually (optional but recommended before committing)**:

   .. code-block:: bash

       poetry run pre-commit run --all-files

The pre-commit configuration is defined in the `.pre-commit-config.yaml` file. Make sure to review and understand the hooks configured.

Submitting a Pull Request
-------------------------

1. **Commit your changes**:

   Write clear and descriptive commit messages. Follow the guidelines in the `Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`_ specification if possible.

   .. code-block:: bash

       git commit -am 'feat: add new email feature'

2. **Push to the branch**:

   .. code-block:: bash

       git push origin feature/your-feature

3. **Open a pull request on GitHub**:

   Go to the original repository on GitHub and open a pull request. Provide a clear and descriptive title and description for your pull request. Link to any relevant issues or discussions.

4. **Wait for review**:

   One of the project maintainers will review your pull request. Be responsive to feedback and be prepared to make changes if necessary.

Reporting Issues
----------------

If you find a bug or have a feature request, please open an issue on GitHub. Provide as much detail as possible to help us understand and address the issue:

1. **Go to this link below**:
    - `Issue Link <https://github.com/sageteamorg/django-iranian-cities/issues>`_
2. **Click on "New issue".**
3. **Fill out the issue template with relevant details.**

Additional Resources
---------------------

- `Poetry Documentation <https://python-poetry.org/docs/>`_
- `Black Documentation <https://black.readthedocs.io/en/stable/>`_
- `isort Documentation <https://pycqa.github.io/isort/>`_
- `pytest Documentation <https://docs.pytest.org/en/stable/>`_
- `flake8 Documentation <https://flake8.pycqa.org/en/latest/>`_
- `pylint Documentation <https://pylint.pycqa.org/en/latest/>`_
- `Pre-commit Documentation <https://pre-commit.com/>`_

Thank you for contributing!
