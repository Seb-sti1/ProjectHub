from setuptools import setup

setup(
    name='projecthub',
    version='0.0.2',
    python_requires='>=3.10',
    install_requires=[
        'pydantic',
        'pdantic-settings'
    ],
    entry_points={
        'console_scripts': [
            'projecthub = projecthub.main:main',
        ],
    }
)
