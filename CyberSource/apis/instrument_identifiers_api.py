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


class InstrumentIdentifiersApi(object):
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
        self.api_client.set_configuration(merchant_config)


    def tms_v1_instrumentidentifiers_post(self, profile_id, body, **kwargs):
        """
        Create an Instrument Identifier
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tms_v1_instrumentidentifiers_post(profile_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str profile_id: The id of a profile containing user specific TMS configuration. (required)
        :param Body body: Please specify either a Card or Bank Account. (required)
        :return: TmsV1InstrumentidentifiersPost200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.tms_v1_instrumentidentifiers_post_with_http_info(profile_id, body, **kwargs)
        else:
            (data) = self.tms_v1_instrumentidentifiers_post_with_http_info(profile_id, body, **kwargs)
            return data

    def tms_v1_instrumentidentifiers_post_with_http_info(self, profile_id, body, **kwargs):
        """
        Create an Instrument Identifier
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.tms_v1_instrumentidentifiers_post_with_http_info(profile_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str profile_id: The id of a profile containing user specific TMS configuration. (required)
        :param Body body: Please specify either a Card or Bank Account. (required)
        :return: TmsV1InstrumentidentifiersPost200Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['profile_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tms_v1_instrumentidentifiers_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'profile_id' is set
        if ('profile_id' not in params) or (params['profile_id'] is None):
            raise ValueError("Missing the required parameter `profile_id` when calling `tms_v1_instrumentidentifiers_post`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `tms_v1_instrumentidentifiers_post`")

        '''if 'profile_id' in params and params['profile_id'] > 36:
            raise ValueError("Invalid value for parameter `profile_id` when calling `tms_v1_instrumentidentifiers_post`, must be a value less than or equal to `36`")
        if 'profile_id' in params and params['profile_id'] < 36:
            raise ValueError("Invalid value for parameter `profile_id` when calling `tms_v1_instrumentidentifiers_post`, must be a value greater than or equal to `36`")'''

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'profile_id' in params:
            header_params['profile-id'] = params['profile_id']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        #header_params['Content-Type'] = self.api_client.\
            #select_header_content_type(['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/tms/v1/instrumentidentifiers', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TmsV1InstrumentidentifiersPost200Response',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
