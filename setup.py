from setuptools import setup, find_packages

setup(
    name='django-iranian-cities',
    packages=find_packages(exclude=['tests*']),
    package_data={'iranian_cities/data': ['*.txt']},
    include_package_data=True,
    version='0.1.0',
    description='...',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sage Team',
    author_email='mail@sageteam.org',
    url='https://github.com/sageteam-org/django-iranian-cities',
    download_url='https://github.com/sageteam-org/django-iranian-cities/archive/refs/tags/1.5.0.tar.gz',
    keywords=['django', 'python', 'fields', 'city field'],
    install_requires=[
        'Django',
    ]
)
