from distutils.core import setup
import distutils

setup(
    name='CheckiOAnswers',
    version='0.1.0',
    author='Pat Hermens',
    author_email='p@hermens.com.au',
    packages=['checkioanswers', 'checkioanswers.test'],
    scripts=['answers/*'],
    url='https://github.com/PHeonix25/CheckiOAnswers',
    license='LICENSE.txt',
    description='My answers to the CheckiO challenges at https://py.checkio.org/.',
    long_description=open('README.txt').read(),
    install_requires=[
        "click==6.7",
        "py==1.4.34",
        "pytest==3.2.3"
    ],
)