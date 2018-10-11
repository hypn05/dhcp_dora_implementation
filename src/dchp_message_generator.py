import struct
import socket

def dhcp_message(operation_code,
                 hardware_type,
                 hardware_address_length,
                 transaction_identifier,
                 client_IP_address,
                 your_IP_address,
                 server_IP_address,
                 gateway_IP_address,
                 client_hardware_address
                 ):
    # make empty binary string
    dhcp_message = b''
    
    # Field name: Operation Code (OP) 
    # Size: 1 Byte
    OP = struct.pack('B',operation_code)
    dhcp_message += OP
    
 
    # Field name: Hardware Type: HType
    # Size: 1 Byte
    HType = struct.pack('B',hardware_type)
    dhcp_message+= HType
    
    
    # Field name: Hardware Address Length: HLen
    # Size: 1 Byte
    # Value: 6
    HLen = struct.pack('B',hardware_address_length)
    dhcp_message+= HLen
    
    
    # Field name: Hops
    # Size: 1 Byte
    # Value: 0 (no relay nodes)
    Hops = struct.pack('B',0)
    dhcp_message += Hops
    
    
    # Field name: Transaction Identifier (XID) 
    # Size: 4 Byte(s)
    # Value: A 32-bit identification field generated by the client,
    # to allow it to match up the request with replies received from DHCP servers.
    XID = struct.pack('I',transaction_identifier)
    dhcp_message += XID
    
    
    # Field name: Seconds (Secs)
    # Size: 2 Byte(s)
    # Value: For DHCP, it is defined as the number of seconds elapsed 
    # since a client began an attempt to acquire or renew a lease
    # Value: 0
    Secs = struct.pack('H',0)
    dhcp_message += Secs
    
    # Field name: Flags (Flags)
    # Size: 2 Byte(s)
    # Value: 0
    Flags = struct.pack('H',0)
    dhcp_message += Flags
    
    # Field name: Client IP Address (CIAddr)
    # Size: 4 Byte(s)
    # Hint: use  socket.inet_aton(ip_string)
    CIAddr = socket.inet_aton(client_IP_address)
    dhcp_message+= CIAddr
    
    # Field name: Your IP Address (YIAddr)
    # Size: 4 Byte(s)
    # Hint: use  socket.inet_aton(ip_string)
    YIAddr = socket.inet_aton(your_IP_address)
    dhcp_message+= YIAddr
    
    
    # Field name: Server IP Address (SIAddr)
    # Size: 4 Byte(s)
    # Hint: use  socket.inet_aton(ip_string)
    SIAddr = socket.inet_aton(server_IP_address)
    dhcp_message+= SIAddr
    
    # Field name: Gateway IP Address (GIAddr)
    # Size: 4 Byte(s)
    # Hint: use  socket.inet_aton(ip_string)
    GIAddr = socket.inet_aton(gateway_IP_address)
    dhcp_message+= GIAddr
    
    # Field name: Client Hardware Address: (CHAddr)
    # Size: 16 Byte(s)
    # the first 6 bytes are for the MAC address
    # Create empty binary string
    CHAddr = b''
    for mac_field in client_hardware_address.split(':'):
        # convert Hex to int and pack it as one byte
        CHAddr +=   struct.pack('B', int(mac_field, 16))
    
    # the rest of the bytes will be set to zero
    for i in range(10):
        CHAddr += struct.pack('B', 0)
    
    dhcp_message+= CHAddr
    
    
    return dhcp_message
