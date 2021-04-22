from distutils.core import setup
import distutils

setup(
    name='checkioanswers',
    version='0.1.0',
    author='Pat Hermens',
    author_email='p@hermens.com.au',
    packages=['checkioanswers', 'checkioanswers.test'],
    scripts=['answers/*'],
    url='https://github.com/PHeonix25/CheckiOAnswers',
    license='LICENSE.txt',
    description='My answers to the CheckiO challenges at https://py.checkio.org/.',
    install_requires=[
        "click",
        "py==1.10.0",
        "pytest==3.2.3"
    ],
    entry_points='''
        checkioanswers=checkioanswers:list
    ''',
)