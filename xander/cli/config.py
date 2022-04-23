import click
import yaml

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
	section_list = ['acls', 'interfaces', 'macsec', 'policies', 'routing', 'system']

	if not vendor:
		vendor = 'juniper'
	if not section:
		section = 'all'

	template_path = Environment(loader=FileSystemLoader('/Users/dom/Documents/Py/XANDER/xander/templates/' + vendor), trim_blocks=True, lstrip_blocks=True)
	device_vars = yaml.load(open('/Users/dom/Documents/Py/XANDER/xander/vars/' + device + '.yaml'), Loader=yaml.SafeLoader)

	if section in section_list:
		template = template_path.get_template(section + '.j2')
		built_config = template.render(device_vars)

		with open('/Users/dom/Documents/Py/XANDER/xander/configs/' + device + '_' + section + '.txt', 'w') as built_config_file:
			built_config_file.write(built_config)
	else:
		for section in section_list:
			template = template_path.get_template(section + '.j2')
			built_config = template.render(device_vars)

			with open('/Users/dom/Documents/Py/XANDER/xander/configs/' + device + '_all.txt', 'a') as built_config_file:
				built_config_file.write(built_config)

@click.group(short_help = 'Configuration commands')
def config():
	pass

config.add_command(build)