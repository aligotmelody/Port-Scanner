import dns.resolver
import re 
import termcolor
import socket



host_names = re.compile(r'^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9]*[a-zA-Z0-9])\.)+[a-zA-Z]{2,}$')
def hst_name_check(hst_name):
     return bool(host_names.match(hst_name))



def resolve_hostname(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"Resolved {hostname} to {ip_address}")
        return ip_address
    except socket.gaierror as e:
        print(termcolor.colored(f"Error resolving hostname: {e}", "light_red"))
        return None