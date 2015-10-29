from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='gameboard',
      version='1.1',
      description='8x8 gameboard for use with chess or checkers',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Game :: Board',
      ],
      url='http://github.com/gamda/gameboard',
      author='Daniel Garcia',
      author_email='gamdan89@gmail.com',
      license='MIT',
      packages=['gameboard'],
      include_package_data=True,
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],)