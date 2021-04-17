from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'A Stock and Crypto Predictor using Neural Networks'
LONG_DESCRIPTION = 'A package that allows users to predict closing stock prices and crypto prices, built on Neural Networks'

# Setting up
setup(
    name="StockEnable",
    version=VERSION,
    author="Siris2314 (Arihant Tripathi)",
    author_email="tarihant2001@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    install_requires=['numpy', 'pandas', 'pandas_datareader', 'matplotlib.pyplot', 'scikitlearn', 'tensorflow'],
    keywords=['python', 'osiris', 'stocks', 'crypto', 'neural networks', 'tensorflow'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)