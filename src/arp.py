import re

# trunk-ignore(bandit/B404)
import subprocess

import pandas as pd


def get_arp_data():
    # trunk-ignore(bandit/B602)
    # trunk-ignore(bandit/B607)
    arp_data = subprocess.check_output("arp -a", shell=True).decode("utf-8")

    # Split the data into blocks for each interface
    interfaces_data = re.split(r"\n\s*\n", arp_data.strip())

    # Initialize an empty list to store individual records
    records = []

    for interface_data in interfaces_data:
        lines = interface_data.split("\n")
        interface_info = lines[0].split(" --- ")[0].split(": ")[1]

        for line in lines[2:]:
            if elements := line.split():
                records.append([interface_info] + elements)

    # Create a DataFrame
    columns = ["Interface", "Internet_Address", "Physical_Address", "Type"]
    return pd.DataFrame(records, columns=columns)
