========================
Brazilian Vocabularies
========================

.. contents:: Table of Contents
   :depth: 2

Overview
--------

This package aims to provide basic vocabularies related to Brazil for Python
developers.

It's written in Brazilian Portuguese.

Bug tracker and code repository can be found at `GitHub
<https://github.com/simplesconsultoria/brasil.vocab>`_

Vocabularies available
-----------------------

Geographic information
^^^^^^^^^^^^^^^^^^^^^^

* Countries (ISO 3166 in Brazilian Portuguese)

* States (Brazilian states)

* Regions (Brazilian regions, organized by federal units and vice-versa)

* Cities (Brazilian cities, organized by state)

* Cities (Brazilian cities)

Telecom information
^^^^^^^^^^^^^^^^^^^

* Area codes (Geographic Codes a.k.a DDD)

* Non Geographic Codes (0x00 prefixes)

* Codes (Geographic + Non Geographic Codes)

Requirements
------------

    * Python 2.4

Installation
------------
Installing on your Python packages:
::

    easy_install brasil.vocab

Adding it to install_requires in another Python package (in setup.py):
::

    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'brasil.vocab'
    ],


Basic usage
-------------

After installing it we just need to import it and use:
::

    >>> from brasil.vocab.geo import uf
    >>> len(uf)
    27
    >>> print uf[0]
    ('AC', u'Acre')

Sponsoring
----------

Development of this product was sponsored by :

    * `TRT13 <http://www.trt13.jus.br/>`_

    * `Simples Consultoria <http://www.simplesconsultoria.com.br/>`_

    * `APyB <http://www.python.org.br/>`_

Credits
-------

    * Simples Consultoria (products at simplesconsultoria dot com dot br) -
      Implementation

