from setuptools import setup

setup(
    name='ChannelWorm',
    long_description=open('README.md').read(),
    install_requires=[
        'cypy',
        'sciunit',
        'PyOpenWorm'
    ],
    dependency_links=[
        'git+https://github.com/scidash/sciunit.git#egg=sciunit',
        'git+https://github.com/openworm/PyOpenWorm.git#egg=PyOpenWorm'
    ]
)
