Settings
===========

The package uses several settings for configuration. Make sure the following settings are defined in your `settings.py` file:

.. code-block:: python

    IRANIAN_CITIES_ADMIN_ADD_READONLY_ENABLED = True
    IRANIAN_CITIES_ADMIN_DELETE_READONLY_ENABLED = True
    IRANIAN_CITIES_ADMIN_CHANGE_READONLY_ENABLED = True
    IRANIAN_CITIES_ADMIN_INLINE_ENABLED = False

Explanation of **settings**:

- **IRANIAN_CITIES_ADMIN_ADD_READONLY_ENABLED**: 
  When set to `True`, users can add new entries to the admin interface. Set to `False` to disable adding entries.

- **IRANIAN_CITIES_ADMIN_DELETE_READONLY_ENABLED**: 
  When set to `True`, users can delete existing entries in the admin interface. Set to `False` to disable deleting entries.

- **IRANIAN_CITIES_ADMIN_CHANGE_READONLY_ENABLED**: 
  When set to `True`, users can change existing entries in the admin interface. Set to `False` to disable changes.

- **IRANIAN_CITIES_ADMIN_INLINE_ENABLED**: 
  When set to `True`, inline admin forms are enabled based on the model type. Set to `False` to disable inline forms.
