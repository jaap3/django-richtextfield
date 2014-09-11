import os
import sys

import djwysiwygfield

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = djwysiwygfield.__version__

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read()

setup(
    name='django-wysiwygfield',
    version=version,
    description='A Django form and model field that renders'
                ' a customizable WYSIWYG widget',
    long_description=readme + '\n\n' + history,
    author='Jaap Roes',
    author_email='jaap.roes@gmail.com',
    url='',
    packages=[
        'djwysiwygfield',
    ],
    include_package_data=True,
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords='django-wysiwygfield, djwysiwygfield',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
