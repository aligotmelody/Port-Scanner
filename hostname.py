import dns.resolver
import re 
import termcolor



host_names = re.compile(r'^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9]*[a-zA-Z0-9])\.)+[a-zA-Z]{2,}$')
def hst_name_check(hst_name):
     return bool(host_names.match(hst_name))



def resolve_hostname(hostname):
  
  try:
    resolver = dns.resolver.Resolver()
    ip_address = resolver.query(hostname, 'A')[0].to_text()
    i = 0
    while len(ip_address) > 0 and ip_address[i+1].rdtype == dns.rdatatype.CNAME:
          cname_target = ip_address[0].data.to_text()
          print(f"Following CNAME record: {hostname} --> {cname_target}")
    return ip_address
  
  except dns.resolver.NoAnswer:
    print(termcolor.colored(f"Error resolving hostname '{hostname}': Could not find IP address !!!", "light_red"))
    return None