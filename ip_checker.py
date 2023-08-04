#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Python Version    : 3.X
# Author            : Nx-Shield VPN

import ipaddress
import requests

class IpChecker:
    """
    IpChecker Class

    Methods:
        - __init__(self, RANGE_IP): Constructor for initializing the IP range.
        - check_ip_range(self, ip_address): Checks if the given IP is within the range of IPs.
        - has_a_website(self, ip_address): Checks if the given IP hosts a website.
    """

    def __init__(self, RANGE_IP):
        """Constructor to initialize the IP range."""
        self.RANGE_IP = RANGE_IP

    def check_ip_range(self, ip_address):
        """
        Check if the given IP address is within the range of IPs.

        Args:
            ip_address (str): The IP address to be checked.

        Returns:
            str: "Yes" if the IP is in range, "No" otherwise.
        """
        for ip in self.RANGE_IP:
            try:
                if ipaddress.ip_address(ip_address) in list(ipaddress.ip_network(ip, False).hosts()):
                    return "Yes"
                else:
                    return "No"
            except ValueError:
                return "No"

    def has_a_website(self, ip_address):
        """
        Check if the given IP address hosts a website.

        Args:
            ip_address (str): The IP address to be checked.

        Returns:
            str: The website content if it exists, "Nothing" otherwise.
        """
        try:
            render = (requests.get(ip_address).text)
        except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
            ip_address = f"http://{ip_address}"
            try:
                render = (requests.get(ip_address).text)
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.TooManyRedirects):
                render = "Nothing"
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout, requests.exceptions.TooManyRedirects):
            render = "Nothing"
        return render


def check(ip_address, show):
    """
    Perform the IP address check.

    Args:
        ip_address (str): The IP address to be checked.
        show (str): An optional HTTP POST parameter to determine whether or not to perform the website check.

    Returns:
        list: Contains the result of the IP range check and, optionally, the website check.
    """
    render = list()
    if (show and not ip_address) or ip_address == '':
        render = ['Error']

    if ip_address != '':
        RANGE_IP = ['1.1.1.1/24', '8.8.8.8/24', '8.8.4.4/24']
        checker = IpChecker(RANGE_IP)
        render_range = checker.check_ip_range(ip_address)
        render.append(render_range)

        if show != '':
            render_website = checker.has_a_website(ip_address)
            render.append(render_website)
            return render

    return render


if __name__ == "__main__":
    print(check("127.0.0.1", "True"))
