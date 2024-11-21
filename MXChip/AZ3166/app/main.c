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

#include <stdio.h>

#include "tx_api.h"

#include "board_init.h"
#include "cmsis_utils.h"
#include "screen.h"
#include "wwd_networking.h"
// #include "zenoh-pico.h"

#include "cloud_config.h"
#include "sensor.h"

#define ECLIPSETX_THREAD_STACK_SIZE 4096
#define MQTT_THREAD_STACK_SIZE 4096
#define ECLIPSETX_THREAD_PRIORITY   4
#define MQTT_THREAD_PRIORITY 6

TX_THREAD eclipsetx_thread;
TX_THREAD mqtt_thread;
ULONG eclipsetx_thread_stack[ECLIPSETX_THREAD_STACK_SIZE / sizeof(ULONG)];
ULONG mqtt_thread_stack[MQTT_THREAD_STACK_SIZE / sizeof(ULONG)];

extern void thread_mqtt_entry(NX_IP *ip, NX_PACKET_POOL* pool);
extern void mqtt_thread_cyclic(char msg_buffer[], size_t buffer_size);

static void eclipsetx_thread_entry(ULONG parameter)
{
    UINT status;

    printf("Starting Eclipse ThreadX thread\r\n\r\n");

    // Initialize the network
    if ((status = wwd_network_init(WIFI_SSID, WIFI_PASSWORD, WIFI_MODE)))
    {
        printf("ERROR: Failed to initialize the network (0x%08x)\r\n", status);
    }

    // Connect to the network
    else if((status = wwd_network_connect()))
    {
        printf("ERROR: Failed to connect to the network (0x%08x)\r\n", status);
    }

    screen_print("Connected to WiFi",  L0);

    thread_mqtt_entry(&nx_ip, &nx_pool[0]);
    hts221_data_t data;

    while (1) {
      data = hts221_data_read();
      int humitidy = (int)data.humidity_perc;
      int temperature = (int)data.temperature_degC;
      char buffer[512];
      snprintf(buffer, sizeof(buffer), "{\"user\": \"ecub\", \"command\": \"to_ecuf\", \"data\": \"%d\"}", temperature);
    size_t buffer_length = strlen(buffer);
      printf("Temp: %d C\r\nHumidity: %d %%\r\n", temperature, humitidy);
      // screen_print(buffer, L1);
      mqtt_thread_cyclic(buffer, buffer_length);
      tx_thread_sleep(200);
    }
}

void tx_application_define(void* first_unused_memory)
{
    systick_interval_set(TX_TIMER_TICKS_PER_SECOND);

    // Create ThreadX thread
    UINT status = tx_thread_create(&eclipsetx_thread,
        "Eclipse ThreadX Thread",
        eclipsetx_thread_entry,
        0,
        eclipsetx_thread_stack,
        ECLIPSETX_THREAD_STACK_SIZE,
        ECLIPSETX_THREAD_PRIORITY,
        ECLIPSETX_THREAD_PRIORITY,
        TX_NO_TIME_SLICE,
        TX_AUTO_START);

    if (status != TX_SUCCESS) {
      printf("ERROR: Eclipse ThreadX thread creation failed\r\n");
    }



}

int main(void)
{
    // Initialize the board
    board_init();

    // Enter the ThreadX kernel
    tx_kernel_enter();

    return 0;
}
