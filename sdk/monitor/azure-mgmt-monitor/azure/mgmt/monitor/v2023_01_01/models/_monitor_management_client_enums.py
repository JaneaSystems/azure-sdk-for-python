# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class ReceiverStatus(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """Indicates the status of the receiver. Receivers that are not Enabled will not receive any
    communications.
    """

    NOT_SPECIFIED = "NotSpecified"
    ENABLED = "Enabled"
    DISABLED = "Disabled"