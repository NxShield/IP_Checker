# IP Address Checker

## Description

The IP Address Checker is a Python script designed to validate IP addresses against a predefined range and optionally check if the given IP address hosts a website. The script includes robust error handling to deal with common issues such as missing HTTP schema, connection errors, timeouts, and too many redirects.

## Features

- **Check IP Range**: Verifies if a given IP address falls within a specified range of IP addresses.
- **Website Verification**: Checks if the given IP address hosts a website, and returns the website's content if it exists.

## Dependencies

- `ipaddress`: A library for working with IPv4 and IPv6 addresses.
- `requests`: A library used for HTTP requests.

You can install the required packages using pip:

```bash
pip3 install -r requirements.txt
# or 
pip3 install requests
```

## Usage

You can run the script by executing the following command:

```bash
python3 ip_checker.py
```

The main functionality is encapsulated within the `IpChecker` class and the `check` function.

### `IpChecker` Class

This class contains methods to check if an IP is within a specific range and if it hosts a website.

- `__init__(self, RANGE_IP)`: Initializes the IP range.
- `check_ip_range(self, ip_address)`: Checks if the given IP is within the range of IPs.
- `has_a_website(self, ip_address)`: Checks if the given IP hosts a website.

### `check(ip_address, show)` Function

This function performs the IP address check, and optionally the website check, based on the given parameters.

- `ip_address`: The IP address to be checked.
- `show`: An optional HTTP POST parameter to determine whether or not to perform the website check.

## Example

To check if the IP address "127.0.0.1" is in the specified range and if it hosts a website, execute the following code:

```python
print(check("127.0.0.1", "True"))
```

To only check if the IP address "127.0.0.1" is in the specified range, execute the following code:

```python
print(check("127.0.0.1", ""))
```

## Author

Nx-Shield VPN

## License

Please refer to the project's [license file](./LICENCE) for information on how this code can be used.
