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

from enum import Enum


class ApplicationGatewaySkuName(Enum):

    standard_small = "Standard_Small"
    standard_medium = "Standard_Medium"
    standard_large = "Standard_Large"


class ApplicationGatewayTier(Enum):

    standard = "Standard"


class IPAllocationMethod(Enum):

    static = "Static"
    dynamic = "Dynamic"


class TransportProtocol(Enum):

    udp = "Udp"
    tcp = "Tcp"


class SecurityRuleProtocol(Enum):

    tcp = "Tcp"
    udp = "Udp"
    asterisk = "*"


class SecurityRuleAccess(Enum):

    allow = "Allow"
    deny = "Deny"


class SecurityRuleDirection(Enum):

    inbound = "Inbound"
    outbound = "Outbound"


class RouteNextHopType(Enum):

    virtual_network_gateway = "VirtualNetworkGateway"
    vnet_local = "VnetLocal"
    internet = "Internet"
    virtual_appliance = "VirtualAppliance"
    none = "None"


class ApplicationGatewayProtocol(Enum):

    http = "Http"
    https = "Https"


class ApplicationGatewayCookieBasedAffinity(Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class ApplicationGatewayRequestRoutingRuleType(Enum):

    basic = "Basic"
    path_based_routing = "PathBasedRouting"


class ApplicationGatewayOperationalState(Enum):

    stopped = "Stopped"
    starting = "Starting"
    running = "Running"
    stopping = "Stopping"


class LoadDistribution(Enum):

    default = "Default"
    source_ip = "SourceIP"
    source_ip_protocol = "SourceIPProtocol"


class ProbeProtocol(Enum):

    http = "Http"
    tcp = "Tcp"


class VirtualNetworkGatewayType(Enum):

    vpn = "Vpn"
    express_route = "ExpressRoute"


class VpnType(Enum):

    policy_based = "PolicyBased"
    route_based = "RouteBased"


class VirtualNetworkGatewaySkuName(Enum):

    basic = "Basic"
    high_performance = "HighPerformance"
    standard = "Standard"


class VirtualNetworkGatewaySkuTier(Enum):

    basic = "Basic"
    high_performance = "HighPerformance"
    standard = "Standard"


class ProcessorArchitecture(Enum):

    amd64 = "Amd64"
    x86 = "X86"


class VirtualNetworkGatewayConnectionType(Enum):

    ipsec = "IPsec"
    vnet2_vnet = "Vnet2Vnet"
    express_route = "ExpressRoute"
    vpn_client = "VPNClient"


class VirtualNetworkGatewayConnectionStatus(Enum):

    unknown = "Unknown"
    connecting = "Connecting"
    connected = "Connected"
    not_connected = "NotConnected"


class AuthorizationUseStatus(Enum):

    available = "Available"
    in_use = "InUse"


class ExpressRouteCircuitPeeringAdvertisedPublicPrefixState(Enum):

    not_configured = "NotConfigured"
    configuring = "Configuring"
    configured = "Configured"
    validation_needed = "ValidationNeeded"


class ExpressRouteCircuitPeeringType(Enum):

    azure_public_peering = "AzurePublicPeering"
    azure_private_peering = "AzurePrivatePeering"
    microsoft_peering = "MicrosoftPeering"


class ExpressRouteCircuitPeeringState(Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class ExpressRouteCircuitSkuTier(Enum):

    standard = "Standard"
    premium = "Premium"


class ExpressRouteCircuitSkuFamily(Enum):

    unlimited_data = "UnlimitedData"
    metered_data = "MeteredData"


class ServiceProviderProvisioningState(Enum):

    not_provisioned = "NotProvisioned"
    provisioning = "Provisioning"
    provisioned = "Provisioned"
    deprovisioning = "Deprovisioning"


class NetworkOperationStatus(Enum):

    in_progress = "InProgress"
    succeeded = "Succeeded"
    failed = "Failed"
