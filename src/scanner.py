import datetime as dt
import ipaddress
import os

import nmap3
import pandas as pd
from rich import print

from arp import get_arp_data
from extras import DATA_DIR

arp_dataframe = get_arp_data()
# addrs = arp_dataframe[arp_dataframe["Internet_Address"].str.startswith("192.168")][
#     "Internet_Address"
# ]
# TODO ping sweep before to identify devices that are down/don't exist and need to be skipped
addrs = list(ipaddress.ip_network("192.168.0.0/16"))

# Use nmap to get additional information about the devices
nmap = nmap3.Nmap()  # Adjust the concurrency level as needed

# Create an empty list to store the extracted information
data_list = []

for addr in addrs:
    addr = str(addr)
    if not nmap.as_root():
        print("Error: Insufficient privileges to run scan")
        exit()

    results = nmap.nmap_os_detection(addr)
    data = results[addr]

    # Extract actively used ports
    active_ports = [port["portid"] for port in data["ports"] if port["state"] == "open"]

    # Extract hostname
    hostname = data["hostname"][0]["name"] if data.get("hostname") else ""

    # Extract macaddress and macaddrvendor
    macaddress = data["macaddress"]["addr"] if data.get("macaddress") else ""
    macaddrvendor = (
        data["macaddress"].get("vendor", "") if data.get("macaddress") else ""
    )

    # Extract likely os
    likely_os = data["osmatch"][0]["name"] if data.get("osmatch") else ""

    # Check if the extracted information is empty
    if active_ports or hostname or macaddress or macaddrvendor or likely_os:
        # Append the extracted information to the data_list
        new_data = {
            "ip_address": addr,
            "active_ports": active_ports,
            "hostname": hostname,
            "macaddress": macaddress,
            "macaddrvendor": macaddrvendor,
            "likely_os": likely_os,
        }

        data_list.append(new_data)
        print(new_data)

# Create a dataframe from the data_list
df = pd.DataFrame.from_records(data_list)

# Print the dataframe
print(df)

# Save the dataframe to a CSV file
file_name = os.path.join(DATA_DIR, f"{dt.datetime.now().timestamp()}-scan-output.csv")
df.to_csv(file_name)
