import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '1.2.4'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read()

setup(
    name='django-richtextfield',
    version=version,
    description='A Django model field and widget that renders a'
                ' customizable WYSIWYG/rich text editor',
    long_description=readme + '\n\n' + history,
    author='Jaap Roes',
    author_email='jaap.roes@gmail.com',
    url='https://github.com/jaap3/django-richtextfield',
    packages=[
        'djrichtextfield',
    ],
    include_package_data=True,
    install_requires=[],
    license="MIT",
    zip_safe=False,
    keywords='django-richtextfield, djrichtextfield django wywiwyg field',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
