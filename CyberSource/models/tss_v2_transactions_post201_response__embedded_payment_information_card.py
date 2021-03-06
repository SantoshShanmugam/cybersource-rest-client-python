# coding: utf-8

"""
    CyberSource Flex API

    Simple PAN tokenization service

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'suffix': 'str',
        'prefix': 'str',
        'type': 'str'
    }

    attribute_map = {
        'suffix': 'suffix',
        'prefix': 'prefix',
        'type': 'type'
    }

    def __init__(self, suffix=None, prefix=None, type=None):
        """
        TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard - a model defined in Swagger
        """

        self._suffix = None
        self._prefix = None
        self._type = None

        if suffix is not None:
          self.suffix = suffix
        if prefix is not None:
          self.prefix = prefix
        if type is not None:
          self.type = type

    @property
    def suffix(self):
        """
        Gets the suffix of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard.
        Last four digits of the cardholder’s account number. This field is returned only for tokenized transactions. You can use this value on the receipt that you give to the cardholder. 

        :return: The suffix of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard.
        Last four digits of the cardholder’s account number. This field is returned only for tokenized transactions. You can use this value on the receipt that you give to the cardholder. 

        :param suffix: The suffix of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard.
        :type: str
        """
        if suffix is not None and len(suffix) > 4:
            raise ValueError("Invalid value for `suffix`, length must be less than or equal to `4`")

        self._suffix = suffix

    @property
    def prefix(self):
        """
        Gets the prefix of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard.
        The description for this field is not available.

        :return: The prefix of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard.
        The description for this field is not available.

        :param prefix: The prefix of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard.
        :type: str
        """
        if prefix is not None and len(prefix) > 6:
            raise ValueError("Invalid value for `prefix`, length must be less than or equal to `6`")

        self._prefix = prefix

    @property
    def type(self):
        """
        Gets the type of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard.
        Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover 

        :return: The type of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard.
        Type of card to authorize. - 001 Visa - 002 Mastercard - 003 Amex - 004 Discover 

        :param type: The type of this TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard.
        :type: str
        """
        if type is not None and len(type) > 3:
            raise ValueError("Invalid value for `type`, length must be less than or equal to `3`")

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TssV2TransactionsPost201ResponseEmbeddedPaymentInformationCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
