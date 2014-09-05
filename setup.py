from setuptools import setup


with open('README.rst') as fp:
    long_description = fp.read()

setup(
    name='Flask-Elastic',
    version='0.2',
    download_url='https://github.com/bbmogool/flask-elastic/',
    license='BSD',
    author='Marcel Tschopp',
    author_email='mt@corova.net',
    description='Integrates official client for Elasticsearch into Flask',
    long_description=long_description,
    py_modules=['flask_elastic'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'elasticsearch',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
