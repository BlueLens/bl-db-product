# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.add_object_response import AddObjectResponse
from swagger_server.models.get_object_response import GetObjectResponse
from swagger_server.models.object import Object
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestObjectController(BaseTestCase):
    """ ObjectController integration test stubs """

    def test_add_object(self):
        """
        Test case for add_object

        Added a new Object
        """
        body = Object()
        response = self.client.open('//objects',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_object_by_id(self):
        """
        Test case for get_object_by_id

        Find Object by ID
        """
        response = self.client.open('//objects/{objectId}'.format(objectId='objectId_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
