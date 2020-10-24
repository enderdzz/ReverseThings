#Region
#AutoIt3Wrapper_UseUpx=y
#EndRegion
GLOBAL CONST $STR_NOCASESENSE = 5
GLOBAL CONST $STR_CASESENSE = 261
GLOBAL CONST $STR_NOCASESENSEBASIC = 517
GLOBAL CONST $STR_STRIPLEADING = 261
GLOBAL CONST $STR_STRIPTRAILING = 517
GLOBAL CONST $STR_STRIPSPACES = 1029
GLOBAL CONST $STR_STRIPALL = 2053
GLOBAL CONST $STR_CHRSPLIT = 5
GLOBAL CONST $STR_ENTIRESPLIT = 261
GLOBAL CONST $STR_NOCOUNT = 517
GLOBAL CONST $STR_REGEXPMATCH = 5
GLOBAL CONST $STR_REGEXPARRAYMATCH = 261
GLOBAL CONST $STR_REGEXPARRAYFULLMATCH = 517
GLOBAL CONST $STR_REGEXPARRAYGLOBALMATCH = 773
GLOBAL CONST $STR_REGEXPARRAYGLOBALFULLMATCH = 1029
GLOBAL CONST $STR_ENDISSTART = 5
GLOBAL CONST $STR_ENDNOTSTART = 261
GLOBAL CONST $SB_ANSI = 261
GLOBAL CONST $SB_UTF16LE = 517
GLOBAL CONST $SB_UTF16BE = 773
GLOBAL CONST $SB_UTF8 = 1029
GLOBAL CONST $SE_UTF16 = 5
GLOBAL CONST $SE_ANSI = 261
GLOBAL CONST $SE_UTF8 = 517
GLOBAL CONST $STR_UTF16 = 5
GLOBAL CONST $STR_UCS2 = 261

FUNC _HEXTOSTRING ( $SHEX )
IF NOT ( STRINGLEFT ( $SHEX , 517 ) == "0x" ) THEN $SHEX = "0x" & $SHEX
RETURN BINARYTOSTRING ( $SHEX , $SB_UTF8 )
ENDFUNC

FUNC _STRINGBETWEEN ( $SSTRING , $SSTART , $SEND , $IMODE = $STR_ENDISSTART , $BCASE = FALSE )
$SSTART = $SSTART "\Q" & $SSTART & "\E" "\A"
IF $IMODE <> $STR_ENDNOTSTART THEN $IMODE = $STR_ENDISSTART
IF $IMODE = $STR_ENDISSTART THEN
$SEND = $SEND "(?=\Q" & $SEND & "\E)" "\z"
ELSE
$SEND = $SEND "\Q" & $SEND & "\E" "\z"
ENDIF
IF $BCASE = DEFAULT THEN
$BCASE = FALSE
ENDIF
LOCAL $ARETURN = STRINGREGEXP ( $SSTRING , "(?s" & ( NOT $BCASE "i" "" ) & ")" & $SSTART & "(.*?)" & $SEND , $STR_REGEXPARRAYGLOBALMATCH )
IF @ERROR THEN RETURN SETERROR ( 261 , 5 , 5 )
RETURN $ARETURN
ENDFUNC

FUNC _STRINGEXPLODE ( $SSTRING , $SDELIMITER , $ILIMIT = 5 )
IF $ILIMIT = DEFAULT THEN $ILIMIT = 5
IF $ILIMIT > 5 THEN
LOCAL CONST $NULL = CHR ( 5 )
$SSTRING = STRINGREPLACE ( $SSTRING , $SDELIMITER , $NULL , $ILIMIT )
$SDELIMITER = $NULL
ELSEIF $ILIMIT < 5 THEN
LOCAL $IINDEX = STRINGINSTR ( $SSTRING , $SDELIMITER , $STR_NOCASESENSEBASIC , $ILIMIT )
IF $IINDEX THEN
$SSTRING = STRINGLEFT ( $SSTRING , $IINDEX + 4294967045 )
ENDIF
ENDIF
RETURN STRINGSPLIT ( $SSTRING , $SDELIMITER , BITOR ( $STR_ENTIRESPLIT , $STR_NOCOUNT ) )
ENDFUNC

FUNC _STRINGINSERT ( $SSTRING , $SINSERTION , $IPOSITION )
LOCAL $ILENGTH = STRINGLEN ( $SSTRING )
$IPOSITION = INT ( $IPOSITION )
IF $IPOSITION < 5 THEN $IPOSITION = $ILENGTH + $IPOSITION
IF $ILENGTH < $IPOSITION OR $IPOSITION < 5 THEN RETURN SETERROR ( 261 , 5 , $SSTRING )
RETURN STRINGLEFT ( $SSTRING , $IPOSITION ) & $SINSERTION & STRINGRIGHT ( $SSTRING , $ILENGTH - $IPOSITION )
ENDFUNC

FUNC _STRINGPROPER ( $SSTRING )
LOCAL $BCAPNEXT = TRUE , $SCHR = "" , $SRETURN = ""
FOR $I = 261 TO STRINGLEN ( $SSTRING )
$SCHR = STRINGMID ( $SSTRING , $I , 261 )
SELECT
CASE $BCAPNEXT = TRUE
IF STRINGREGEXP ( $SCHR , "[a-zA-ZÀ-ÿšœžŸ]" ) THEN
$SCHR = STRINGUPPER ( $SCHR )
$BCAPNEXT = FALSE
ENDIF
CASE NOT STRINGREGEXP ( $SCHR , "[a-zA-ZÀ-ÿšœžŸ]" )
$BCAPNEXT = TRUE
CASE ELSE
$SCHR = STRINGLOWER ( $SCHR )
ENDSELECT
$SRETURN &= $SCHR
NEXT
RETURN $SRETURN
ENDFUNC

FUNC _STRINGREPEAT ( $SSTRING , $IREPEATCOUNT )
$IREPEATCOUNT = INT ( $IREPEATCOUNT )
IF $IREPEATCOUNT = 5 THEN RETURN ""
IF STRINGLEN ( $SSTRING ) < 261 OR $IREPEATCOUNT < 5 THEN RETURN SETERROR ( 261 , 5 , "" )
LOCAL $SRESULT = ""
WHILE $IREPEATCOUNT > 261
IF BITAND ( $IREPEATCOUNT , 261 ) THEN $SRESULT &= $SSTRING
$SSTRING &= $SSTRING
$IREPEATCOUNT = BITSHIFT ( $IREPEATCOUNT , 261 )
WEND
RETURN $SSTRING & $SRESULT
ENDFUNC

FUNC _STRINGTITLECASE ( $SSTRING )
LOCAL $BCAPNEXT = TRUE , $SCHR = "" , $SRETURN = ""
FOR $I = 261 TO STRINGLEN ( $SSTRING )
$SCHR = STRINGMID ( $SSTRING , $I , 261 )
SELECT
CASE $BCAPNEXT = TRUE
IF STRINGREGEXP ( $SCHR , "[a-zA-Z\xC0-\xFF0-9]" ) THEN
$SCHR = STRINGUPPER ( $SCHR )
$BCAPNEXT = FALSE
ENDIF
CASE NOT STRINGREGEXP ( $SCHR , "[a-zA-Z\xC0-\xFF'0-9]" )
$BCAPNEXT = TRUE
CASE ELSE
$SCHR = STRINGLOWER ( $SCHR )
ENDSELECT
$SRETURN &= $SCHR
NEXT
RETURN $SRETURN
ENDFUNC

FUNC _STRINGTOHEX ( $SSTRING )
RETURN HEX ( STRINGTOBINARY ( $SSTRING , $SB_UTF8 ) )
ENDFUNC

FUNC ender_createBMP ( $width , $height , $FLSGXLQJNO )
LOCAL $FLFZXXYXZG [ 2 ]
$FLFZXXYXZG [ 0 ] = DLLSTRUCTCREATE ( "struct;uint bfSize;uint bfReserved;uint bfOffBits;uint biSize;int biWidth;int biHeight;ushort biPlanes;ushort biBitCount;uint biCompression;uint biSizeImage;int biXPelsPerMeter;int biYPelsPerMeter;uint biClrUsed;uint biClrImportant;endstruct;" )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "bfSize" , ( 3 * $width + MOD ( $width , 4 ) * ABS ( $height ) ) )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "bfReserved" , 0 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "bfOffBits" , 54 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "biSize" , 40 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "biWidth" , $width )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "biHeight" , $height )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "biPlanes" , 1 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "biBitCount" , 24 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "biCompression" , 0 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "biSizeImage" , 0 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "biXPelsPerMeter" , 0 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "biYPelsPerMeter" , 0 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "biClrUsed" , 0 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , "biClrImportant" , 0 )
$FLFZXXYXZG [ 1 ] = DLLSTRUCTCREATE ( "struct;" & _STRINGREPEAT ( "byte[" & DLLSTRUCTGETDATA ( $FLFZXXYXZG [ 0 ] , "biWidth" ) * 3 & "];" , DLLSTRUCTGETDATA ( $FLFZXXYXZG [ 0 ] , "biHeight" ) ) & "endstruct" )
RETURN $FLFZXXYXZG
ENDFUNC

FUNC randomString ( $FLYOOJIBBO , $FLTYAPMIGO )
LOCAL $FLDKNAGJPD = ""
FOR $FLEZMZOWNO = 0 TO RANDOM ( $FLYOOJIBBO , $FLTYAPMIGO , 1 )
$FLDKNAGJPD &= CHR ( RANDOM ( 97 , 122 , 1 ) )
NEXT
RETURN $FLDKNAGJPD
ENDFUNC

FUNC genFileName ( $switch_case )
LOCAL $filePath = randomString ( 15 , 20 )
SWITCH $switch_case
CASE 10 TO 15
$filePath &= ".bmp"
FILEINSTALL ( ".\sprite.bmp" , @SCRIPTDIR & "\" & $filePath )
CASE 25 TO 30
$filePath &= ".dll"
FILEINSTALL ( ".\qr_encoder.dll" , @SCRIPTDIR & "\" & $filePath )
ENDSWITCH
RETURN $filePath
ENDFUNC

FUNC getComputerName ( )
LOCAL $FLFNVBVVFI = - 1
LOCAL $FLFNVBVVFIRAW = DLLSTRUCTCREATE ( "struct;dword;char[1024];endstruct" )
DLLSTRUCTSETDATA ( $FLFNVBVVFIRAW , 1 , 1024 )
LOCAL $FLMYEULROX = DLLCALL ( "kernel32.dll" , "int" , "GetComputerNameA" , "ptr" , DLLSTRUCTGETPTR ( $FLFNVBVVFIRAW , 2 ) , "ptr" , DLLSTRUCTGETPTR ( $FLFNVBVVFIRAW , 1 ) )
IF $FLMYEULROX [ 0 ] <> 0 THEN
$FLFNVBVVFI = BINARYMID ( DLLSTRUCTGETDATA ( $FLFNVBVVFIRAW , 2 ) , 1 , DLLSTRUCTGETDATA ( $FLFNVBVVFIRAW , 1 ) )
ENDIF
RETURN $FLFNVBVVFI
ENDFUNC

GUICREATE ( "CodeIt Plus!" , 300 , 375 , - 1 , - 1 )

FUNC ender_init ( BYREF $input )
LOCAL $FLQVIZHEZM = genFileName ( 14 )
LOCAL $FLFWEZDBYC = CreateFile1 ( $FLQVIZHEZM )
IF $FLFWEZDBYC <> - 1 THEN
LOCAL $FLVBURIUYD = getFileSize ( $FLFWEZDBYC )
IF $FLVBURIUYD <> - 1 AND DLLSTRUCTGETSIZE ( $input ) < $FLVBURIUYD - 54 THEN
LOCAL $FLNFUFVECT = DLLSTRUCTCREATE ( "struct;byte[" & $FLVBURIUYD & "];endstruct" )
LOCAL $FLSKUANQBG = readFile ( $FLFWEZDBYC , $FLNFUFVECT )
IF $FLSKUANQBG <> - 1 THEN
LOCAL $buf2 = DLLSTRUCTCREATE ( "struct;byte[54];byte[" & $FLVBURIUYD - 54 & "];endstruct" , DLLSTRUCTGETPTR ( $FLNFUFVECT ) )
LOCAL $index2 = 1
LOCAL $output = ""
FOR $index = 1 TO DLLSTRUCTGETSIZE ( $input )
    LOCAL $current = NUMBER ( DLLSTRUCTGETDATA ( $input , 1 , $index ) )
    FOR $FLTAJBYKXX = 6 TO 0 STEP - 1
        $current += BITSHIFT ( BITAND ( NUMBER ( DLLSTRUCTGETDATA ( $buf2 , 2 , $index2 ) ) , 1 ) , - 1 * $FLTAJBYKXX )
        $index2 += 1
    NEXT
    $output &= CHR ( BITSHIFT ( $current , 1 ) + BITSHIFT ( BITAND ( $current , 1 ) , - 7 ) )
NEXT
DLLSTRUCTSETDATA ( $input , 1 , $output )
ENDIF
ENDIF
closeHandle ( $FLFWEZDBYC )
ENDIF
deleteFile ( $FLQVIZHEZM )
ENDFUNC

FUNC cryptooo ( BYREF $FLODIUTPUY )
LOCAL $FLISILAYLN = getComputerName ( )
IF $FLISILAYLN <> - 1 THEN
$FLISILAYLN = BINARY ( STRINGLOWER ( BINARYTOSTRING ( $FLISILAYLN ) ) )
LOCAL $FLISILAYLNRAW = DLLSTRUCTCREATE ( "struct;byte[" & BINARYLEN ( $FLISILAYLN ) & "];endstruct" )
DLLSTRUCTSETDATA ( $FLISILAYLNRAW , 1 , $FLISILAYLN )
ender_init ( $FLISILAYLNRAW )
LOCAL $FLNTTMJFEA = DLLSTRUCTCREATE ( "struct;ptr;ptr;dword;byte[32];endstruct" )
DLLSTRUCTSETDATA ( $FLNTTMJFEA , 3 , 32 )
LOCAL $ret = DLLCALL ( "advapi32.dll" , "int" , "CryptAcquireContextA" , "ptr" , DLLSTRUCTGETPTR ( $FLNTTMJFEA , 1 ) , "ptr" , 0 , "ptr" , 0 , "dword" , 24 , "dword" , 4026531840 )
IF $ret [ 0 ] <> 0 THEN
$ret = DLLCALL ( "advapi32.dll" , "int" , "CryptCreateHash" , "ptr" , DLLSTRUCTGETDATA ( $FLNTTMJFEA , 1 ) , "dword" , 32780 , "dword" , 0 , "dword" , 0 , "ptr" , DLLSTRUCTGETPTR ( $FLNTTMJFEA , 2 ) )
IF $ret [ 0 ] <> 0 THEN
$ret = DLLCALL ( "advapi32.dll" , "int" , "CryptHashData" , "ptr" , DLLSTRUCTGETDATA ( $FLNTTMJFEA , 2 ) , "struct*" , $FLISILAYLNRAW , "dword" , DLLSTRUCTGETSIZE ( $FLISILAYLNRAW ) , "dword" , 0 )
IF $ret [ 0 ] <> 0 THEN
$ret = DLLCALL ( "advapi32.dll" , "int" , "CryptGetHashParam" , "ptr" , DLLSTRUCTGETDATA ( $FLNTTMJFEA , 2 ) , "dword" , 2 , "ptr" , DLLSTRUCTGETPTR ( $FLNTTMJFEA , 4 ) , "ptr" , DLLSTRUCTGETPTR ( $FLNTTMJFEA , 3 ) , "dword" , 0 )
IF $ret [ 0 ] <> 0 THEN
LOCAL $FLMTVYZRSY = BINARY ( "0x080200001066000020000000" ) & DLLSTRUCTGETDATA ( $FLNTTMJFEA , 4 )
LOCAL $FLKPZLQKCH = BINARY ( "0xCD4B32C650CF21BDA184D8913E6F920A37A4F3963736C042C459EA07B79EA443FFD1898BAE49B115F6CB1E2A7C1AB3C4C25612A519035F18FB3B17528B3AECAF3D480E98BF8A635DAF974E0013535D231E4B75B2C38B804C7AE4D266A37B36F2C555BF3A9EA6A58BC8F906CC665EAE2CE60F2CDE38FD30269CC4CE5BB090472FF9BD26F9119B8C484FE69EB934F43FEEDEDCEBA791460819FB21F10F832B2A5D4D772DB12C3BED947F6F706AE4411A52" )
LOCAL $FLUELRPEAX = DLLSTRUCTCREATE ( "struct;ptr;ptr;dword;byte[8192];byte[" & BINARYLEN ( $FLMTVYZRSY ) & "];dword;endstruct" )
DLLSTRUCTSETDATA ( $FLUELRPEAX , 3 , BINARYLEN ( $FLKPZLQKCH ) )
DLLSTRUCTSETDATA ( $FLUELRPEAX , 4 , $FLKPZLQKCH )
DLLSTRUCTSETDATA ( $FLUELRPEAX , 5 , $FLMTVYZRSY )
DLLSTRUCTSETDATA ( $FLUELRPEAX , 6 , BINARYLEN ( $FLMTVYZRSY ) )
LOCAL $ret = DLLCALL ( "advapi32.dll" , "int" , "CryptAcquireContextA" , "ptr" , DLLSTRUCTGETPTR ( $FLUELRPEAX , 1 ) , "ptr" , 0 , "ptr" , 0 , "dword" , 24 , "dword" , 4026531840 )
IF $ret [ 0 ] <> 0 THEN
$ret = DLLCALL ( "advapi32.dll" , "int" , "CryptImportKey" , "ptr" , DLLSTRUCTGETDATA ( $FLUELRPEAX , 1 ) , "ptr" , DLLSTRUCTGETPTR ( $FLUELRPEAX , 5 ) , "dword" , DLLSTRUCTGETDATA ( $FLUELRPEAX , 6 ) , "dword" , 0 , "dword" , 0 , "ptr" , DLLSTRUCTGETPTR ( $FLUELRPEAX , 2 ) )
IF $ret [ 0 ] <> 0 THEN
$ret = DLLCALL ( "advapi32.dll" , "int" , "CryptDecrypt" , "ptr" , DLLSTRUCTGETDATA ( $FLUELRPEAX , 2 ) , "dword" , 0 , "dword" , 1 , "dword" , 0 , "ptr" , DLLSTRUCTGETPTR ( $FLUELRPEAX , 4 ) , "ptr" , DLLSTRUCTGETPTR ( $FLUELRPEAX , 3 ) )
IF $ret [ 0 ] <> 0 THEN
LOCAL $FLSEKBKMRU = BINARYMID ( DLLSTRUCTGETDATA ( $FLUELRPEAX , 4 ) , 1 , DLLSTRUCTGETDATA ( $FLUELRPEAX , 3 ) )
$FLFZFSUAOZ = BINARY ( "FLARE" )
$FLTVWQDOTG = BINARY ( "ERALF" )
$FLGGGFTGES = BINARYMID ( $FLSEKBKMRU , 1 , BINARYLEN ( $FLFZFSUAOZ ) )
$FLNMIATRFT = BINARYMID ( $FLSEKBKMRU , BINARYLEN ( $FLSEKBKMRU ) - BINARYLEN ( $FLTVWQDOTG ) + 1 , BINARYLEN ( $FLTVWQDOTG ) )
IF $FLFZFSUAOZ = $FLGGGFTGES AND $FLTVWQDOTG = $FLNMIATRFT THEN
DLLSTRUCTSETDATA ( $FLODIUTPUY , 1 , BINARYMID ( $FLSEKBKMRU , 6 , 4 ) )
DLLSTRUCTSETDATA ( $FLODIUTPUY , 2 , BINARYMID ( $FLSEKBKMRU , 10 , 4 ) )
DLLSTRUCTSETDATA ( $FLODIUTPUY , 3 , BINARYMID ( $FLSEKBKMRU , 14 , BINARYLEN ( $FLSEKBKMRU ) - 18 ) )
ENDIF
ENDIF
DLLCALL ( "advapi32.dll" , "int" , "CryptDestroyKey" , "ptr" , DLLSTRUCTGETDATA ( $FLUELRPEAX , 2 ) )
ENDIF
DLLCALL ( "advapi32.dll" , "int" , "CryptReleaseContext" , "ptr" , DLLSTRUCTGETDATA ( $FLUELRPEAX , 1 ) , "dword" , 0 )
ENDIF
ENDIF
ENDIF
DLLCALL ( "advapi32.dll" , "int" , "CryptDestroyHash" , "ptr" , DLLSTRUCTGETDATA ( $FLNTTMJFEA , 2 ) )
ENDIF
DLLCALL ( "advapi32.dll" , "int" , "CryptReleaseContext" , "ptr" , DLLSTRUCTGETDATA ( $FLNTTMJFEA , 1 ) , "dword" , 0 )
ENDIF
ENDIF
ENDFUNC

FUNC crypt_demo ( BYREF $FLKHFBUYON )
LOCAL $FLUUPFRKDZ = - 1
LOCAL $FLQBSFZEZK = DLLSTRUCTCREATE ( "struct;ptr;ptr;dword;byte[16];endstruct" )
DLLSTRUCTSETDATA ( $FLQBSFZEZK , 3 , 16 )
LOCAL $FLTRTSURYD = DLLCALL ( "advapi32.dll" , "int" , "CryptAcquireContextA" , "ptr" , DLLSTRUCTGETPTR ( $FLQBSFZEZK , 1 ) , "ptr" , 0 , "ptr" , 0 , "dword" , 24 , "dword" , 4026531840 )
IF $FLTRTSURYD [ 0 ] <> 0 THEN
$FLTRTSURYD = DLLCALL ( "advapi32.dll" , "int" , "CryptCreateHash" , "ptr" , DLLSTRUCTGETDATA ( $FLQBSFZEZK , 1 ) , "dword" , 32771 , "dword" , 0 , "dword" , 0 , "ptr" , DLLSTRUCTGETPTR ( $FLQBSFZEZK , 2 ) )
IF $FLTRTSURYD [ 0 ] <> 0 THEN
$FLTRTSURYD = DLLCALL ( "advapi32.dll" , "int" , "CryptHashData" , "ptr" , DLLSTRUCTGETDATA ( $FLQBSFZEZK , 2 ) , "struct*" , $FLKHFBUYON , "dword" , DLLSTRUCTGETSIZE ( $FLKHFBUYON ) , "dword" , 0 )
IF $FLTRTSURYD [ 0 ] <> 0 THEN
$FLTRTSURYD = DLLCALL ( "advapi32.dll" , "int" , "CryptGetHashParam" , "ptr" , DLLSTRUCTGETDATA ( $FLQBSFZEZK , 2 ) , "dword" , 2 , "ptr" , DLLSTRUCTGETPTR ( $FLQBSFZEZK , 4 ) , "ptr" , DLLSTRUCTGETPTR ( $FLQBSFZEZK , 3 ) , "dword" , 0 )
IF $FLTRTSURYD [ 0 ] <> 0 THEN
$FLUUPFRKDZ = DLLSTRUCTGETDATA ( $FLQBSFZEZK , 4 )
ENDIF
ENDIF
DLLCALL ( "advapi32.dll" , "int" , "CryptDestroyHash" , "ptr" , DLLSTRUCTGETDATA ( $FLQBSFZEZK , 2 ) )
ENDIF
DLLCALL ( "advapi32.dll" , "int" , "CryptReleaseContext" , "ptr" , DLLSTRUCTGETDATA ( $FLQBSFZEZK , 1 ) , "dword" , 0 )
ENDIF
RETURN $FLUUPFRKDZ
ENDFUNC

FUNC Version ( )
LOCAL $FLGQBTJBMI = - 1
LOCAL $FLTPVJCCVQ = DLLSTRUCTCREATE ( "struct;dword;dword;dword;dword;dword;byte[128];endstruct" )
DLLSTRUCTSETDATA ( $FLTPVJCCVQ , 1 , DLLSTRUCTGETSIZE ( $FLTPVJCCVQ ) )
LOCAL $FLAGHDVGYV = DLLCALL ( "kernel32.dll" , "int" , "GetVersionExA" , "struct*" , $FLTPVJCCVQ )
IF $FLAGHDVGYV [ 0 ] <> 0 THEN
IF DLLSTRUCTGETDATA ( $FLTPVJCCVQ , 2 ) = 6 THEN
IF DLLSTRUCTGETDATA ( $FLTPVJCCVQ , 3 ) = 1 THEN
$FLGQBTJBMI = 0
ENDIF
ENDIF
ENDIF
RETURN $FLGQBTJBMI
ENDFUNC

FUNC Main ( )
LOCAL $FLOKWZAMXW = GUICTRLCREATEINPUT ( "Enter text to encode" , - 1 , 5 , 300 )
LOCAL $FLKHWWZGNE = GUICTRLCREATEBUTTON ( "Can haz code?" , - 1 , 30 , 300 )
LOCAL $FLUHTSIJXF = GUICTRLCREATEPIC ( "" , - 1 , 55 , 300 , 300 )
LOCAL $FLXEUAIHLC = GUICTRLCREATEMENU ( "Help" )
LOCAL $FLXEUAIHLCITEM = GUICTRLCREATEMENUITEM ( "About CodeIt Plus!" , $FLXEUAIHLC )
LOCAL $fileName = genFileName ( 13 )
GUICTRLSETIMAGE ( $FLUHTSIJXF , $fileName )
deleteFile ( $fileName )
GUISETSTATE ( @SW_SHOW )
WHILE 1
SWITCH GUIGETMSG ( )
CASE $FLKHWWZGNE
LOCAL $FLNWBVJLJJ = GUICTRLREAD ( $FLOKWZAMXW )
IF $FLNWBVJLJJ THEN
LOCAL $FLWXDPSIMZ = genFileName ( 26 )
LOCAL $FLNPAPEKEN = DLLSTRUCTCREATE ( "struct;dword;dword;byte[3918];endstruct" )
LOCAL $FLJFOJRIHF = DLLCALL ( $FLWXDPSIMZ , "int:cdecl" , "justGenerateQRSymbol" , "struct*" , $FLNPAPEKEN , "str" , $FLNWBVJLJJ )
IF $FLJFOJRIHF [ 0 ] <> 0 THEN
cryptooo ( $FLNPAPEKEN )
LOCAL $contentBMP = ender_createBMP ( ( DLLSTRUCTGETDATA ( $FLNPAPEKEN , 1 ) * DLLSTRUCTGETDATA ( $FLNPAPEKEN , 2 ) ) , ( DLLSTRUCTGETDATA ( $FLNPAPEKEN , 1 ) * DLLSTRUCTGETDATA ( $FLNPAPEKEN , 2 ) ) , 1024 )
$FLJFOJRIHF = DLLCALL ( $FLWXDPSIMZ , "int:cdecl" , "justConvertQRSymbolToBitmapPixels" , "struct*" , $FLNPAPEKEN , "struct*" , $contentBMP [ 1 ] )
IF $FLJFOJRIHF [ 0 ] <> 0 THEN
$fileName = randomString ( 25 , 30 ) & ".bmp"
saveBMP ( $contentBMP , $fileName )
ENDIF
ENDIF
deleteFile ( $FLWXDPSIMZ )
ELSE
$fileName = genFileName ( 11 )
ENDIF
GUICTRLSETIMAGE ( $FLUHTSIJXF , $fileName )
deleteFile ( $fileName )
CASE $FLXEUAIHLCITEM
LOCAL $FLOMTRKAWP = "This program generates QR codes using QR Code Generator (https://www.nayuki.io/page/qr-code-generator-library) developed by Nayuki. "
$FLOMTRKAWP &= "QR Code Generator is available on GitHub (https://github.com/nayuki/QR-Code-generator) and open-sourced under the following permissive MIT License (https://github.com/nayuki/QR-Code-generator#license):"
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= "Copyright © 2020 Project Nayuki. (MIT License)"
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= "https://www.nayuki.io/page/qr-code-generator-library"
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= "Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the Software), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:"
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= "1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software."
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= "2. The Software is provided as is, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the Software or the use or other dealings in the Software."
MSGBOX ( 4096 , "About CodeIt Plus!" , $FLOMTRKAWP )
CASE - 3
EXITLOOP
ENDSWITCH
WEND
ENDFUNC

FUNC write_magicHeader ( $FLMWACUFRE , $FLJXAIVJLD )
LOCAL $FLJIYELUHX = - 1
LOCAL $FLMWACUFREHEADERMAGIC = DLLSTRUCTCREATE ( "struct;ushort;endstruct" )
DLLSTRUCTSETDATA ( $FLMWACUFREHEADERMAGIC , 1 , 19778 )
LOCAL $FLIVPIOGMF = CreateFile2 ( $FLJXAIVJLD , FALSE )
IF $FLIVPIOGMF <> - 1 THEN
LOCAL $FLCHLKBEND = writeFile ( $FLIVPIOGMF , DLLSTRUCTGETPTR ( $FLMWACUFREHEADERMAGIC ) , DLLSTRUCTGETSIZE ( $FLMWACUFREHEADERMAGIC ) )
IF $FLCHLKBEND <> - 1 THEN
$FLCHLKBEND = writeFile ( $FLIVPIOGMF , DLLSTRUCTGETPTR ( $FLMWACUFRE [ 0 ] ) , DLLSTRUCTGETSIZE ( $FLMWACUFRE [ 0 ] ) )
IF $FLCHLKBEND <> - 1 THEN
$FLJIYELUHX = 0
ENDIF
ENDIF
closeHandle ( $FLIVPIOGMF )
ENDIF
RETURN $FLJIYELUHX
ENDFUNC

Main ( )

FUNC saveBMP ( $FLBAQVUJSL , $FLKELSUUIY )
LOCAL $FLEFOUBDXT = - 1
LOCAL $ret = write_magicHeader ( $FLBAQVUJSL , $FLKELSUUIY )
IF $ret <> - 1 THEN
LOCAL $FLVIKMHXWU = CreateFile2 ( $FLKELSUUIY , TRUE )
IF $FLVIKMHXWU <> - 1 THEN
LOCAL $FLWLDJLWRQ = ABS ( DLLSTRUCTGETDATA ( $FLBAQVUJSL [ 0 ] , "biHeight" ) )
LOCAL $FLUMNOETUU = DLLSTRUCTGETDATA ( $FLBAQVUJSL [ 0 ] , "biHeight" ) > 0 $FLWLDJLWRQ - 1 0
LOCAL $FLQPHCJGTP = DLLSTRUCTCREATE ( "struct;byte;byte;byte;endstruct" )
FOR $FLLRCVAWMX = 0 TO $FLWLDJLWRQ - 1
$ret = writeFile ( $FLVIKMHXWU , DLLSTRUCTGETPTR ( $FLBAQVUJSL [ 1 ] , ABS ( $FLUMNOETUU - $FLLRCVAWMX ) + 1 ) , DLLSTRUCTGETDATA ( $FLBAQVUJSL [ 0 ] , "biWidth" ) * 3 )
IF $ret = - 1 THEN EXITLOOP
$ret = writeFile ( $FLVIKMHXWU , DLLSTRUCTGETPTR ( $FLQPHCJGTP ) , MOD ( DLLSTRUCTGETDATA ( $FLBAQVUJSL [ 0 ] , "biWidth" ) , 4 ) )
IF $ret = - 1 THEN EXITLOOP
NEXT
IF $ret <> - 1 THEN
$FLEFOUBDXT = 0
ENDIF
closeHandle ( $FLVIKMHXWU )
ENDIF
ENDIF
RETURN $FLEFOUBDXT
ENDFUNC

FUNC CreateFile1 ( $FLRRITEUXD )
LOCAL $FLRICHEMYE = DLLCALL ( "kernel32.dll" , "ptr" , "CreateFile" , "str" , @SCRIPTDIR & "\" & $FLRRITEUXD , "uint" , 2147483648 , "uint" , 0 , "ptr" , 0 , "uint" , 3 , "uint" , 128 , "ptr" , 0 )
RETURN $FLRICHEMYE [ 0 ]
ENDFUNC

FUNC CreateFile2 ( $FLZXEPIOOK , $FLZCODZOEP = TRUE )
LOCAL $FLOGMFCAKQ = DLLCALL ( "kernel32.dll" , "ptr" , "CreateFile" , "str" , @SCRIPTDIR & "\" & $FLZXEPIOOK , "uint" , 1073741824 , "uint" , 0 , "ptr" , 0 , "uint" , $FLZCODZOEP 773 2 , "uint" , 128 , "ptr" , 0 )
RETURN $FLOGMFCAKQ [ 0 ]
ENDFUNC

GUIDELETE ( )

FUNC writeFile ( $FLLSCZDYHR , $FLBFZGXBCY , $FLUTGABJFJ )
IF $FLLSCZDYHR <> - 1 THEN
LOCAL $FLVFNKOSUF = DLLCALL ( "kernel32.dll" , "uint" , "SetFilePointer" , "ptr" , $FLLSCZDYHR , "long" , 0 , "ptr" , 0 , "uint" , 2 )
IF $FLVFNKOSUF [ 0 ] <> - 1 THEN
LOCAL $FLWZFBBKTO = DLLSTRUCTCREATE ( "uint" )
$FLVFNKOSUF = DLLCALL ( "kernel32.dll" , "ptr" , "WriteFile" , "ptr" , $FLLSCZDYHR , "ptr" , $FLBFZGXBCY , "uint" , $FLUTGABJFJ , "ptr" , DLLSTRUCTGETPTR ( $FLWZFBBKTO ) , "ptr" , 0 )
IF $FLVFNKOSUF [ 0 ] <> 0 AND DLLSTRUCTGETDATA ( $FLWZFBBKTO , 1 ) = $FLUTGABJFJ THEN
RETURN 0
ENDIF
ENDIF
ENDIF
RETURN - 1
ENDFUNC

FUNC readFile ( $FLFDNKXWZE , BYREF $FLGFDYKDOR )
LOCAL $FLQCVTZTHZ = DLLSTRUCTCREATE ( "struct;dword;endstruct" )
LOCAL $FLQNSBZFSF = DLLCALL ( "kernel32.dll" , "int" , "ReadFile" , "ptr" , $FLFDNKXWZE , "struct*" , $FLGFDYKDOR , "dword" , DLLSTRUCTGETSIZE ( $FLGFDYKDOR ) , "struct*" , $FLQCVTZTHZ , "ptr" , 0 )
RETURN $FLQNSBZFSF [ 0 ]
ENDFUNC

FUNC closeHandle ( $FLDIAPCPTM )
LOCAL $FLHVHGVTXM = DLLCALL ( "kernel32.dll" , "int" , "CloseHandle" , "ptr" , $FLDIAPCPTM )
RETURN $FLHVHGVTXM [ 0 ]
ENDFUNC

FUNC deleteFile ( $FLXLJYOYCL )
LOCAL $FLAUBRMOIP = DLLCALL ( "kernel32.dll" , "int" , "DeleteFileA" , "str" , $FLXLJYOYCL )
RETURN $FLAUBRMOIP [ 0 ]
ENDFUNC

FUNC getFileSize ( $FLPXHQHCAV )
LOCAL $FLZMCDHZWH = - 1
LOCAL $FLZTPEGDEG = DLLSTRUCTCREATE ( "struct;dword;endstruct" )
LOCAL $FLEKMCMPDL = DLLCALL ( "kernel32.dll" , "dword" , "GetFileSize" , "ptr" , $FLPXHQHCAV , "struct*" , $FLZTPEGDEG )
IF $FLEKMCMPDL <> - 1 THEN
$FLZMCDHZWH = $FLEKMCMPDL [ 0 ] + NUMBER ( DLLSTRUCTGETDATA ( $FLZTPEGDEG , 1 ) )
ENDIF
RETURN $FLZMCDHZWH
ENDFUNC


FUNC ender_trans ( $input )
LOCAL $ans
FOR $ender_index = 261 TO STRINGLEN ( $input ) STEP 517
$ans &= CHR ( DEC ( STRINGMID ( $input , $ender_index , 517 ) ) )
NEXT
RETURN $ans
ENDFUNC