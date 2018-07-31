#!/usr/bin/env python
import argparse
import csv
import socket
import sys


class HAProxySocket:

    def __init__(self, socket_path):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.socket_file = socket_path

    def cli(self, message):
        payload = ''

        # Open the socket.
        try:
            self.sock.connect(self.socket_file)
        except IOError as msg:
            return msg

        # Send the CLI command to the socket.
        message = "{}\n".format(message)
        self.sock.send(bytearray(message, 'ASCII'))

        # Get back a response and compile it line-by-line.
        response = self.sock.recv(8192)
        while response:
            payload += response.decode('ASCII')
            response = self.sock.recv(8192)

        # If there was a response return it.
        if payload:
            return payload

        # Close the socket connection.
        self.sock.close()


def discovery(args):
    haproxy = HAProxySocket(args.socket_path)
    results = haproxy.cli('show stats')

    print(results)


def get_all_metrics(args):
    haproxy = HAProxySocket(args.socket_path)
    info = haproxy.cli('show info')
    metrics = haproxy.cli('show stats')

    print(info, metrics)


def get_one_metric(args):
    haproxy = HAProxySocket(args.socket_path)
    results = haproxy.cli('show stats')

    print(results)


def send_command(args):
    haproxy = HAProxySocket(args.socket_path)
    results = haproxy.cli(args.command)

    print(results)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--socket", help="The file path to the HAProxy socket")
    subparsers = parser.add_subparsers("sub-command help")

    discovery_parser = subparsers.add_parser('discovery', help="Discover the available HAProxy endpoints")
    discovery_parser.set_defaults(func=discovery)

    all_metrics_parser = subparsers.add_parser('all metrics')
    all_metrics_parser.add_argument("-a", "--all-metrics")
    all_metrics_parser.set_defaults(func=get_all_metrics)

    one_metric_parser = subparsers.add_parser('one metric')
    one_metric_parser.add_argument("-e", "--endpoint", type=str, help="The frontend, backend, or server metrics")
    one_metric_parser.add_argument('-m', '--metric', type=str, help="The particular metric being gathered")
    one_metric_parser.set_defaults(func=get_one_metric)

    command_parser = subparsers.add_parser('command')
    command_parser.add_argument('-c', '--command', type=str, help="Run an HAProxy CLI command")
    command_parser.set_defaults(func=send_command)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
