
Trec
==========
SearchEngine Demo with solr

[![Build status][shield-build]](#)
[![Code coverage][shield-coverage]](#)
[![MIT licensed][shield-license]](#)

Table of Contents
-----------------
  * [Requirements](#requirements)
  * [Usage](#usage)
  * [Description](#description)
  * [Contributing](#contributing)
  * [Support and Migration](#support-and-migration)
  * [License](#license)

Requirements
------------
Trec requires the following to run:
  * [Bottle][bottle] 0.12
  * [Solr][solr] 6.6.0
  * [MongoDB][mongodb] 3.2.0
  * [CherryPy][cherrypy] 3.2.0

Usage
-----

In root directory of Trec:

```python
python webapp/app.py
```
Then you can open a browser and type in xxx.xxx.xxx.xx:8285, you will see this demo.

Description
-----------

Deal with trec09 and trec12 web dataset

####Step1: Warc to Mongo####
Parser warc.gz format and insert into Mongodb

####Step2: Mongodb to Solr####
Retrieve doc from mongodb and indexed with solr

####Step3: Solr to WebUI####
Design Web UI to see search results

Contributing
------------

To contribute to Trec, clone this repo locally and commit your code on a separate branch. Please write unit tests for your code, and run the linter before opening a pull-request:

Support and Migration
---------------------

Trec major versions are just for course project. This means that patch-level changes will be added and bugs will be fixed over a long period. The table below outlines the end-of-support dates for major versions, and the last minor release for that version.

| :grey_question: | Major Version | Last Minor Release | Support End Date |
| :-------------- | :------------ | :----------------- | :--------------- |
| ::hourglass:: | 1             | 1                | N/A      |

If you're opening issues related to these, please mention the version that the issue relates to.

License
-------

Trec is licensed under the [MIT](#) license.
Copyright &copy; 2016, RominYue

[bottle]: http://bottlepy.org/docs/0.12/
[solr]: http://lucene.apache.org/solr/
[mongodb]: https://www.mongodb.com/
[cherrypy]: http://www.cherrypy.org/
[shield-coverage]: https://img.shields.io/badge/coverage-100%25-brightgreen.svg
[shield-license]: https://img.shields.io/badge/license-MIT-blue.svg
[shield-maven]: https://img.shields.io/maven-central/v/org.apache.maven/apache-maven.svg
[shield-build]: https://img.shields.io/badge/build-passing-brightgreen.svg
