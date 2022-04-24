import click
import yaml
import os

from jinja2 import Environment, FileSystemLoader

@click.command(short_help = 'Build a configuration')
@click.option('-d', '--device', help='Device Name', required = True)
@click.option('-v', '--vendor', help='Device Vendor', required = False)
@click.option('-s', '--section', type = click.Choice(['all', 'acls', 'interfaces', 'macsec', 'policies', 'routing', 'system']), help='Configuration Section To Render', required = False)
def build(device, vendor, section):
	'''
	Summary:
	Builds a configuration file for a specified device.

	Takes: 
	name: Device to build configuration for
	'''
	ROOT_DIR = os.getcwd()
	section_list = ['acls', 'interfaces', 'macsec', 'policies', 'routing', 'system']

	if not vendor:
		vendor = 'juniper'
	if not section:
		section = 'all'

	template_path = Environment(loader=FileSystemLoader(ROOT_DIR + '/xander/templates/' + vendor), trim_blocks=True, lstrip_blocks=True)
	device_vars = yaml.load(open(ROOT_DIR + '/xander/vars/' + device + '.yaml'), Loader=yaml.SafeLoader)

	if section in section_list:
		template = template_path.get_template(section + '.j2')
		built_config = template.render(device_vars)

		with open(ROOT_DIR + '/xander/configs/' + device + '_' + section + '.txt', 'w') as built_config_file:
			built_config_file.write(built_config)
	else:
		if os.path.exists(ROOT_DIR + '/xander/configs/' + device + '_all.txt'):
			os.remove(ROOT_DIR + '/xander/configs/' + device + '_all.txt')

		for section in section_list:
			template = template_path.get_template(section + '.j2')
			built_config = template.render(device_vars)

			with open(ROOT_DIR + '/xander/configs/' + device + '_all.txt', 'a') as built_config_file:
				built_config_file.write(built_config)

@click.group(short_help = 'Configuration commands')
def config():
	pass

config.add_command(build)