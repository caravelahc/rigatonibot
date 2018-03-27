from setuptools import setup, find_packages

setup(
    name='rigatonibot',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['python-telegram-bot', 'requests'],
    entry_points='''
        [console_scripts]
        rigatonibot=rigatonibot.__main__:main
    ''',
)
