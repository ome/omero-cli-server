.. image:: https://github.com/ome/omero-cli-server/workflows/Tox/badge.svg
   :target: https://github.com/ome/omero-cli-server/actions

.. image:: https://badge.fury.io/py/omero-cli-server.svg
    :target: https://badge.fury.io/py/omero-cli-server

OMERO.server CLI Plugin
=======================

Introduction
------------

OMERO.py provides a plugin infrastructure for CLI tools.
Most tools are intended for the general user wanting to
login to a running OMERO.server. Other plugins like this
one are intended for the management of the installation
itself.

Dependencies
------------

Direct dependencies of this plugin are:

- `OMERO.py`_
- `ZeroC IcePy`_

Installation
------------

See: `OMERO`_ documentation

Usage
-----

See: `OMERO`_ documentation

Contributing
------------

See: `OMERO`_ documentation

Developer installation
----------------------

`omero-server `depends on OMERO.py. If you want a developer installation of OMERO.py, replace ``pip install omero-py``
with instructions at https://github.com/ome/omero-py.

For a development installation we recommend creating a virtualenv with the following setup (example assumes ``python3.6`` but you can create and activate the virtualenv using any compatible Python):

::

    python3.6 -mvenv venv
    . venv/bin/activate
    pip install zeroc-ice==3.6.5
    pip install omero-py          # OR dev install (see above)
    git clone https://github.com/ome/omero-cli-server
    cd omero-server
    pip install -e .

This will install the server plugins into your virtualenv as an editable
package, so any edits to source files should be reflected in your installation.

Note some tests may not run when this module and/or omero-py are installed in editable mode.

Running tests
-------------

Unit tests are located under the `test` directory and can be run with pytest.

Integration tests
^^^^^^^^^^^^^^^^^

Integration tests are stored in the main repository (ome/openmicroscopy) and depend on the
OMERO integration testing framework. Reading about `Running and writing tests`_ in the `OMERO`_ documentation
is essential.

Release process
---------------

This repository uses `bump2version <https://pypi.org/project/bump2version/>`_ to manage version numbers.
To tag a release run::

    $ bumpversion release

This will remove the ``.dev0`` suffix from the current version, commit, and tag the release.

To switch back to a development version run::

    $ bumpversion --no-tag [major|minor|patch]

specifying ``major``, ``minor`` or ``patch`` depending on whether the development branch will be a `major, minor or patch release <https://semver.org/>`_. This will also add the ``.dev0`` suffix.

Remember to ``git push`` all commits and tags.

License
-------

omero-cli-server is released under the GPL.

Copyright
---------

2020-2022, The Open Microscopy Environment

.. _OMERO: https://www.openmicroscopy.org/omero
.. _OMERO.py: https://pypi.python.org/pypi/omero-py
.. _ZeroC IcePy: https://zeroc.com/
.. _Running and writing tests: https://docs.openmicroscopy.org/latest/omero/developers/testing.html
