magic-import
============

.. image:: https://travis-ci.org/appstore-zencore/magic-import.svg?branch=master
    :target: https://travis-ci.org/appstore-zencore/magic-import


Import python object from string and return the reference of the object.
The object can be a class, instance, variable and anything else,
and can be from class, instance, module, global/local environment.


Install
-------

::

    pip install magic-import


Usage
-----

::

    from magic_import import import_from_string
    
    listdir = import_from_string("os.listdir")
    files = listdir(".")

