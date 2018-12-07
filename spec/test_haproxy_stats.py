import unittest
import haproxy_stats


class TestHAProxy(unittest.TestCase):

    def test_cli(self):
        haproxy = haproxy_stats.HAProxySocket('/socket/path')
        self.assertIsNotNone(haproxy.cli('show stats'))
        self.assertIsNotNone(haproxy.cli('show info'))


if __name__ == '__main__':
    unittest.main()
