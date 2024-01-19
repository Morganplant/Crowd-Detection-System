# Project Objectives

> [!error] Assumptions
>
> - All of the people have at least 1 device connected to the local WIFI network (eduroam)
> -

### Goals

- Generate a number of "people" in different areas, to estimate the crowd density of these areas
  - this works only if areas are on [different subnets] DHCP ranges, DHCP leases to 5min, to know quickly if a device has left the network
- Generate a number of "people" on the entire campus / general area
  - Ways to do this:
    - with network management access:
      - via network management API, this way you can look at the topology of the network and so long as you know the physical location of the access points devices are connecting to, the system can pick out smartphones / other devices, to provide a crowd density value for the different access points.
    - without:
      - scan the entire network for phones / devices - this shows the an estimate of the crowd density on the whole network [Does not show specific areas]
      - go to specific areas, and use packet sniffing techniques, to identify devices to produce a crowd density number
- Save Historical Data in a secure anonymous way
- Produce an interface that shows the following:
  - Crowd density of the general area
  - Crowd density of smaller areas within the general area (computer science labs, lunch areas, cafes, etc...)
  - show a graph based on historical data to show historical crowd density

### Scanning

System should scan devices on a network and then through "some" process identify smartphones / other devices, that allows the system to identify this device as a datapoint for crowd density calculations.

#### WIFI

- Scan the network
- Discover Smartphones / other devices to identify a crowd data point

#### IOT

- scan for nearby devices
- Discover Smartphones / other devices to identify a crowd data point
