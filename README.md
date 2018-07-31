# Zabbix Template for HAProxy

This Zabbix template for HAProxy aims to achieve dynamic monitoring on frontends, backends, and servers by means of
querying the HAProxy stats socket available on the client machine. Each Zabbix item is generated with discovery scripts.

For Zabbix 3.2 and earlier, metrics are retrieved for each item interval. For Zabbix 3.4 and greater, the 
[Dependent Items](https://www.zabbix.com/documentation/3.4/manual/config/items/itemtypes/dependent_items) functionality 
is used to update items simultaneously.

HAProxy Statistics:
* HTTP Response Codes
* Network Traffic
* User Sessions
* Bytes In/Out

## Requirements

* Zabbix 2.2 or later
* HAProxy 1.5 or later
* Python 2.6 or later

## Installation

### Zabbix 3.4+

### Zabbix 2.2 - 3.2