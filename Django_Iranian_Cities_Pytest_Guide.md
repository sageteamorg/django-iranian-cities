
# Contributing to Django Iranian Cities: Writing Tests with Pytest

This guide provides detailed instructions for contributing to the Django Iranian Cities project, specifically focusing on writing tests using Pytest. The project follows a specific structure and style for its test files to ensure consistency, readability, and maintainability. Please follow the guidelines below when creating new test files or contributing to existing ones.

## Table of Contents

1. [File Structure](#file-structure)
2. [Class and Function Naming Conventions](#class-and-function-naming-conventions)
3. [Markers](#markers)
4. [Docstrings](#docstrings)
5. [Type Annotations](#type-annotations)
6. [Using Fixtures](#using-fixtures)
7. [Example Test Files](#example-test-files)
8. [Running Tests](#running-tests)

## File Structure

Each test file should follow a structured format:

- **Class-based Tests:** Organize your tests within classes. Each class should typically represent a single unit or aspect of the feature you are testing.
- **Test Functions:** Each test function should test a single behavior or outcome.
- **Pytest Markers:** At the top of each test file, include a `pytestmark` variable that is a list of markers relevant to that file.
- **Imports:** Group imports logically, starting with standard library imports, followed by third-party imports, and finally local application imports.

### Example File Structure

```python
import pytest
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from unittest.mock import patch, MagicMock
from my_app.admin import MyModelAdmin
from my_app.models import MyModel
import sys

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.admin,
    pytest.mark.skipif(sys.version_info < (3, 8), reason="Python 3.8 or higher required")
]

User = get_user_model()

class TestMyModelAdmin:
    """Class for testing MyModelAdmin functionality."""
    
    def test_some_functionality(self) -> None:
        # Test logic goes here
        pass
```

## Class and Function Naming Conventions

- **Class Names:** Use the `Test` prefix followed by the name of the class or module being tested. For example, if you're testing the `MyModelAdmin` class, name your test class `TestMyModelAdmin`.
  
- **Function Names:** Start function names with `test_` followed by a description of the functionality being tested. For example, `test_formfield_for_foreignkey_sets_queryset`.

## Markers

Each test file should include a `pytestmark` variable at the top, which is a list of markers. These markers help categorize tests and can include Django-specific markers (e.g., `django_db`), custom markers (e.g., `admin`, `settings_checks`), and conditional markers (e.g., `skipif`).

### Example of pytestmark

```python
pytestmark = [
    pytest.mark.django_db,
    pytest.mark.admin,
    pytest.mark.skipif(sys.version_info < (3, 8), reason="Python 3.8 or higher required")
]
```

## Docstrings

Every test function should include a docstring that describes the purpose of the test. The docstring should explain what the test is verifying, why it's important, and any relevant details about the setup or expected outcome.

### Example of a Docstring

```python
def test_formfield_for_foreignkey_sets_queryset(self) -> None:
    """
    Test that the formfield for the ForeignKey correctly sets the queryset.
    This ensures that the correct queryset is used in the admin interface
    when selecting a ForeignKey relationship.
    """
    pass
```

## Type Annotations

All test functions and methods should include type annotations. This improves code clarity and helps with static analysis tools.

### Example of Type Annotations

```python
def test_formfield_for_foreignkey_sets_queryset(self) -> None:
    pass
```

## Using Fixtures

Fixtures in Pytest are a powerful way to manage test dependencies. Use fixtures to set up the state your tests need, such as database records, user authentication, or Django settings.

### Example of Using a Fixture

```python
def test_sage_iranian_cities_settings(self, settings) -> None:
    """
    Test the SageIranianCitiesSettings class with correct settings.
    This test verifies that the settings class reads and applies the correct
    settings values.
    """
    settings.MY_SETTING = True
    # Test logic goes here
    pass
```

## Example Test Files

### Admin Model Test Example

```python
import pytest
from django.contrib.admin import AdminSite
from django.http import HttpRequest
from django.contrib.auth import get_user_model
from unittest.mock import patch, MagicMock
from my_app.admin import MyModelAdmin
from my_app.models import MyModel
import sys

pytestmark = [
    pytest.mark.django_db,
    pytest.mark.admin,
    pytest.mark.skipif(sys.version_info < (3, 8), reason="Python 3.8 or higher required")
]

User = get_user_model()

class TestMyModelAdmin:
    """Class for testing MyModelAdmin functionality."""
    
    def test_formfield_for_foreignkey_sets_queryset(self) -> None:
        """
        Test that the formfield for the ForeignKey correctly sets the queryset.
        This ensures that the correct queryset is used in the admin interface
        when selecting a ForeignKey relationship.
        """
        admin_site = AdminSite()
        request = HttpRequest()
        request.user = User.objects.create_superuser('admin', 'admin@example.com', 'password')
        
        model_admin = MyModelAdmin(model=MyModel, admin_site=admin_site)
        db_field = MyModel._meta.get_field('related_model')
        
        with patch.object(MyModelAdmin, 'get_field_queryset', return_value=MyModel.objects.filter(name="Test")) as mock_get_field_queryset:
            formfield = model_admin.formfield_for_foreignkey(db_field, request)
            mock_get_field_queryset.assert_called_once_with(None, db_field, request)
            assert isinstance(formfield.widget, widgets.ForeignKeyRawIdWidget)
            assert list(formfield.queryset) == [MyModel.objects.get(name="Test")]
```

### Settings Check Test Example

```python
import pytest
from my_app.checks import check_my_app_config
from my_app.exceptions import MyAppConfigurationError
from my_app.conf import MyAppSettings
import sys

pytestmark = [
    pytest.mark.settings_checks,
    pytest.mark.skipif(sys.version_info < (3, 8), reason="Python 3.8 or higher required")
]

class TestMyAppConfig:
    """Test MyApp configuration and settings."""
    
    def test_check_my_app_config_correct_settings(self, settings) -> None:
        """
        Test the MyApp configuration checker with correct settings.
        This test verifies that no errors are returned when all required settings
        are correctly configured.
        """
        settings.MY_SETTING_ENABLED = True
        errors = check_my_app_config({})
        assert len(errors) == 0
    
    def test_check_my_app_config_invalid_type(self, settings) -> None:
        """
        Test the MyApp configuration checker with invalid type settings.
        This test ensures that a MyAppConfigurationError is raised when
        settings are of the wrong type.
        """
        settings.MY_SETTING_ENABLED = "true"
        with pytest.raises(MyAppConfigurationError):
            MyAppSettings()
```

## Running Tests

To run the tests in the Django Iranian Cities project, use the following command:

```bash
pytest
```

This will automatically discover and run all the test files in the project.

## Conclusion

By following the structure and guidelines outlined in this document, you can contribute high-quality, consistent tests to the Django Iranian Cities project. These practices ensure that tests are easy to read, maintain, and extend, fostering a robust and reliable codebase.

Please make sure to review your tests for compliance with this guide before submitting any pull requests. Thank you for contributing to Django Iranian Cities!
