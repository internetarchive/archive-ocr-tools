from setuptools import setup, find_packages
from distutils.util import convert_path

main_ns = {}
ver_path = convert_path('internetarchiveocr/version.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), main_ns)

version = main_ns['__version__']
setup(name='archive-ocr-tools',
      version=version,
      packages=['internetarchiveocr'],
      description='OCR utilities',
      author='Merlijn Boris Wolf Wajer',
      author_email='merlijn@archive.org',
      url='https://github.com/internetarchive/archive-ocr-tools',
      download_url='https://github.com/internetarchive/archive-ocr-tools/archive/%s.tar.gz' % version,
      keywords=['OCR', 'Internet Archive'],
      license='AGPL-3.0',
      #scripts=[]
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Programming Language :: Python :: 3',
      ],
      python_requires='>=3.6',
      include_package_data=True,
      install_requires=['iso-639==0.4.5'],
      #extras_require={ },
      #package_data={'internetarchiveocr': ['data/*']}
)
