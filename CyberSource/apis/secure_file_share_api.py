# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class SecureFileShareApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, merchant_config, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client
        self.api_client.set_configaration(merchant_config)

    def get_file(self, file_id, **kwargs):
        """
        Download a file with file identifier
        Download a file for the given file identifier
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_file(file_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_id: Unique identifier for each file (required)
        :param str organization_id: Valid Cybersource Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_file_with_http_info(file_id, **kwargs)
        else:
            (data) = self.get_file_with_http_info(file_id, **kwargs)
            return data

    def get_file_with_http_info(self, file_id, **kwargs):
        """
        Download a file with file identifier
        Download a file for the given file identifier
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_file_with_http_info(file_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str file_id: Unique identifier for each file (required)
        :param str organization_id: Valid Cybersource Organization Id
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file_id', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file_id' is set
        if ('file_id' not in params) or (params['file_id'] is None):
            raise ValueError("Missing the required parameter `file_id` when calling `get_file`")

        if 'organization_id' in params and len(params['organization_id']) > 32:
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_file`, length must be less than or equal to `32`")
        if 'organization_id' in params and len(params['organization_id']) < 1:
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_file`, length must be greater than or equal to `1`")
        if 'organization_id' in params and not re.search('[a-zA-Z0-9-_]+', params['organization_id']):
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_file`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")

        collection_formats = {}

        path_params = {}
        if 'file_id' in params:
            path_params['fileId'] = params['file_id']

        query_params = []
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/xml', 'text/csv', 'application/pdf'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/hal+json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/sfs/v1/files/'+file_id, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_file_details(self, start_date, end_date, **kwargs):
        """
        Get list of files
        Get list of files and it's information of them available inside the report directory
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_file_details(start_date, end_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param date start_date: Valid start date in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd  (required)
        :param date end_date: Valid end date in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd  (required)
        :param str organization_id: Valid Cybersource Organization Id
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_file_details_with_http_info(start_date, end_date, **kwargs)
        else:
            (data) = self.get_file_details_with_http_info(start_date, end_date, **kwargs)
            return data

    def get_file_details_with_http_info(self, start_date, end_date, **kwargs):
        """
        Get list of files
        Get list of files and it's information of them available inside the report directory
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_file_details_with_http_info(start_date, end_date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param date start_date: Valid start date in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd  (required)
        :param date end_date: Valid end date in **ISO 8601 format** Please refer the following link to know more about ISO 8601 format. - https://xml2rfc.tools.ietf.org/public/rfc/html/rfc3339.html#anchor14   **Example date format:**   - yyyy-MM-dd  (required)
        :param str organization_id: Valid Cybersource Organization Id
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['start_date', 'end_date', 'organization_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_file_details" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'start_date' is set
        if ('start_date' not in params) or (params['start_date'] is None):
            raise ValueError("Missing the required parameter `start_date` when calling `get_file_details`")
        # verify the required parameter 'end_date' is set
        if ('end_date' not in params) or (params['end_date'] is None):
            raise ValueError("Missing the required parameter `end_date` when calling `get_file_details`")

        if 'organization_id' in params and len(params['organization_id']) > 32:
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_file_details`, length must be less than or equal to `32`")
        if 'organization_id' in params and len(params['organization_id']) < 1:
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_file_details`, length must be greater than or equal to `1`")
        if 'organization_id' in params and not re.search('[a-zA-Z0-9-_]+', params['organization_id']):
            raise ValueError("Invalid value for parameter `organization_id` when calling `get_file_details`, must conform to the pattern `/[a-zA-Z0-9-_]+/`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'start_date' in params:
            query_params.append(('startDate', params['start_date']))
        if 'end_date' in params:
            query_params.append(('endDate', params['end_date']))
        if 'organization_id' in params:
            query_params.append(('organizationId', params['organization_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/hal+json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/sfs/v1/file-details', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse2009',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)