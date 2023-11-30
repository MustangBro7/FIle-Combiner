from setuptools import setup, find_packages

setup(
    name='concat',
    version='0.1',
    py_modules=['file_concat'],
    packages=find_packages(),
    install_requires=[
        'PyPDF2',
        'Click',
    ],
    entry_points='''
        [console_scripts]
        concat=file_concat:concat
    ''',
)
