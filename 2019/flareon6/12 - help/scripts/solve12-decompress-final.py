import ctypes
from binascii import unhexlify
nt   =  ctypes.windll.ntdll
def decompress_buffer(data):
    final_size = ctypes.c_ulong(0)
    uncompressed =ctypes.c_buffer(0x7c00)
    nt.RtlDecompressBuffer(0x102,uncompressed,0x1000,ctypes.c_char_p(data),0xa00,ctypes.byref(final_size))
    return uncompressed.raw
def main():
    a = '09b90003d9a29a65fb4bb500030000000400030000ea77fe19346a5b2f00146570e1fc89a10000d396909aeb51a52c00459ef8cd145e4e460606009c010c0892b3f78a00016db159adcde4da008836e62c3021bc050088dcd434ca60a10a004341186c759f148a00ae473fd28f725a080089b23c4a0c766ebd004cf044896848553600c22d4660ea0000d200bc05bfd621d3cdb300a91d94190c158255007d52dd5d186a585e00a1d0787f97cbee830079f14666a78f808600993dc6b8f1fe210c000cb3da187c2ea13b00db9f47f456c2873c00a86fce88c4f9ba7d00b69a4295e8c74f5a00ac9a6324c12262f70032e64ac04464d6d8006b18b719e2b3ddcb0007c139c67b489baa002416f4dfa5c4e74200f163edae1cfa07b600983c67805121570d00e37e7156c80ee0ec0068b7ff40ea715ab8004ec97e537dad3e8e001b1cd8f8eb7bae6e00821085e22a1dc495002c836d365c6ffb4a00c766474b39b863df00c2ffefeccc3118cf003401262874d5556c004c3119c422081ffa00c0a7bd5c191d5e9c00354002e9fd63f2ef0094077d3d72ad427b00a40d994b2eb0c00f00fb18441b74a5be24007a5cdf7175fc977e00cdb578754582324800ac91803b073b06380091b0f05cc913cda00099ddb13e86d8343e00d6b8626337893f6c007e66239164102b660043316a8ba9c806c700946f48ef817aa5e3003074b0d97ca79ad700cbacf8a9eff0c98a0077f17ece88dc1a90000ad1b341f74c4d870068001bfc2573a80b00f538738a15db75df00ca7e228372844ffb004ba0f90ff5b3595d00162e38d038cfe9c30044c6e3d5d7d87d3c006af7e239667073660012b9f1c65ac7e18d00a81e2cc0b181c06700064ba4e2298f4cf600d3bfee325c9bf081009f7edf08e9a09c1500a8fe6953e7e013fc009bb4caac0459072c00d565cbe1342ac4d10051aea53f4f6820bf00aed974a0af9deab400fa8801af986c41cc00d2648a2128cf527d002b579c76988b766a00587b6348f54fd87b008c9516dcbee50d8e0060dda8523dd33dfe00c4a8727f91e1f5d8003a0faba1ce8bd39b008e246fd9b315ae2400c829227cf188402600f86ceef8b7f8c636005a1ab04df9d6be6000706000829594ce7c002c9143c93ea804db00267ee79e388303cf003ffd6fd7a3f487e8002a92b713db4270c6006ac44a78c9b7fd1d004a964bc6aa1b533a007da9cd8164d8c2bb00bbb428d3d1c97cbf00802b2142c98d5ff300309977a40758d32d00350ab173fcb83896004478383efb8bace100d63eb17d18a5beff008fbe91258c2dfa54009be4dafc6d190aa10098ba73aa9665730700df74d608733a8fd700a6b48da89763e27b0013ba77d35d47b62a0045ea452ca8f5a1630089d977b46ff7a94c000bc36a4296b5057f008eea6bd7f88ec77800a136d3f03f93cf0b0090886c140bf1a657007f572c58491c668900f36d82c9c6609b7900d08790a974b1c29c005290529db408b388001074d79362309775007430c0efb886e9f0000eb0ffd9dc8aca3100a4341f1532a66b93007be8866dc07ee4bb00288c815683277f7500b2abf381b3587b1d00ef3af6f9a18c7ea400414473705830053e0068d3157445deeff9001851cc4f0682f3db00eac9d1e29a48f94b005e39cc08eb07be97001887f7fa6cfdfef60074b4b95dd36a5d9600571ddccd88010db800d3750548fc8d72360064c88f551526c3d700b7b3935df6042aa700f7230559610b35f80013ffe9b22236e38900da1fe13c730c09cd00742a7635bd551ee1000573b517d27149be003efb763e3f9a847b0084a7c6354feb3ed600837e394241d4c739007a0240e994c5cf720016a90aa58acff0540095af368c5f67092400023f86d5f2600af900e56dd9f469f1312b00339f940d7a76a0b700158a210765a4ef3300287862623681157e00aa517e0e9733e776006603495791401b250086e84ef7f8408bb600ebd3c011b7aafdc700d2a22fedbebf34eb0077d6bf4699146fe1006eed9869a6fe43ab009a2cebc72b1cf41400930a6dd6f0bb80cd00c6e626801d2f3a2500e7812b135563dfa7001fa0dc2ef5828747004f5f34f91bddeb9800cc65c79332c1858c005ff24bffb46c60df00dc801438bcf9957f002707b1cd4b8ee11000d5b7abbc2c2b1afc0055bf5a2364ed32cc000f430c68bbe999170082d50763ef6594c50050ea90d04822c90600a94e70de7162d3bb00bc496123b97303680025e382490dccce4000a43492934c70cc9100d02a11c069a8ed00003ccb0dff242845f900b2b8d318fa37836300f1b82d8839ff5a40006af1ebd75e277e83000b5c0ef1bc8789c400f5483d0cdcac4acc0091995ba618de8ac400dbbea91430bbd7f300358e98b4cca48c36009603f098a454224500c180cb76bbe7c3b80095d73e3581c3367100cb54af3db294059e005359a5880b4c749e005be3b1b7d9ac42cb0077306d1d69ddec9100e2c4558d6550b43c00a32f92a365691fcc00686269e72b4fac6300804c5f8909b3fea800f6c701759cdfd45b007b34feccd5b9bf7d00d450ec6a10425062001a319285366661cc00a96a54a86075a58e004dcd964aa49024cd0086a44f50f90e60fb00e8ccbca642dc174e009ae7000a68f0d5b1006b716e7a7419f7ae00021015434bf930c10062ce46e31203da97006e4f39a8d503677400f654f983818258bc008ad99e2430566fa400123d2f5de5eda2c50029a2ddfe1fa2699000bcd356519ef2fe7600a907291b120b116500b036554109402fa4008d43710bdeb73ede005e7ffe7584fc7cbf00c10782cc0e477ce300949808afcc62251c0035ece1c60f729f0d009ef6d390fa02ef1d007b86b03ca6467f04003c22fe0a94a73cd5005b2a55aee56b54880005e46b77cf0478ee008e88e68e2cacea35006b7246cf427021cb0084ca4a372a1a901f005746b14683fa22370044e9a76ef371954400d7f2da4816f9acdf00ef93eba70b380de60040ea659ea1dc9fdb004be550edfaace1e3002a9067f76bc0b81d009e10c60d360d4c4c0083dd05329e6d2ae600c477a1d20a900a3000a83df77dd14530a700d4eb365c2c373cbd0081b73e4523e59594005262486af6ab65d1008fb25f07aa4ee94e00299f8a9ff155c94700a61e9e4296e189e200b08759d52257a76700705a48fb8c0f5b7e004298cd97ca812b520031e4b29a04162be200866d39cfa51db1e7005b3a0471869b9f'
    a = unhexlify(a)
    b = decompress_buffer(a)
    print(b)
if __name__ == '__main__':
    main()
	
	f0ll0w_th3_br34dcrumbs@flare-on.com