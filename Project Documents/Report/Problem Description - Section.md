---
tags:
  - G5038-Individual-Project
---

### What is the Problem that is being solved?

This Project `Crowd Pulse` aims to solve 3 problems; Crowd Monitoring, Effective Resource Allocation, and Security & safety concerns.

#### Crowd Monitoring - Primary Focus

`Crowd Pulse` will provide insights into presence and density values, for the campus area, providing insights for monitoring the campus area.

#### Resource Allocation Optimization - Secondary Focus

By tracking the crowd density, it would allow the campus administration to allocate more resources to areas that have more traffic.

#### Safety and Security - Secondary Focus

This could greatly contribute to the security and safety of the campus, as it would allow campus security to know where issues could be identified, as well as knowing areas that should be monitored for people's safety.

### Does `Crowd Pulse` Build on anything?

#continue-later

### Has it been done before

`Crowd Pulse` is not the first system to attempt such a thing, there are a multitude of other projects that revolve around crowd monitoring and analysis of the data. However these systems often use different methods to capture the crowd presence data, such as:

- Computer Vision
- Weight Monitoring System (used on trains mostly)
- IoT sensors
- Body Heat

  However using these methods can be inefficient, as shown below:

  - Computer vision requires that cameras be set up at all the exits and entrances, as well as expensive software to identify people and monitor when specific people enter and exit buildings.
  - Weight monitoring requires that all people are of similar weights to identify how many people are in an area, this is not always the case as children do not weigh as much as adults, and the weight variability between adults is large, and so there is not an accurate way of measuring crowd density
  - IoT sensors, depending on the implementation it can be a good way of identifying people, but it requires lots of small devices to be placed around an area for monitoring.
  - Body head systems, can be thrown off by large heat sources and so are not a good indication of crowd density, it is also hard to generate crowd density values if there is a large crowd if the crowd is packed tightly together, so heat sources are not easy to determine.

`Crowd Pulse` uses a form of WIFI tracking, which allows tracking crowd density on the following assumptions, which are talked about in more depth later in this report:

> [!warning] Assumption 1 - Each member of the crowd will have a device

> [!warning] Assumption 2 - The device a crowd member has will be on the local WIFI network

> [!warning] Assumption 3 - Crowd members will have no more than 1 device actively connected to the network

### Why is this an "important" problem?

#continue-later

### Why it's interesting / worthwhile

### What does the reader / examiner need to know / understand

- Network Classes
- CIDR
