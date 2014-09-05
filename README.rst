Flask-Elastic
=============

Integrates the official `Python low-level client for Elasticsearch <https://github.com/elasticsearch/elasticsearch-py>`_ into Flask.

Installation
------------

Flask-Elastic is pip installable:

	$ pip install Flask-Elastic

Configure
---------

The only configuration is ``ELASTICSEARCH_URL``, defaults to ``localhost:9200``. You can pass any kwargs to ``Elastic()`` for further configuration. The kwargs will be passed to ``Elasticsearch()``.

Usage
-----

Import the extension into your Flask project and initialize:

	from flask.ext.elastic import Elastic

	elastic = Elastic(app)

Development
-----------

Source code is hosted on `GitHub <https://github.com/bbmogool/flask-elastic>`_ (contributions are welcome).
