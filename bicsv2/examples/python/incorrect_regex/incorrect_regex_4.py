import re

def validate_ipv4_addresses(ip_list):
    valid_ips = []
    pattern = re.compile(r"\b(?:\d{3}\.){3}\d{1,3}\b")
    for ip in ip_list:
        if pattern.match(ip):
            valid_ips.append(ip)
    return valid_ips
