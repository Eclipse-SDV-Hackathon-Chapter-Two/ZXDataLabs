/*
 * Copyright (c) Microsoft
 * Copyright (c) 2024 Eclipse Foundation
 *
 *  This program and the accompanying materials are made available
 *  under the terms of the MIT license which is available at
 *  https://opensource.org/license/mit.
 *
 *  SPDX-License-Identifier: MIT
 *
 *  Contributors:
 *     Microsoft         - Initial version
 *     Frédéric Desbiens - 2024 version.
 */

#ifndef _CLOUD_CONFIG_H
#define _CLOUD_CONFIG_H

typedef enum
{
    None         = 0,
    WEP          = 1,
    WPA_PSK_TKIP = 2,
    WPA2_PSK_AES = 3
} WiFi_Mode;

// ----------------------------------------------------------------------------
// WiFi connection config
// ----------------------------------------------------------------------------
#define HOSTNAME      "ecub_1"  //Change to unique hostname.
// Hackathon
// #define WIFI_SSID     "ICF_Gast"
// #define WIFI_PASSWORD "icfwlan11"
// Nikos
#define WIFI_SSID "TP-Link_8277"
#define WIFI_PASSWORD "66636847"
// #define WIFI_SSID     "IwansIphone"
// #define WIFI_PASSWORD "iwannavi2211"
#define WIFI_MODE     WPA2_PSK_AES

#endif // _CLOUD_CONFIG_H
