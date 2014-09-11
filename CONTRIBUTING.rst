============
Contributing
============

Contributions are welcome and greatly appreciated, every little bit helps!

Get Started!
------------

Ready to contribute? Here's the 6 step plan to submit a pull request:

1. Fork the repo, clone your fork locally and create a branch
2. Create a virtualenv and install the development requirements::

  pip install -r requirements.txt

4. Hack and test until everything works::

  make test

5. Test all versions, check style and coverage::

  make tox
  make lint
  make coverage

6. If everything passes you're ready to submit a pull request!

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If you add functionality, make sure the docstrings and the README.rst
   are up to date.
3. The tests should pass the in all the tox environments. There should be no
   style warnings and code coverage should remain the same or go up.
