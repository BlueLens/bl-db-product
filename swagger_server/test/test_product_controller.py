# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.add_product_response import AddProductResponse
from swagger_server.models.delete_product_response import DeleteProductResponse
from swagger_server.models.get_product_response import GetProductResponse
from swagger_server.models.get_products_response import GetProductsResponse
from swagger_server.models.product import Product
from swagger_server.models.update_product_response import UpdateProductResponse
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestProductController(BaseTestCase):
    """ ProductController integration test stubs """

    def test_add_product(self):
        """
        Test case for add_product

        Added a new Product
        """
        body = Product()
        response = self.client.open('//products',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_delete_product_by_id(self):
        """
        Test case for delete_product_by_id

        Deletes a Product
        """
        response = self.client.open('//products/{productId}'.format(productId='productId_example'),
                                    method='DELETE')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_product_by_id(self):
        """
        Test case for get_product_by_id

        Find Product by ID
        """
        response = self.client.open('//products/{productId}'.format(productId='productId_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_products_by_hostcode(self):
        """
        Test case for get_products_by_hostcode

        Get Product by host_code
        """
        response = self.client.open('//products/hosts/{hostCode}'.format(hostCode='hostCode_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_product(self):
        """
        Test case for update_product

        Update an existing Product
        """
        body = Product()
        response = self.client.open('//products',
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
