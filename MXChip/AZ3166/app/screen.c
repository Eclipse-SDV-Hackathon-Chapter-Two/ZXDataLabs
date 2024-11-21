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

#include "screen.h"

#include "ssd1306.h"

void zxdatalabs_screen_print(char *user, char *cmd, char *data)
{
    ssd1306_Fill(Black);
    ssd1306_SetCursor(2, L0);
    ssd1306_WriteString(user, Font_7x10, White);
    ssd1306_SetCursor(2, L1);
    ssd1306_WriteString(cmd, Font_7x10, White);
    ssd1306_SetCursor(2, L2);
    ssd1306_WriteString(data, Font_7x10, White);
    ssd1306_UpdateScreen();
}

void screen_print(char* str, LINE_NUM line)
{
    ssd1306_Fill(Black);
    ssd1306_SetCursor(2, line);
    ssd1306_WriteString(str, Font_6x8, White);
    ssd1306_UpdateScreen();
}

void screen_printn(const char* str, unsigned int str_length, LINE_NUM line)
{
    ssd1306_Fill(Black);
    ssd1306_SetCursor(2, line);

    for (unsigned int i = 0; i < str_length; ++i)
    {
        if (ssd1306_WriteChar(str[i], Font_6x8, White) != str[i])
        {
            return;
        }
    }

    ssd1306_UpdateScreen();
}
