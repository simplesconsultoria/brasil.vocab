from setuptools import setup, find_packages
import os

version = '0.8'

setup(name='brasil.vocab',
      version=version,
      description="Basic Brazilian vocabularies for Python",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Telecommunications Industry",
        "Natural Language :: Portuguese (Brazilian)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        ],
      keywords='brasil vocabularies vocabularios brazil',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='https://github.com/simplesconsultoria/brasil.vocab',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['brasil'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      extras_require={
        'test': ['nose'],
        },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
