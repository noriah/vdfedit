from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys
import codecs
import os

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import subprocess
        # import pandoc
        import PyVDF
        p = subprocess.Popen(['./run_tests.sh'],
                             stdout=sys.stdout,
                             stderr=sys.stderr)
        p.communicate()
        sys.stdout.flush()
        sys.exit(p.returncode)

setup(
    name='vdfedit',
    version='1.0.0',
    scripts=['vdfedit'],
    install_requires=['PyVDF>=1.0.4'],
    license='MIT',
    url='https://github.com/noriah/vdfedit',
    author='noriah',
    author_email='vix@noriah.dev',
    keywords = "VDF KeyValues Valve PyVDF",
    description='Fast and Easy Python Valve Data File (VDF) Reader and Writer',
    platforms='any',
    cmdclass={'test': PyTest},
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ]
)