# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.add_host_response import AddHostResponse
from swagger_server.models.host import Host
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestHostController(BaseTestCase):
    """ HostController integration test stubs """

    def test_add_host(self):
        """
        Test case for add_host

        Add a new HOst
        """
        body = Host()
        response = self.client.open('//hosts',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
