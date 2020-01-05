#include "aes.h"

#include <stdint.h>
#include <stdio.h>
#include <string.h>

static char flag[] =
        "\x3a\x2e\x82\xaa\xb5\x84\xdd\x4c\x81\xd0\x92\x7b\xab\xa0\x23\x48"
        "\x31\x2a\x4f\x6a\x99\xb4\x6a\x5a\xa8\x41\xcf\xaa\x95\xeb\xcd\xe6";

static uint8_t iv[16]  = { 0xf0, 0xf1, 0xf2, 0xf3, 0xf4, 0xf5, 0xf6, 0xf7,
                           0xf8, 0xf9, 0xfa, 0xfb, 0xfc, 0xfd, 0xfe, 0xff };

int hex2bin(char c)
{
    if ((c >= '0') && (c <= '9'))
    {
        return c - '0';
    }

    if ((c >= 'a') && (c <= 'f'))
    {
        return c - 'a' + 10;
    }
    return 0;
}

static void unhexlify(char *hex_str)
{
    int len = strlen(hex_str);
    for (int i = 0; i < (len / 2); ++i)
    {
        hex_str[i] = hex2bin(hex_str[2 * i]) | hex2bin(hex_str[2 * i + 1]);
    }
}

int main(int argc, char **argv)
{
    struct AES_ctx ctx = {0};

    char key[sizeof(DEC_KEY)];
    strcpy(key, DEC_KEY);
    unhexlify(key);

    AES_init_ctx_iv(&ctx, (uint8_t *)key, iv);
    AES_CBC_decrypt_buffer(&ctx, flag, sizeof(flag) - 1);
    printf("flag: %s\n", flag);
    return 0;
}