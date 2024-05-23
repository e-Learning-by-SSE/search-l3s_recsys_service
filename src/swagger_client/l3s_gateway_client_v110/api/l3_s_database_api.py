# coding: utf-8

"""
    L3S Gateway for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from l3s_gateway_client_v110.api_client import ApiClient


class L3SDatabaseApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_document_all(self, secret_key, **kwargs):  # noqa: E501
        """delete_document_all  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_document_all(secret_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str secret_key: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_document_all_with_http_info(secret_key, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_document_all_with_http_info(secret_key, **kwargs)  # noqa: E501
            return data

    def delete_document_all_with_http_info(self, secret_key, **kwargs):  # noqa: E501
        """delete_document_all  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_document_all_with_http_info(secret_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str secret_key: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['secret_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_document_all" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'secret_key' is set
        if ('secret_key' not in params or
                params['secret_key'] is None):
            raise ValueError("Missing the required parameter `secret_key` when calling `delete_document_all`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'secret_key' in params:
            query_params.append(('secret_key', params['secret_key']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/l3s-database/document/all', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_document_by_id(self, entity_type, entity_id, secret_key, **kwargs):  # noqa: E501
        """delete_document_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_document_by_id(entity_type, entity_id, secret_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: (required)
        :param str entity_id: (required)
        :param str secret_key: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_document_by_id_with_http_info(entity_type, entity_id, secret_key, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_document_by_id_with_http_info(entity_type, entity_id, secret_key, **kwargs)  # noqa: E501
            return data

    def delete_document_by_id_with_http_info(self, entity_type, entity_id, secret_key, **kwargs):  # noqa: E501
        """delete_document_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_document_by_id_with_http_info(entity_type, entity_id, secret_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: (required)
        :param str entity_id: (required)
        :param str secret_key: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id', 'secret_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_document_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `delete_document_by_id`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `delete_document_by_id`")  # noqa: E501
        # verify the required parameter 'secret_key' is set
        if ('secret_key' not in params or
                params['secret_key'] is None):
            raise ValueError("Missing the required parameter `secret_key` when calling `delete_document_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entity_type'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entity_id'] = params['entity_id']  # noqa: E501

        query_params = []
        if 'secret_key' in params:
            query_params.append(('secret_key', params['secret_key']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/l3s-database/document/{entity_type}/{entity_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_check_secret_key(self, secret_key, **kwargs):  # noqa: E501
        """get_check_secret_key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_check_secret_key(secret_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str secret_key: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_check_secret_key_with_http_info(secret_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_check_secret_key_with_http_info(secret_key, **kwargs)  # noqa: E501
            return data

    def get_check_secret_key_with_http_info(self, secret_key, **kwargs):  # noqa: E501
        """get_check_secret_key  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_check_secret_key_with_http_info(secret_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str secret_key: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['secret_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_check_secret_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'secret_key' is set
        if ('secret_key' not in params or
                params['secret_key'] is None):
            raise ValueError("Missing the required parameter `secret_key` when calling `get_check_secret_key`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'secret_key' in params:
            query_params.append(('secret_key', params['secret_key']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/l3s-database/check_secret', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_all(self, **kwargs):  # noqa: E501
        """get_document_all  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_document_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_document_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_document_all_with_http_info(self, **kwargs):  # noqa: E501
        """get_document_all  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/l3s-database/document/all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_by_id(self, entity_type, entity_id, **kwargs):  # noqa: E501
        """get_document_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_by_id(entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: (required)
        :param str entity_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_document_by_id_with_http_info(entity_type, entity_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_document_by_id_with_http_info(entity_type, entity_id, **kwargs)  # noqa: E501
            return data

    def get_document_by_id_with_http_info(self, entity_type, entity_id, **kwargs):  # noqa: E501
        """get_document_by_id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_by_id_with_http_info(entity_type, entity_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str entity_type: (required)
        :param str entity_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['entity_type', 'entity_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'entity_type' is set
        if ('entity_type' not in params or
                params['entity_type'] is None):
            raise ValueError("Missing the required parameter `entity_type` when calling `get_document_by_id`")  # noqa: E501
        # verify the required parameter 'entity_id' is set
        if ('entity_id' not in params or
                params['entity_id'] is None):
            raise ValueError("Missing the required parameter `entity_id` when calling `get_document_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'entity_type' in params:
            path_params['entity_type'] = params['entity_type']  # noqa: E501
        if 'entity_id' in params:
            path_params['entity_id'] = params['entity_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/l3s-database/document/{entity_type}/{entity_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_paths_all(self, **kwargs):  # noqa: E501
        """get_document_paths_all  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_paths_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_document_paths_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_document_paths_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_document_paths_all_with_http_info(self, **kwargs):  # noqa: E501
        """get_document_paths_all  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_paths_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_paths_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/l3s-database/document/all-paths', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_skills_all(self, **kwargs):  # noqa: E501
        """get_document_skills_all  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_skills_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_document_skills_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_document_skills_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_document_skills_all_with_http_info(self, **kwargs):  # noqa: E501
        """get_document_skills_all  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_skills_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_skills_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/l3s-database/document/all-skills', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_document_tasks_all(self, **kwargs):  # noqa: E501
        """get_document_tasks_all  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_tasks_all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_document_tasks_all_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_document_tasks_all_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_document_tasks_all_with_http_info(self, **kwargs):  # noqa: E501
        """get_document_tasks_all  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_document_tasks_all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_document_tasks_all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/l3s-database/document/all-tasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_l3_s_databse_sync(self, **kwargs):  # noqa: E501
        """get_l3_s_databse_sync  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_l3_s_databse_sync(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_l3_s_databse_sync_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_l3_s_databse_sync_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_l3_s_databse_sync_with_http_info(self, **kwargs):  # noqa: E501
        """get_l3_s_databse_sync  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_l3_s_databse_sync_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_l3_s_databse_sync" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/l3s-database/sync', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sse_search_ok(self, **kwargs):  # noqa: E501
        """get_sse_search_ok  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sse_search_ok(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DtoSSEConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sse_search_ok_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sse_search_ok_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sse_search_ok_with_http_info(self, **kwargs):  # noqa: E501
        """get_sse_search_ok  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sse_search_ok_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: DtoSSEConnectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sse_search_ok" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/l3s-database/connection-sse', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DtoSSEConnectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
