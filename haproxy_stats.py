#!/usr/bin/env python
import argparse
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


def discovery(socket_path='/var/run/haproxysock'):
    haproxy = HAProxySocket(socket_path)
    results = haproxy.cli('show stats')

    print(results)


def get_all_stats(socket_path='/var/run/haproxysock'):
    haproxy = HAProxySocket(socket_path)
    info = haproxy.cli('show info')
    stats = haproxy.cli('show stats')

    print(info, stats)


def get_one_stats(socket_path='/var/run/haproxysock'):
    haproxy = HAProxySocket(socket_path)
    stats = haproxy.cli('show stats')

    print(stats)


def send_command(command, socket_path='/var/run/haproxysock'):
    haproxy = HAProxySocket(socket_path)
    results = haproxy.cli(command)

    print(results)


def main():
    print('Discovery Output')
    discovery()

    print('All Statistics')
    get_all_stats()

    print('One Statistic')
    get_one_stats()

    print('Send Command')
    send_command('show info')


if __name__ == "__main__":
    main()
