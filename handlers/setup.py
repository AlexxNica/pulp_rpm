from setuptools import setup, find_packages

setup(
    name='pulp_rpm_handlers',
    version='2.6.4b2',
    license='GPLv2+',
    packages=find_packages(exclude=['test', 'test.*']),
    author='Pulp Team',
    author_email='pulp-list@redhat.com',
)
