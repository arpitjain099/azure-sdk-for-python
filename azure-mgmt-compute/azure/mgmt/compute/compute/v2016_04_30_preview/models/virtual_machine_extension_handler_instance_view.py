# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualMachineExtensionHandlerInstanceView(Model):
    """The instance view of a virtual machine extension handler.

    :param type: Full type of the extension handler which includes both
     publisher and type.
    :type type: str
    :param type_handler_version: The type version of the extension handler.
    :type type_handler_version: str
    :param status: The extension handler status.
    :type status: :class:`InstanceViewStatus
     <azure.mgmt.compute.compute.v20160430preview.models.InstanceViewStatus>`
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'type_handler_version': {'key': 'typeHandlerVersion', 'type': 'str'},
        'status': {'key': 'status', 'type': 'InstanceViewStatus'},
    }

    def __init__(self, type=None, type_handler_version=None, status=None):
        self.type = type
        self.type_handler_version = type_handler_version
        self.status = status
