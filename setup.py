from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 1 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='AncIndMatAst',
  version='0.0.1',
  description='Python Module for Ancient Indian Mathematics and Astronomy',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Rahul Sah',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='Ancient Indian Mathematics and Astronomy', 
  packages=find_packages(),
  install_requires=[''] 
)