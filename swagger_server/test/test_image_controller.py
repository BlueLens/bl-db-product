# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.add_image_response import AddImageResponse
from swagger_server.models.image import Image
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestImageController(BaseTestCase):
    """ ImageController integration test stubs """

    def test_add_image(self):
        """
        Test case for add_image

        Added a new Image
        """
        body = Image()
        response = self.client.open('//images',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
