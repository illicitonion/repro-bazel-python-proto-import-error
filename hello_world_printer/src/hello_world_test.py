import unittest

import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_instantiate_proto(self):
        proto_instance = hello_world.instantiate_proto()
        self.assertEqual(proto_instance.some_string, "Hello world")

if __name__ == '__main__':
    unittest.main()
