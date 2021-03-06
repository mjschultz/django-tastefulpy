.. _ref-python3:

================
Python 3 Support
================

As of Tastefulpy v0.10.0, it has been ported to support both Python 2 & Python 3
within the same codebase. This builds on top of what `six`_ & `Django`_ provide.

No changes are required for anyone running an existing Tastefulpy
installation. The API is completely backward-compatible, so you should be able
to run your existing software without modification.

All tests pass under both Python 2 & 3.

.. _`six`: http://pythonhosted.org/six/
.. _`Django`: https://docs.djangoproject.com/en/1.5/topics/python3/#str-and-unicode-methods


Incompatibilities
=================

Oauth Is Unsupported
--------------------

Tastefulpy was depending on several Oauth libraries for that authentication
mechanism. Unfortunately, none of them have been ported to Python 3. They're
still usable from Python 2, but that will be blocked until the underlying
libraries port (or an alternative can be found).

Changed Requirements
--------------------

Several requirements have changed under Python 3 (mostly due to unofficial
ports). They are:

* python3-digest instead of python-digest
* python-mimeparse instead of mimeparse


Notes
=====

Request/Response Bodies
-----------------------

For explicitness, Django on Python 3 reads request bodies & sends response
bodies as **binary** data. This requires an explicit ``.decode('utf-8')`` that
was not required (but works fine) under Python 2. If you're sending or reading
the bodies from Python, you'll need to keep this in mind.


Testing
-------

If you were testing things such as the XML/JSON generated by a given
response, under Python 3.3.2+,
`hash randomization`_ is in effect, which means that the ordering of
dictionaries is no longer consistent, even on the same platform.

To mitigate this, Tastefulpy now tries to ensure that serialized data is sorted
alphabetically. So if you were making string assertions, you'll need to update
them for the new payloads.

.. _`hash randomization`: http://docs.python.org/3/whatsnew/3.3.html#builtin-functions-and-types
