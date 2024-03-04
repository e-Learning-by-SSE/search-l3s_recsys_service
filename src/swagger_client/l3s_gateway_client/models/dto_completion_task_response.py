# coding: utf-8

"""
    L3S Gateway for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DtoCompletionTaskResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'unit_id': 'str',
        'existing_skills': 'list[str]',
        'new_skills': 'list[str]',
        'title': 'str',
        'summary': 'str',
        'content_tags': 'list[str]',
        'context_tags': 'list[str]'
    }

    attribute_map = {
        'unit_id': 'unit_id',
        'existing_skills': 'existing_skills',
        'new_skills': 'new_skills',
        'title': 'title',
        'summary': 'summary',
        'content_tags': 'content_tags',
        'context_tags': 'context_tags'
    }

    def __init__(self, unit_id=None, existing_skills=None, new_skills=None, title=None, summary=None, content_tags=None, context_tags=None):  # noqa: E501
        """DtoCompletionTaskResponse - a model defined in Swagger"""  # noqa: E501
        self._unit_id = None
        self._existing_skills = None
        self._new_skills = None
        self._title = None
        self._summary = None
        self._content_tags = None
        self._context_tags = None
        self.discriminator = None
        if unit_id is not None:
            self.unit_id = unit_id
        if existing_skills is not None:
            self.existing_skills = existing_skills
        if new_skills is not None:
            self.new_skills = new_skills
        if title is not None:
            self.title = title
        if summary is not None:
            self.summary = summary
        if content_tags is not None:
            self.content_tags = content_tags
        if context_tags is not None:
            self.context_tags = context_tags

    @property
    def unit_id(self):
        """Gets the unit_id of this DtoCompletionTaskResponse.  # noqa: E501


        :return: The unit_id of this DtoCompletionTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        """Sets the unit_id of this DtoCompletionTaskResponse.


        :param unit_id: The unit_id of this DtoCompletionTaskResponse.  # noqa: E501
        :type: str
        """

        self._unit_id = unit_id

    @property
    def existing_skills(self):
        """Gets the existing_skills of this DtoCompletionTaskResponse.  # noqa: E501

        list of skill ids  # noqa: E501

        :return: The existing_skills of this DtoCompletionTaskResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._existing_skills

    @existing_skills.setter
    def existing_skills(self, existing_skills):
        """Sets the existing_skills of this DtoCompletionTaskResponse.

        list of skill ids  # noqa: E501

        :param existing_skills: The existing_skills of this DtoCompletionTaskResponse.  # noqa: E501
        :type: list[str]
        """

        self._existing_skills = existing_skills

    @property
    def new_skills(self):
        """Gets the new_skills of this DtoCompletionTaskResponse.  # noqa: E501

        list of skill ids  # noqa: E501

        :return: The new_skills of this DtoCompletionTaskResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._new_skills

    @new_skills.setter
    def new_skills(self, new_skills):
        """Sets the new_skills of this DtoCompletionTaskResponse.

        list of skill ids  # noqa: E501

        :param new_skills: The new_skills of this DtoCompletionTaskResponse.  # noqa: E501
        :type: list[str]
        """

        self._new_skills = new_skills

    @property
    def title(self):
        """Gets the title of this DtoCompletionTaskResponse.  # noqa: E501


        :return: The title of this DtoCompletionTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DtoCompletionTaskResponse.


        :param title: The title of this DtoCompletionTaskResponse.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def summary(self):
        """Gets the summary of this DtoCompletionTaskResponse.  # noqa: E501


        :return: The summary of this DtoCompletionTaskResponse.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this DtoCompletionTaskResponse.


        :param summary: The summary of this DtoCompletionTaskResponse.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def content_tags(self):
        """Gets the content_tags of this DtoCompletionTaskResponse.  # noqa: E501


        :return: The content_tags of this DtoCompletionTaskResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._content_tags

    @content_tags.setter
    def content_tags(self, content_tags):
        """Sets the content_tags of this DtoCompletionTaskResponse.


        :param content_tags: The content_tags of this DtoCompletionTaskResponse.  # noqa: E501
        :type: list[str]
        """

        self._content_tags = content_tags

    @property
    def context_tags(self):
        """Gets the context_tags of this DtoCompletionTaskResponse.  # noqa: E501


        :return: The context_tags of this DtoCompletionTaskResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._context_tags

    @context_tags.setter
    def context_tags(self, context_tags):
        """Sets the context_tags of this DtoCompletionTaskResponse.


        :param context_tags: The context_tags of this DtoCompletionTaskResponse.  # noqa: E501
        :type: list[str]
        """

        self._context_tags = context_tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(DtoCompletionTaskResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DtoCompletionTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other