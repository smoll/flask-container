import os
import unittest
from pyvirtualdisplay import Display
from selenium import webdriver

class TestViewCount(unittest.TestCase):

    def setUp(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.driver = webdriver.Firefox()

        self.addCleanup(self.driver.quit)
        self.addCleanup(self.display.stop)

    def testViewCount(self):
        if os.environ.get('DOCKER_HOST') is not None:
            try:
                from urllib.parse import urlparse # for python3
            except ImportError: # for backwards compatibility
                from urlparse import urlparse
            uri = urlparse(os.environ.get('DOCKER_HOST')) # e.g. tcp://192.168.59.103:2376
            host = uri.hostname # e.g. 192.168.59.103
        else:
            host = 'localhost'

        self.driver.get('http://%s:5000' % host)
        self.assertRegex(self.driver.page_source, r'[0-9]+ times') # str looks like "...viewed 123 times."

if __name__ == '__main__':
    unittest.main(verbosity=2)
