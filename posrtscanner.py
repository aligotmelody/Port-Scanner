import socket 
import termcolor
import ipaddress
import re
from hostname import resolve_hostname


print(termcolor.colored("""
                                                                                          
                                                                                          
                                                                                          
                                             :.                                           
                                             -*                                           
                                             ##                                           
                                            *%+                                           
                                         - :%%=                                           
                                         -=:%%%=                                          
                                  :      #+ +%%%#       :                                 
                                   +    #%.  %%%%*     =:                                 
                       -+.         #-  .%%= :%%%%*  *=%:          .-:                     
                        -%-      .=%%=  +%%%%%%%#. -%%=     .= -+#+:                      
                         -%%#**=.  *%%%+ +%%%%%% .#%%%-  =*+=:%%=                         
                        .-=-=#%%%+ -%%%%..%%%%%# :%%%%:.#%: :%%%                          
                          =#. =%%%: -==:-*%#####*--::  *%%##%%%=                          
                   ..      =%##%%%%*=++*+:       .:=+*%%%%%%*+:  ..                       
                     -++-. ..:-+%%%#+*%+             .+%%*: -=++#%++=-:                   
                      .+%%%%%%* .%+*%%#     +*=        .*= *%%%%#-                        
                         :+%%%# *=#%%%#    .#%*          *=.+#*= .:::.                    
                  .-+*#*+:  :: ++#%%%%%-                  #=::-+#%%%###+=--.              
        .:--:...:*%%%%%%%%%###%%=%%%%%%%+:                =%%%%%%%=    .---:.             
       .::-+#%%%%%%#+==*%%%%%%%%=%%%%%%%%%%*++=-.         :%%%%%%%%***#%%%%%%%#+=--.      
              .::--.   .#%%%%%%%=%%%%%%%%%%%%%%%%#:       =%***#%%%%%%%%#-    .:..        
               :::-+#%%%%#+-:::+**%%%%%%%%%%%%%%%%%-     .%:.--. :=+++-.                  
                      ..  -#%%#:++*%%%%%%%%#  =%%%%*     *-:%%%%*:.                       
                       :=*%%%%%- +*+%%%%%%%%*+#%%%%+   :#*  +%%%#%%=                      
                   .:---=*-::. .=%%%*+*%%%%%%%%%%%+  -#%%%%*=:    :=+-                    
                        .   =#%%%%%%+=++********+==++:-*%%%%+##:      .                   
                           #%%#++%%- -+=-:*%%%%%%:.=**- *%%#: :#.                         
                          .%%*  +%+ *%%%%..%%%%%# =%%%%..*%%%#+=-.                        
                         :#%*:++=.  *%%#- =%%%%%%= +%%%-  .-==+%#.                        
                       =*+-. -     .%%*  =%%%%##%%=  +%*:       +#.                       
                      -.           #=.-  %%%%*  *%*   *=         :=:                      
                                  =      #%%%+  +%-   .+                                  
                                         .#%%%- %-     .                                  
                                           =%%% *                                         
                                            #%*  :                                        
                                            %%.                                           
                                           :%-                                            
                                            #                                             
                                            :                                             
                                                                                          
                                                                                          
              BY __ALI ELTAIB__
              @san_lowkey                                                                           

""", "cyan"))




#checking the octets of an IP Address:
def octet(ip_address):
       address = []
       octets = ip_address.split(".")
       for octet in octets:
            if int(octet) < 0 or int(octet) > 255:
                  raise ValueError(termcolor.colored("Invalid IP address !!!","light_red"))
       current_ip = ".".join(octets)
       address.append(current_ip)
       return address

#----------------------------------------------------------------------------
# ipv4 REGEX check #

IPv4_regex = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}(?:\/\d{1,2})?\b')
def ip_is_valid(ip_address):
      return bool(IPv4_regex.match(ip_address))

#----------------------------------------------------------------
#  getting the ip range #

def get_range_ip_inpt(ip_range_str):
       if ip_is_valid(ip_range_str) and "/" in ip_range_str :
             ip_network = ipaddress.ip_network(ip_range_str, strict=False)
             CIp_range = [str(ip) for ip in ip_network.hosts()]
             OIp_Range=[]
             for ip in CIp_range:
                   OIp= octet(ip)
                   OIp_Range.append(OIp)

             return OIp_Range
       elif "," in ip_range_str :
              Ip_range = ip_range_str.split(",")
              IP_range1 =[]
              for ip in Ip_range:
                    if ip_is_valid(ip):
                          f_ip =octet(ip)
                          IP_range1.append(f_ip)
                    else:
                          print(termcolor.colored("there's an invalid IP among the provided IPs !!!", "light_red"))
              return IP_range1
       elif '.' in ip_range_str:
              Oip = octet(ip_range_str)
              return (Oip) 
       else:
             print(termcolor.colored("THE PROVIDED IP ADDRESS IS NOT VALID !!", "red"))
             new_ip = input(termcolor.colored("rewrite the ip: ", "cyan"))
             get_range_ip_inpt(new_ip)


#---------------------------------------------------------------
# the port REGEX check #
             
port_regex = re.compile(r'^\d{1,5}$|^\d{1,5}-\d{1,5}|\d{1,5}(,\d{1,5})*')
def port_is_valid(port):
       return bool(port_regex.match(port))
       

#----------------------------------------------------------------------
def get_port():
      flag = ""
      str_ports = input(termcolor.colored("Specify The Ports: ", "light_cyan"))
      if port_is_valid(str_ports):
             if "," in str_ports:
                     flag = "lst"
                     nm_ports = str_ports.split(",")
                     int_ports = [int(port) for port in nm_ports]
                     print(flag)
                     return int_ports, flag
             elif "-" in str_ports:
                     flag = "rng"
                     f_ports=[]
                     nm_ports = str_ports.split("-")
                     if int(nm_ports[0]) > int(nm_ports[1]):
                            print(termcolor.colored("order of ports range is not correct !!!", "red"))
                            get_port()
                     else:
                            for port in range(int(nm_ports[0]),int(nm_ports[1])+1):
                                     f_ports.append(port)
                            print(flag)  
                            return f_ports, flag
             elif int(str_ports) > 0:
                   flag = "solo"
                   print(flag)
                   return str_ports, flag

#------------------------------------------------------------------

def Scanner(ip, ports, flag):
      if flag == "lst" or  flag =="rng":
             for port in ports:
                   port_scan(ip,port)
      elif flag == "solo":
            port_scan(ip,ports)
      else:
            print(termcolor.colored("unexpected value check the Scanner function !!!!", "light_red"))
#-----------------------------------------------------------------------------------           
              
def port_scan(ipAddress, Port):
          for ip in ipAddress:
                ip_obj = ipaddress.ip_address(ip)
                ip_str = str(ip)
                try:
                     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                     #sock.settimeout(5)
                     if isinstance(Port, str):
                             Port = int(Port)
                             print(type(Port))
                             print(type(ip_obj))
                             print(ip_obj)
                             sock.connect_ex((ip, Port))
                             #sock.connect_ex((ip_obj, Port))  # Attempt connection (might raise exception)
                             result = sock.recv(1024).decode()
              
                     return result
            
                except socket.timeout:
                            print(termcolor.colored(f"[-] Connection timed out for port {Port}", "light_yellow"))  
                except ValueError:  
                            print(termcolor.colored("invalid value !!", "light_red"))
              
                except KeyboardInterrupt :
                            print(termcolor.colored("Scan stopped by user !!!!!.", "red"))

                except socket.error :
                            print(termcolor.colored(f"Couldn't connect to the server {ipAddress} xxxxxxx", "light_red"))
                finally:
                            sock.close()  
#--------------------------------------------------------------------
# USER Input check #
def given_inpt_check(inpt):
       if ip_is_valid(inpt):
              targets = get_range_ip_inpt(inpt)
              Port, flag = get_port()
              print(flag)
              Scanner(targets, Port,flag)
              return targets 

       elif hst_name_check(inpt):
             IP_address = resolve_hostname(inpt)
             targets = get_range_ip_inpt(IP_address)
             Port = get_port()
             Scanner(targets, Port)
             return targets
       else:
             print(termcolor.colored("invalid form !!!", "light_red"))
             main()
#####################   MAIN   #########################
print("Second commit")
  
def main():
      user_inpt = input(termcolor.colored("PS: the tool takes CIDR notation || provide the HOSTNAME or IP: ", "light_cyan"))
      given_inpt_check(user_inpt)
   

if __name__ == "__main__" : 
      main()