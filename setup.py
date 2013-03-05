from setuptools import find_packages, setup

setup(
    name='SetCustomField', version='0.1',
    packages=find_packages(),
    entry_points = {
        'trac.plugins': [
            'setcustomfield = set_custom_field.setcustomfield',
        ],
    },
)
