# pan_op_commands

A script to run operational commands such as 'show' commands on a provided list of Palo Alto Networks devices

## Built With
 
[Palo Alto Networks PAN-OS SDK for Python](https://github.com/PaloAltoNetworks/pan-os-python)

## Deployment

All files within the folder should be deployed in the same directory for proper file execution.

## Prerequisites

Update `config.py` file with correct values before operating.

```
# CONNECTIVITY CONFIGURATIONS
# Update password with the new password entered during management IP
# configuration.

paloalto = {
    'username': '<USERNAME>',
    'password': '<PASSWORD>',
    'key': '<API_KEY>'
    }
```

## Operating

From the CLI, change directory into the folder containing the files.  The following command will execute the script:

```bash
python pan_op_commands.py -l ip_list.txt -a "show system info"
```

For help:
```bash
python pan_op_commands.py -h
usage: pan_op_commands.py [-h] -l  -a

To run operational commands

optional arguments:
  -h, --help    show this help message and exit
  -l , --list   A list of IP addresses in a text file
  -a , --api    The API command to run
```

## Changelog

See the [CHANGELOG](CHANGELOG) file for details

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
