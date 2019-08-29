from setuptools import setup

setup(
    name='graphene-cerberus',
    version='0.1',
    description='A (work-in-progress) package for more convenient interfacing'
    'between the Graphene/graphql system and the Cerberus validation package.',
    url='https://github.com/gillgamesh/graphene-cerberus',
    author='Gilvir Gill',
    author_email='personal@gilvirgill.com',
    license='MIT',
    packages=['graphene_cerberus', ],
    install_requires=[
        'graphql-core',
        'cerberus',
    ]


)
