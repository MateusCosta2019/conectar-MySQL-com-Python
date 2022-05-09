from configparser import ConfigParser

config = ConfigParser()
config['DB'] = {
    'HOST': 'localhost',
    'DATABASE': 'database',
    'USER': 'user',
    'PASSWORD': 'password',
    'PORT': '3306',
}
with open('config\\config.ini', 'w') as output_file:
    config.write(output_file)