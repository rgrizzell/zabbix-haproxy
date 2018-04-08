# Zabbix Template for HAProxy.

This Zabbix template for HAProxy aims to achieve dynamic monitoring on frontends, backends, and servers by means of
querying the HAProxy stats socket available on the client machine. Each Zabbix item is generated with discovery scripts.

To ensure HAProxy statistics match up in terms of times, statistics in Zabbix 3.2 and earlier are queried in bulk and
cached on local system until the next check interval. For Zabbix 3.4 and greater, the 
[Dependent Items](https://www.zabbix.com/documentation/3.4/manual/config/items/itemtypes/dependent_items) functionality 
is used to update items simultaneously.

HAProxy Statistics:
* HTTP Response Codes
* Network Traffic
* User Sessions

## Requirements

* Zabbix 2.2 or later
* HAProxy 1.5 or later
* Python 2.6 or later

## Installation

### Zabbix 3.4+

### Zabbix 2.2 - 3.2