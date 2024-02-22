import unittest
from osrm.client import Client


class RouteTest(unittest.TestCase):

    def setUp(self) -> None:
        self.client = Client(profile="car")

    def test_route_arg_validation(self):
        res = self.client.route("90.41077946230386,23.79267908943424;90.41069869278742,23.793502599914536")
        self.assertTrue(res is not None)
        pass


if __name__ == '__main__':
    unittest.main()
