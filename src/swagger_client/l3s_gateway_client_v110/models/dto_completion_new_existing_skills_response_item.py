# coding: utf-8

"""
    L3S Gateway for SEARCH

    Welcome to the Swagger UI documentation site!  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DtoCompletionNewExistingSkillsResponseItem(object):
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
        'task_id': 'str',
        'new_skills': 'list[str]',
        'existing_skills': 'list[str]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'new_skills': 'new_skills',
        'existing_skills': 'existing_skills'
    }

    def __init__(self, task_id=None, new_skills=None, existing_skills=None):  # noqa: E501
        """DtoCompletionNewExistingSkillsResponseItem - a model defined in Swagger"""  # noqa: E501
        self._task_id = None
        self._new_skills = None
        self._existing_skills = None
        self.discriminator = None
        if task_id is not None:
            self.task_id = task_id
        if new_skills is not None:
            self.new_skills = new_skills
        if existing_skills is not None:
            self.existing_skills = existing_skills

    @property
    def task_id(self):
        """Gets the task_id of this DtoCompletionNewExistingSkillsResponseItem.  # noqa: E501

        The task ID  # noqa: E501

        :return: The task_id of this DtoCompletionNewExistingSkillsResponseItem.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this DtoCompletionNewExistingSkillsResponseItem.

        The task ID  # noqa: E501

        :param task_id: The task_id of this DtoCompletionNewExistingSkillsResponseItem.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def new_skills(self):
        """Gets the new_skills of this DtoCompletionNewExistingSkillsResponseItem.  # noqa: E501

        List of new skills in the learning task  # noqa: E501

        :return: The new_skills of this DtoCompletionNewExistingSkillsResponseItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._new_skills

    @new_skills.setter
    def new_skills(self, new_skills):
        """Sets the new_skills of this DtoCompletionNewExistingSkillsResponseItem.

        List of new skills in the learning task  # noqa: E501

        :param new_skills: The new_skills of this DtoCompletionNewExistingSkillsResponseItem.  # noqa: E501
        :type: list[str]
        """

        self._new_skills = new_skills

    @property
    def existing_skills(self):
        """Gets the existing_skills of this DtoCompletionNewExistingSkillsResponseItem.  # noqa: E501

        List of existing skills ids for the learning task  # noqa: E501

        :return: The existing_skills of this DtoCompletionNewExistingSkillsResponseItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._existing_skills

    @existing_skills.setter
    def existing_skills(self, existing_skills):
        """Sets the existing_skills of this DtoCompletionNewExistingSkillsResponseItem.

        List of existing skills ids for the learning task  # noqa: E501

        :param existing_skills: The existing_skills of this DtoCompletionNewExistingSkillsResponseItem.  # noqa: E501
        :type: list[str]
        """

        self._existing_skills = existing_skills

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
        if issubclass(DtoCompletionNewExistingSkillsResponseItem, dict):
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
        if not isinstance(other, DtoCompletionNewExistingSkillsResponseItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
