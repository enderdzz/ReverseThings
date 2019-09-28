
#define _CRT_SECURE_NO_WARNINGS
#define BUFSZ 8
#include <iostream>
#include <cstdint>
#include <cstdio>

void encipher(unsigned int num_rounds, uint32_t v[2], uint32_t const key[4]) {
	unsigned int i;
	uint32_t v0 = v[0], v1 = v[1], sum = 0, delta = 0x9E3779B9;
	for (i = 0; i < num_rounds; i++) {
		v0 += (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3]);
		sum += delta;
		v1 += (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum >> 11) & 3]);
	}
	v[0] = v0; v[1] = v1;
	printf("%x %x\n", v0, v1);
}

void decipher(unsigned int num, uint32_t v[2], uint8_t const key[4]) {
	unsigned int i;
	uint32_t v0 = v[0], v1 = v[1], delta = 0x9e3779b9, sum = delta * num;
	for (i = 0; i < num; ++i) {
		v1 -= (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum >> 11) & 3]);
		sum -= delta; 
		v0 -= (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3]);
	}
	//v[0] = v0; v[1] = v1;
	unsigned char plain[BUFSZ] = { 0 };
	plain[0] = v0 & 0xff;
	plain[1] = (v0>>8) & 0xff;
	plain[2] = (v0 >> 16) & 0xff;
	plain[3] = (v0 >> 24) & 0xff;
	plain[4] = v1 & 0xff;
	plain[5] = (v1 >> 8) & 0xff;
	plain[6] = (v1 >> 16) & 0xff;
	plain[7] = (v1 >> 24) & 0xff;
	size_t readsz = sizeof(plain), j;
	//if (plain[0] == 'G' && plain[1] == 'I' && plain[2] == 'F') {
		for (j = 0; j < readsz; ++j) {
			printf("%c", plain[j]);
		}
		//puts("");
		//printf("%02x %02x %02x %02x\n", key[0], key[1], key[2], key[3]);
	//}
}

int main()
{
	uint8_t key[4] = { 0x31,0x73,0x35,0xb1 };
	unsigned char buf[BUFSZ] = { 0 };
	size_t bytes = 0, i, readsz = sizeof(buf);

	FILE *fp = fopen("best.gif.Mugatu","rb");
	//FILE* fp = fopen("the_key_to_success_0000.gif.Mugatu", "rb");
	freopen("ans2.gif", "wb", stdout);
	while ((bytes = fread(buf, sizeof(*buf), readsz, fp)) == readsz) {
		uint32_t num1 = (((uint32_t)buf[3]) << 24) | (((uint32_t)buf[2]) << 16) | (((uint32_t)buf[1]) << 8) | buf[0];
		uint32_t num2 = (((uint32_t)buf[7]) << 24) | (((uint32_t)buf[6]) << 16) | (((uint32_t)buf[5]) << 8) | buf[4];
		uint32_t tmp[2] = { num1, num2 };
		//for (i = 0; i < readsz; ++i) {
		//	printf("0x%02x ", buf[i]);
		//}
		//puts("");
		//uint32_t j;
		//for (j =0; j < (1<<24); ++j){
		//	uint8_t t_key[4] = { 0 };
		//	t_key[0] = 0x31;
		//	t_key[1] = j & 0xff;
		//	t_key[2] = (j >> 8) & 0xff;
		//	t_key[3] = (j >> 16) & 0xff;
		//	
		//	decipher(32, tmp, t_key);
		//}
		decipher(32, tmp, key);
	}
	//for (i = 0; i < bytes; ++i) {
	//	printf("0x%02x ", buf[i]);
	//}
	//puts("");

	//encipher(32, plain, key);

	
}
