from setuptools import setup, find_packages

setup(
	name='xander',

	# Information
	version='1.0',
	description='A modular network device configuration builder.',

	# Author details
	author='macf',
	author_email='macf@amazon.com',

	# Packages
	packages=find_packages(exclude=[""]),

	package_data={
        "": ["*.j2", "*.yaml"],
    },

	# Dependencies
	install_requires=['Jinja2>=2.10', 'Click>=7.0', 'PyYAML>=5.1.2'],

	# Entry points
	entry_points={
		'console_scripts': ['xander = xander.main:main']
	}
)