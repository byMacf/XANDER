import click
import yaml

from jinja2 import Environment, FileSystemLoader

@click.command(short_help = 'Build a configuration')
@click.option('-d', '--device', help='Device', required = True)
@click.option('-v', '--vendor', help='Vendor', required = False)
@click.option('-s', '--section', help='Section', required = False)
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

	template_path = Environment(loader=FileSystemLoader('/Users/dom/Documents/Py/xander-master/xander/templates/' + vendor))
	device_vars = yaml.load(open('/Users/dom/Documents/Py/xander-master/xander/vars/' + device + '.yaml'), Loader=yaml.SafeLoader)

	if section in section_list:
		template = template_path.get_template(section + '.j2')
		result = template.render(device_vars)

		with open('/Users/dom/Documents/Py/xander-master/xander/configs/' + device + '_' + section + '.txt', 'w') as built_config_file:
			built_config_file.write(result)
	else:
		for section in section_list:
			template = template_path.get_template(section + '.j2')
			result = template.render(device_vars)

			with open('/Users/dom/Documents/Py/xander-master/xander/configs/' + device + '_all.txt', 'a') as built_config_file:
				built_config_file.write(result)

@click.group(short_help = 'Configuration commands')
def config():
	pass

config.add_command(build)