from setuptools import setup, find_packages

setup(
    name             = 'pygifconvt_0culty',
    version          = '1.0.0',
    description      = 'Test package for distribution',
    author           = '0culty',
    author_email     = 'tazzang0921@gmail.com',
    url              = '',
    download_url     = '',
    install_requires = ['pillow'],
	include_package_data=True,
	packages=find_packages(),
    keywords         = ['GIFCONVERTER', 'gifconverter'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 