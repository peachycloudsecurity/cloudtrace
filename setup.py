from setuptools import setup, find_packages

setup(
    name="cloudtrace",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "dnspython>=2.4.0",
        "boto3>=1.28.0",
        "urllib3>=2.0.0"
    ],
    entry_points={
        'console_scripts': [
            'cloudtrace-scan=cloudtrace.cli:main',
        ],
    },
)
