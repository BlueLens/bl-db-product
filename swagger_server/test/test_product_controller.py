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
        query_string = [('offset', 56),
                        ('limit', 56)]
        response = self.client.open('//products/hosts/{hostCode}'.format(hostCode='hostCode_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_products_by_hostcode_and_product_no(self):
        """
        Test case for get_products_by_hostcode_and_product_no

        Get Product by hostCode and productNo
        """
        response = self.client.open('//products/hosts/{hostCode}/products/{productNo}'.format(hostCode='hostCode_example', productNo='productNo_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_products_by_hostcode_and_version_id(self):
        """
        Test case for get_products_by_hostcode_and_version_id

        Get Product by hostCode and versionId
        """
        response = self.client.open('//products/hosts/{hostCode}/versions/{versionId}'.format(hostCode='hostCode_example', versionId='versionId_example'),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_products_by_ids(self):
        """
        Test case for get_products_by_ids

        Find Products by IDs
        """
        query_string = [('productIds', 'productIds_example')]
        response = self.client.open('//products',
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_products_by_image_id_and_object_id(self):
        """
        Test case for get_products_by_image_id_and_object_id

        Get Products by imageId and objectId
        """
        response = self.client.open('//products/images/{imageId}/objects/{objectId}'.format(imageId='imageId_example', objectId=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_get_products_by_version_id(self):
        """
        Test case for get_products_by_version_id

        Get Product by versionId
        """
        query_string = [('is_indexed', true),
                        ('offset', 56),
                        ('limit', 56)]
        response = self.client.open('//products/versions/{versionId}'.format(versionId='versionId_example'),
                                    method='GET',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_product_by_hostcode_and_productno(self):
        """
        Test case for update_product_by_hostcode_and_productno

        Update an existing Product
        """
        body = Product()
        response = self.client.open('//products/hosts/{hostCode}/products/{productNo}'.format(hostCode='hostCode_example', productNo='productNo_example'),
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_update_product_by_id(self):
        """
        Test case for update_product_by_id

        Update an existing Product
        """
        body = Product()
        response = self.client.open('//products/{productId}'.format(productId='productId_example'),
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
