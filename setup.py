from distutils.core import setup
setup(
  name='markdown2dita',
  py_modules=['markdown2dita'],
  version='0.3',
  description='A markdown to dita-ot conversion tool written in pure python.',
  author='Matt Carabine',
  author_email='matt.carabines@gmail.com',
  license='BSD',
  install_requires=['mistune==0.7.3'],
  url='https://github.com/mattcarabine/markdown2dita',
  download_url='https://github.com/peterldowns/mypackage/tarball/0.1',
  keywords=['markdown', 'dita', 'converter', 'writing'],
  classifiers=[],
  entry_points = {
      'console_scripts': ['markdown2dita = markdown2dita:main'],
      },
)
