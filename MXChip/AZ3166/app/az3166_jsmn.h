#include <string.h>
#include <stdio.h>
#include "jsmn.h"

static char *JSON_FAIL_MSG = "Failed to parse JSON";
static char json_user[20] = "\0";
static char json_command[20] = "\0";
static char json_data[20] = "\0";

char* az3166_parse(const char *mqtt_payload)
{
    char *ret = NULL;
    int retVal = 0;
    jsmn_parser self;
    jsmntok_t tokens[12]; /* We expect no more than 12 tokens */

    printf("%s\r\n", mqtt_payload);
    jsmn_init(&self);
    retVal = jsmn_parse(&self, mqtt_payload, strlen(mqtt_payload),
                    tokens, sizeof(tokens) / sizeof(tokens[0]));
    if (retVal < 0)
    {
        ret = JSON_FAIL_MSG;;
    }

    sprintf(json_user, "user: %.*s", tokens[2].end - tokens[2].start,
            mqtt_payload + tokens[2].start);
    sprintf(json_command, "cmd: %.*s", tokens[4].end - tokens[4].start,
            mqtt_payload + tokens[4].start);
    sprintf(json_data, "data: %.*s", tokens[6].end - tokens[6].start,
            mqtt_payload + tokens[6].start);

    printf("%s\r\n", json_user);
    printf("%s\r\n", json_command);
    printf("%s\r\n", json_data);

    return ret;
}
