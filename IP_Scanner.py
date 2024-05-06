# A basic example of an Internet Protocol Scanner
import socket

def port_scan(target_ip, port):
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for the connection attempt

        # Attempt to connect to the target IP address and port
        result = s.connect_ex((target_ip, port))
        
        # Check if the connection was successful (0 indicates success)
        if result == 0:
            print(f"Port {port} is open")
            return True
        else:
            print(f"Port {port} is closed")
            return False
    except Exception as e:
        # Handle any errors that occur during the connection attempt
        print(f"Error scanning port {port}: {e}")
    finally:
        # Ensure the socket is closed
        s.close()

def partition_ip(ip_as_str):
    ip_as_str = ip_as_str + "."
    ip = []
    bufferStr = ""
    for i in range(0,len(ip_as_str)):
        if (ip_as_str[i] == '.'):
            ip.append(bufferStr)
            bufferStr = "" # clears string
        else:
            bufferStr = bufferStr + ip_as_str[i]
    return ip

def paritioned_ip_to_string(paritioned_ip):
    ip = ""
    for i in range(0,len(paritioned_ip)):
        ip = ip + str(paritioned_ip[i])
        if (i != len(paritioned_ip)-1):
            ip = ip + "."
    return ip
        
# ip is broken down into 4 sections
def scan_active_ips(start_ip_str, end_ip_str, port):
    active_ips = []
    start_ip = partition_ip(start_ip_str)
    end_ip = partition_ip(end_ip_str)
    print("Start IP: ")
    print(start_ip)
    print("END IP:")
    print(end_ip)
    ip = [start_ip[0],start_ip[1],start_ip[2],start_ip[3]]
    for i in range(0, len(ip)):
        for j in range(int(start_ip[i]),int(end_ip[i])):
            ip[i] = j
            asStr = paritioned_ip_to_string(ip)
            #print(ip)
            if port_scan(asStr, port):
                print(asStr)
                active_ips.append(asStr)

def is_ip_active(ip, port):
    try:
        # Create a TCP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for the connection attempt

        # Attempt to connect to the IP address and port using a TCP SYN packet
        result = s.connect_ex((ip, port))
        
        # Check if the connection was successful (0 indicates success)
        if result == 0:
            return True
        else:
            return False
    except Exception as e:
        # Handle any errors that occur during the connection attempt
        print(f"Error scanning IP {ip}: {e}")
        return False
    finally:
        # Ensure the socket is closed
        s.close()


# Example usage:
start_ip = "192.168.0.0"
end_ip = "192.168.255.255"
port = 80  # A common port used by http cameras
scan_active_ips(start_ip, end_ip, port)
