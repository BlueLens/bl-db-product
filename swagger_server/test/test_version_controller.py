# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.add_version_response import AddVersionResponse
from swagger_server.models.get_version_response import GetVersionResponse
from swagger_server.models.latest_version_response import LatestVersionResponse
from swagger_server.models.version import Version
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestVersionController(BaseTestCase):
    """ VersionController integration test stubs """

    def test_add_version(self):
        """
        Test case for add_version

        Add a new Version
        """
        body = Version()
        response = self.client.open('//versions',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_latest_version(self):
        """
        Test case for get_latest_version

        Gat latest Version
        """
        response = self.client.open('//versions/latest',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_version_by_id(self):
        """
        Test case for get_version_by_id

        Gat Version by ID
        """
        response = self.client.open('//versions/{versionId}'.format(versionId='versionId_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
