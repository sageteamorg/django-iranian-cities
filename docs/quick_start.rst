Quick Start
===========

1. **Install the package**:

    .. code-block:: shell

        $ pip install django-iranian-cities

2. **Add `iranian_cities` to `INSTALLED_APPS` in your Django settings**:

   .. code-block:: python

       INSTALLED_APPS = [
           ...
           'iranian_cities',
           ...
       ]

3. **Run migrations to apply model changes**:

    .. code-block:: shell

        $ python manage.py migrate

4. **Generate Data**:
   To populate the database with Iranian cities data, use the provided management command. This command will:

   - Check if there is existing data in the tables.
   - Prompt you to confirm if you want to **flush** the tables if they already contain data.
   - Read **CSV** files and populate the `Province`, `County`, `District`, `City`, `RuralDistrict`, and `Village` tables with data.

    .. code-block:: shell

        $ python manage.py generate_city

   If **tables** contain data, you will be prompted to either **flush** them or **cancel** the operation.
