from setuptools import setup

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