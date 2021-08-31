# coding: utf-8

"""
    蓝鲸用户管理 API

    蓝鲸用户管理后台服务 API  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CreateCategory(object):
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
        'id': 'int',
        'configured': 'bool',
        'syncing': 'bool',
        'unfilled_namespaces': 'list[str]',
        'display_name': 'str',
        'domain': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'type': 'str',
        'description': 'str',
        'default': 'bool',
        'enabled': 'bool',
        'status': 'str',
        'order': 'int',
        'last_synced_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'configured': 'configured',
        'syncing': 'syncing',
        'unfilled_namespaces': 'unfilled_namespaces',
        'display_name': 'display_name',
        'domain': 'domain',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'type': 'type',
        'description': 'description',
        'default': 'default',
        'enabled': 'enabled',
        'status': 'status',
        'order': 'order',
        'last_synced_time': 'last_synced_time'
    }

    def __init__(self, id=None, configured=None, syncing=None, unfilled_namespaces=None, display_name=None, domain=None, create_time=None, update_time=None, type=None, description=None, default=None, enabled=None, status=None, order=None, last_synced_time=None):  # noqa: E501
        """CreateCategory - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._configured = None
        self._syncing = None
        self._unfilled_namespaces = None
        self._display_name = None
        self._domain = None
        self._create_time = None
        self._update_time = None
        self._type = None
        self._description = None
        self._default = None
        self._enabled = None
        self._status = None
        self._order = None
        self._last_synced_time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if configured is not None:
            self.configured = configured
        self.syncing = syncing
        if unfilled_namespaces is not None:
            self.unfilled_namespaces = unfilled_namespaces
        self.display_name = display_name
        self.domain = domain
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        self.type = type
        if description is not None:
            self.description = description
        if default is not None:
            self.default = default
        if enabled is not None:
            self.enabled = enabled
        if status is not None:
            self.status = status
        if order is not None:
            self.order = order
        if last_synced_time is not None:
            self.last_synced_time = last_synced_time

    @property
    def id(self):
        """Gets the id of this CreateCategory.  # noqa: E501


        :return: The id of this CreateCategory.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateCategory.


        :param id: The id of this CreateCategory.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def configured(self):
        """Gets the configured of this CreateCategory.  # noqa: E501


        :return: The configured of this CreateCategory.  # noqa: E501
        :rtype: bool
        """
        return self._configured

    @configured.setter
    def configured(self, configured):
        """Sets the configured of this CreateCategory.


        :param configured: The configured of this CreateCategory.  # noqa: E501
        :type: bool
        """

        self._configured = configured

    @property
    def syncing(self):
        """Gets the syncing of this CreateCategory.  # noqa: E501


        :return: The syncing of this CreateCategory.  # noqa: E501
        :rtype: bool
        """
        return self._syncing

    @syncing.setter
    def syncing(self, syncing):
        """Sets the syncing of this CreateCategory.


        :param syncing: The syncing of this CreateCategory.  # noqa: E501
        :type: bool
        """
        if syncing is None:
            raise ValueError("Invalid value for `syncing`, must not be `None`")  # noqa: E501

        self._syncing = syncing

    @property
    def unfilled_namespaces(self):
        """Gets the unfilled_namespaces of this CreateCategory.  # noqa: E501


        :return: The unfilled_namespaces of this CreateCategory.  # noqa: E501
        :rtype: list[str]
        """
        return self._unfilled_namespaces

    @unfilled_namespaces.setter
    def unfilled_namespaces(self, unfilled_namespaces):
        """Sets the unfilled_namespaces of this CreateCategory.


        :param unfilled_namespaces: The unfilled_namespaces of this CreateCategory.  # noqa: E501
        :type: list[str]
        """

        self._unfilled_namespaces = unfilled_namespaces

    @property
    def display_name(self):
        """Gets the display_name of this CreateCategory.  # noqa: E501


        :return: The display_name of this CreateCategory.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this CreateCategory.


        :param display_name: The display_name of this CreateCategory.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def domain(self):
        """Gets the domain of this CreateCategory.  # noqa: E501


        :return: The domain of this CreateCategory.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this CreateCategory.


        :param domain: The domain of this CreateCategory.  # noqa: E501
        :type: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")  # noqa: E501

        self._domain = domain

    @property
    def create_time(self):
        """Gets the create_time of this CreateCategory.  # noqa: E501


        :return: The create_time of this CreateCategory.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CreateCategory.


        :param create_time: The create_time of this CreateCategory.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this CreateCategory.  # noqa: E501


        :return: The update_time of this CreateCategory.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this CreateCategory.


        :param update_time: The update_time of this CreateCategory.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

    @property
    def type(self):
        """Gets the type of this CreateCategory.  # noqa: E501


        :return: The type of this CreateCategory.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateCategory.


        :param type: The type of this CreateCategory.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["local", "mad", "ldap", "tof", "custom", "pluggable"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def description(self):
        """Gets the description of this CreateCategory.  # noqa: E501


        :return: The description of this CreateCategory.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateCategory.


        :param description: The description of this CreateCategory.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def default(self):
        """Gets the default of this CreateCategory.  # noqa: E501


        :return: The default of this CreateCategory.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this CreateCategory.


        :param default: The default of this CreateCategory.  # noqa: E501
        :type: bool
        """

        self._default = default

    @property
    def enabled(self):
        """Gets the enabled of this CreateCategory.  # noqa: E501


        :return: The enabled of this CreateCategory.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreateCategory.


        :param enabled: The enabled of this CreateCategory.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def status(self):
        """Gets the status of this CreateCategory.  # noqa: E501


        :return: The status of this CreateCategory.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateCategory.


        :param status: The status of this CreateCategory.  # noqa: E501
        :type: str
        """
        allowed_values = ["normal", "inactive"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def order(self):
        """Gets the order of this CreateCategory.  # noqa: E501


        :return: The order of this CreateCategory.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CreateCategory.


        :param order: The order of this CreateCategory.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def last_synced_time(self):
        """Gets the last_synced_time of this CreateCategory.  # noqa: E501


        :return: The last_synced_time of this CreateCategory.  # noqa: E501
        :rtype: datetime
        """
        return self._last_synced_time

    @last_synced_time.setter
    def last_synced_time(self, last_synced_time):
        """Sets the last_synced_time of this CreateCategory.


        :param last_synced_time: The last_synced_time of this CreateCategory.  # noqa: E501
        :type: datetime
        """

        self._last_synced_time = last_synced_time

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
        if issubclass(CreateCategory, dict):
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
        if not isinstance(other, CreateCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
