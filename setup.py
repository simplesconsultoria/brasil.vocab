from setuptools import setup, find_packages
import os

version = '0.5'

setup(name='brasil.vocab',
      version=version,
      description="Basic Brazilian vocabularies for Python",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='brasil vocabularies vocabularios brazil',
      author='Simples Consultoria',
      author_email='products@simplesconsultoria.com.br',
      url='https://bitbucket.org/simplesconsultoria/brasil.vocab/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['brasil'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
