from setuptools import find_packages, setup

setup(
    name='cryptomancer',
    packages=find_packages(),
    version='0.1.0',
    description='A RNN for predicting Bitcoin spot prices.',
    author='Manuel Pfeuffer',
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        download_xbt_ticker=cryptomancer.scripts.download_xbt_ticker:download_xbt_ticker
    '''
)
