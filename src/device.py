class Device:
    def __str__(self):
        return f"Device: {self.device_name}\nIP Address: {self.ip_address}\nMAC Address: {self.mac_address}\nOS Info: {self.os_info}"

    def __init__(self, device_name_info, ip_address, mac_address_info, os_info):
        self.device_name_info = device_name_info
        self.ip_address = ip_address
        self.mac_address_info = mac_address_info
        self.os_info = os_info

    def isonline(self):
        # Implement the logic to check if the device is online
        # You can use network-related functions or libraries to perform the check
        # Return True if the device is online, False otherwise

        # Example implementation:

        return NotImplemented

    def apconnected(self):
        # Implement the logic to locate the access point the device is connected to
        # You can use network-related functions or libraries to perform the check
        # Return the access point information (e.g., SSID, BSSID) if connected, None otherwise
        return NotImplemented

    def get_more_info(self):
        # Implement the logic to retrieve more information about the device through a socket
        # You can use socket-related functions or libraries to establish a connection and retrieve information
        # Return the additional information about the device
        return NotImplemented

    def get_device_name(self):
        return self.device_name_info[0]["name"]

    def get_device_name_info(self):
        return self.device_name_info

    def get_device_ip_address(self):
        return self.ip_address

    def get_device_mac_address_info(self):
        return self.mac_address_info

    def get_device_os_info(self):
        if len(self.os_info) > 1:
            return {
                posibility["name"]: f"{posibility['accuracy']}%"
                for posibility in self.os_info
            }
        return self.os_info[0]["name"]
