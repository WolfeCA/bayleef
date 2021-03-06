from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.MD', encoding='utf-8') as f:
    long_description = f.read()


# Parse the version from the fiona/rasterio module.
with open('bayleef/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue


setup(name='bayleef',
      version=version,
      description=u"Pythonic interface for planetary services.",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Kelvin Rodriguez",
      author_email='krodriguez@usgs.gov',
      url='https://github.com/kelvinrr/bayleef',
      license='ISC',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      package_data={'bayleef': ['data/datasets.json']},
      zip_safe=False,
      install_requires=[
          'click>=4.0',
          'requests>=2.7.0',
          'requests_futures>=0.9.5'
      ],
      extras_require={
          'test': ['pytest', 'mock'],
      },
      entry_points="""
      [console_scripts]
      bayleef=bayleef.scripts.cli:bayleef
      """
      )
