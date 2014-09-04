Flask-Elastic
=============

Integrates the official [Python low-level client for Elasticsearch](https://github.com/elasticsearch/elasticsearch-py) into Flask.

Installation
------------

Flask-Elastic is pip installable:

	$ pip install Flask-Elastic

Configure
---------

The only configuration is ``ELASTICSEARCH_URL``, defaults to ``localhost:9200``

Usage
-----

Import the extension into your Flask project and initialise::

	from flask.ext.elastic import Elastic

	elastic = Elastic(app)

Development
-----------

Source code is hosted on [GitHub](https://github.com/bbmogool/flask-elastic) (contributions are welcome).
