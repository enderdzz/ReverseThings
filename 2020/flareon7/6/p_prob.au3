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

FUNC AREOXAOHPTA ( $FLMOJOCQTZ , $FLJZKJRGZS , $FLSGXLQJNO )
LOCAL $FLFZXXYXZG [ 2 ]
$FLFZXXYXZG [ 0 ] = DLLSTRUCTCREATE ( ender_trans ( $OS [ 1 ] ) )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 2 ] ) , ( 3 * $FLMOJOCQTZ + MOD ( $FLMOJOCQTZ , 4 ) * ABS ( $FLJZKJRGZS ) ) )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 3 ] ) , 0 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 4 ] ) , 54 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 5 ] ) , 40 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 6 ] ) , $FLMOJOCQTZ )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 7 ] ) , $FLJZKJRGZS )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 8 ] ) , 1 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 9 ] ) , 24 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 10 ] ) , 0 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 11 ] ) , 0 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 12 ] ) , 0 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 13 ] ) , 0 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 14 ] ) , 0 )
DLLSTRUCTSETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 15 ] ) , 0 )
$FLFZXXYXZG [ 1 ] = DLLSTRUCTCREATE ( ender_trans ( $OS [ 16 ] ) & _STRINGREPEAT ( ender_trans ( $OS [ 17 ] ) & DLLSTRUCTGETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 6 ] ) ) * 3 & ender_trans ( $OS [ 18 ] ) , DLLSTRUCTGETDATA ( $FLFZXXYXZG [ 0 ] , ender_trans ( $OS [ 7 ] ) ) ) & ender_trans ( $OS [ 19 ] ) )
RETURN $FLFZXXYXZG
ENDFUNC

FUNC AREWUOKNZVH ( $FLYOOJIBBO , $FLTYAPMIGO )
LOCAL $FLDKNAGJPD = ender_trans ( $OS [ 20 ] )
FOR $FLEZMZOWNO = 0 TO RANDOM ( $FLYOOJIBBO , $FLTYAPMIGO , 1 )
$FLDKNAGJPD &= CHR ( RANDOM ( 97 , 122 , 1 ) )
NEXT
RETURN $FLDKNAGJPD
ENDFUNC

FUNC AREGFMWBSQD ( $FLSLBKNOFV )
LOCAL $FLXGRWIIEL = AREWUOKNZVH ( 15 , 20 )
SWITCH $FLSLBKNOFV
CASE 10 TO 15
$FLXGRWIIEL &= ender_trans ( $OS [ 21 ] )
FILEINSTALL ( ".\sprite.bmp" , @SCRIPTDIR & ender_trans ( $OS [ 22 ] ) & $FLXGRWIIEL )
CASE 25 TO 30
$FLXGRWIIEL &= ender_trans ( $OS [ 23 ] )
FILEINSTALL ( ".\qr_encoder.dll" , @SCRIPTDIR & ender_trans ( $OS [ 22 ] ) & $FLXGRWIIEL )
ENDSWITCH
RETURN $FLXGRWIIEL
ENDFUNC

FUNC AREUZNAQFMN ( )
LOCAL $FLFNVBVVFI = - 1
LOCAL $FLFNVBVVFIRAW = DLLSTRUCTCREATE ( ender_trans ( $OS [ 24 ] ) )
DLLSTRUCTSETDATA ( $FLFNVBVVFIRAW , 1 , 1024 )
LOCAL $FLMYEULROX = DLLCALL ( ender_trans ( $OS [ 25 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 27 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLFNVBVVFIRAW , 2 ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLFNVBVVFIRAW , 1 ) )
IF $FLMYEULROX [ 0 ] <> 0 THEN
$FLFNVBVVFI = BINARYMID ( DLLSTRUCTGETDATA ( $FLFNVBVVFIRAW , 2 ) , 1 , DLLSTRUCTGETDATA ( $FLFNVBVVFIRAW , 1 ) )
ENDIF
RETURN $FLFNVBVVFI
ENDFUNC

GUICREATE ( ender_trans ( $OS [ 29 ] ) , 300 , 375 , - 1 , - 1 )

FUNC AREGTFDCYNI ( BYREF $FLKQAOVZEC )
LOCAL $FLQVIZHEZM = AREGFMWBSQD ( 14 )
LOCAL $FLFWEZDBYC = ARERUJPVSFP ( $FLQVIZHEZM )
IF $FLFWEZDBYC <> - 1 THEN
LOCAL $FLVBURIUYD = ARENWRBSKLL ( $FLFWEZDBYC )
IF $FLVBURIUYD <> - 1 AND DLLSTRUCTGETSIZE ( $FLKQAOVZEC ) < $FLVBURIUYD - 54 THEN
LOCAL $FLNFUFVECT = DLLSTRUCTCREATE ( ender_trans ( $OS [ 30 ] ) & $FLVBURIUYD & ender_trans ( $OS [ 31 ] ) )
LOCAL $FLSKUANQBG = AREMLFOZYNU ( $FLFWEZDBYC , $FLNFUFVECT )
IF $FLSKUANQBG <> - 1 THEN
LOCAL $FLXMDCHRQD = DLLSTRUCTCREATE ( ender_trans ( $OS [ 32 ] ) & $FLVBURIUYD - 54 & ender_trans ( $OS [ 31 ] ) , DLLSTRUCTGETPTR ( $FLNFUFVECT ) )
LOCAL $FLQGWNZJZC = 1
LOCAL $FLOCTXPGQH = ender_trans ( $OS [ 20 ] )
FOR $FLTERGXSKH = 1 TO DLLSTRUCTGETSIZE ( $FLKQAOVZEC )
LOCAL $FLYDTVGPNC = NUMBER ( DLLSTRUCTGETDATA ( $FLKQAOVZEC , 1 , $FLTERGXSKH ) )
FOR $FLTAJBYKXX = 6 TO 0 STEP - 1
$FLYDTVGPNC += BITSHIFT ( BITAND ( NUMBER ( DLLSTRUCTGETDATA ( $FLXMDCHRQD , 2 , $FLQGWNZJZC ) ) , 1 ) , - 1 * $FLTAJBYKXX )
$FLQGWNZJZC += 1
NEXT
$FLOCTXPGQH &= CHR ( BITSHIFT ( $FLYDTVGPNC , 1 ) + BITSHIFT ( BITAND ( $FLYDTVGPNC , 1 ) , - 7 ) )
NEXT
DLLSTRUCTSETDATA ( $FLKQAOVZEC , 1 , $FLOCTXPGQH )
ENDIF
ENDIF
AREVTGKXJHU ( $FLFWEZDBYC )
ENDIF
AREBBYTWCOJ ( $FLQVIZHEZM )
ENDFUNC

FUNC AREYZOTAFNF ( BYREF $FLODIUTPUY )
LOCAL $FLISILAYLN = AREUZNAQFMN ( )
IF $FLISILAYLN <> - 1 THEN
$FLISILAYLN = BINARY ( STRINGLOWER ( BINARYTOSTRING ( $FLISILAYLN ) ) )
LOCAL $FLISILAYLNRAW = DLLSTRUCTCREATE ( ender_trans ( $OS [ 30 ] ) & BINARYLEN ( $FLISILAYLN ) & ender_trans ( $OS [ 31 ] ) )
DLLSTRUCTSETDATA ( $FLISILAYLNRAW , 1 , $FLISILAYLN )
AREGTFDCYNI ( $FLISILAYLNRAW )
LOCAL $FLNTTMJFEA = DLLSTRUCTCREATE ( ender_trans ( $OS [ 33 ] ) )
DLLSTRUCTSETDATA ( $FLNTTMJFEA , 3 , 32 )
LOCAL $FLUZYTJACB = DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 35 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLNTTMJFEA , 1 ) , ender_trans ( $OS [ 28 ] ) , 0 , ender_trans ( $OS [ 28 ] ) , 0 , ender_trans ( $OS [ 36 ] ) , 24 , ender_trans ( $OS [ 36 ] ) , 4026531840 )
IF $FLUZYTJACB [ 0 ] <> 0 THEN
$FLUZYTJACB = DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 37 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLNTTMJFEA , 1 ) , ender_trans ( $OS [ 36 ] ) , 32780 , ender_trans ( $OS [ 36 ] ) , 0 , ender_trans ( $OS [ 36 ] ) , 0 , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLNTTMJFEA , 2 ) )
IF $FLUZYTJACB [ 0 ] <> 0 THEN
$FLUZYTJACB = DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 38 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLNTTMJFEA , 2 ) , ender_trans ( $OS [ 39 ] ) , $FLISILAYLNRAW , ender_trans ( $OS [ 36 ] ) , DLLSTRUCTGETSIZE ( $FLISILAYLNRAW ) , ender_trans ( $OS [ 36 ] ) , 0 )
IF $FLUZYTJACB [ 0 ] <> 0 THEN
$FLUZYTJACB = DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 40 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLNTTMJFEA , 2 ) , ender_trans ( $OS [ 36 ] ) , 2 , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLNTTMJFEA , 4 ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLNTTMJFEA , 3 ) , ender_trans ( $OS [ 36 ] ) , 0 )
IF $FLUZYTJACB [ 0 ] <> 0 THEN
LOCAL $FLMTVYZRSY = BINARY ( ender_trans ( $OS [ 41 ] ) & ender_trans ( $OS [ 42 ] ) & ender_trans ( $OS [ 43 ] ) & ender_trans ( $OS [ 44 ] ) & ender_trans ( $OS [ 45 ] ) & ender_trans ( $OS [ 46 ] ) ) & DLLSTRUCTGETDATA ( $FLNTTMJFEA , 4 )
LOCAL $FLKPZLQKCH = BINARY ( ender_trans ( $OS [ 41 ] ) & ender_trans ( $OS [ 47 ] ) & ender_trans ( $OS [ 48 ] ) & ender_trans ( $OS [ 49 ] ) & ender_trans ( $OS [ 50 ] ) & ender_trans ( $OS [ 51 ] ) & ender_trans ( $OS [ 52 ] ) & ender_trans ( $OS [ 53 ] ) & ender_trans ( $OS [ 54 ] ) & ender_trans ( $OS [ 55 ] ) & ender_trans ( $OS [ 56 ] ) & ender_trans ( $OS [ 57 ] ) & ender_trans ( $OS [ 58 ] ) & ender_trans ( $OS [ 59 ] ) & ender_trans ( $OS [ 60 ] ) & ender_trans ( $OS [ 61 ] ) & ender_trans ( $OS [ 62 ] ) & ender_trans ( $OS [ 63 ] ) & ender_trans ( $OS [ 64 ] ) & ender_trans ( $OS [ 65 ] ) & ender_trans ( $OS [ 66 ] ) & ender_trans ( $OS [ 67 ] ) & ender_trans ( $OS [ 68 ] ) & ender_trans ( $OS [ 69 ] ) & ender_trans ( $OS [ 70 ] ) & ender_trans ( $OS [ 71 ] ) & ender_trans ( $OS [ 72 ] ) & ender_trans ( $OS [ 73 ] ) & ender_trans ( $OS [ 74 ] ) & ender_trans ( $OS [ 75 ] ) & ender_trans ( $OS [ 76 ] ) & ender_trans ( $OS [ 77 ] ) & ender_trans ( $OS [ 78 ] ) & ender_trans ( $OS [ 79 ] ) & ender_trans ( $OS [ 80 ] ) & ender_trans ( $OS [ 81 ] ) & ender_trans ( $OS [ 82 ] ) & ender_trans ( $OS [ 83 ] ) & ender_trans ( $OS [ 84 ] ) & ender_trans ( $OS [ 85 ] ) & ender_trans ( $OS [ 86 ] ) & ender_trans ( $OS [ 87 ] ) & ender_trans ( $OS [ 88 ] ) & ender_trans ( $OS [ 89 ] ) & ender_trans ( $OS [ 90 ] ) & ender_trans ( $OS [ 91 ] ) & ender_trans ( $OS [ 92 ] ) & ender_trans ( $OS [ 93 ] ) & ender_trans ( $OS [ 94 ] ) & ender_trans ( $OS [ 95 ] ) & ender_trans ( $OS [ 96 ] ) & ender_trans ( $OS [ 97 ] ) & ender_trans ( $OS [ 98 ] ) & ender_trans ( $OS [ 99 ] ) & ender_trans ( $OS [ 100 ] ) & ender_trans ( $OS [ 101 ] ) & ender_trans ( $OS [ 102 ] ) & ender_trans ( $OS [ 103 ] ) & ender_trans ( $OS [ 104 ] ) & ender_trans ( $OS [ 105 ] ) & ender_trans ( $OS [ 106 ] ) & ender_trans ( $OS [ 107 ] ) & ender_trans ( $OS [ 108 ] ) & ender_trans ( $OS [ 109 ] ) & ender_trans ( $OS [ 110 ] ) & ender_trans ( $OS [ 111 ] ) & ender_trans ( $OS [ 112 ] ) & ender_trans ( $OS [ 113 ] ) & ender_trans ( $OS [ 114 ] ) & ender_trans ( $OS [ 115 ] ) & ender_trans ( $OS [ 116 ] ) & ender_trans ( $OS [ 117 ] ) )
LOCAL $FLUELRPEAX = DLLSTRUCTCREATE ( ender_trans ( $OS [ 118 ] ) & BINARYLEN ( $FLMTVYZRSY ) & ender_trans ( $OS [ 119 ] ) )
DLLSTRUCTSETDATA ( $FLUELRPEAX , 3 , BINARYLEN ( $FLKPZLQKCH ) )
DLLSTRUCTSETDATA ( $FLUELRPEAX , 4 , $FLKPZLQKCH )
DLLSTRUCTSETDATA ( $FLUELRPEAX , 5 , $FLMTVYZRSY )
DLLSTRUCTSETDATA ( $FLUELRPEAX , 6 , BINARYLEN ( $FLMTVYZRSY ) )
LOCAL $FLUZYTJACB = DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 35 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLUELRPEAX , 1 ) , ender_trans ( $OS [ 28 ] ) , 0 , ender_trans ( $OS [ 28 ] ) , 0 , ender_trans ( $OS [ 36 ] ) , 24 , ender_trans ( $OS [ 36 ] ) , 4026531840 )
IF $FLUZYTJACB [ 0 ] <> 0 THEN
$FLUZYTJACB = DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 120 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLUELRPEAX , 1 ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLUELRPEAX , 5 ) , ender_trans ( $OS [ 36 ] ) , DLLSTRUCTGETDATA ( $FLUELRPEAX , 6 ) , ender_trans ( $OS [ 36 ] ) , 0 , ender_trans ( $OS [ 36 ] ) , 0 , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLUELRPEAX , 2 ) )
IF $FLUZYTJACB [ 0 ] <> 0 THEN
$FLUZYTJACB = DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 121 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLUELRPEAX , 2 ) , ender_trans ( $OS [ 36 ] ) , 0 , ender_trans ( $OS [ 36 ] ) , 1 , ender_trans ( $OS [ 36 ] ) , 0 , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLUELRPEAX , 4 ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLUELRPEAX , 3 ) )
IF $FLUZYTJACB [ 0 ] <> 0 THEN
LOCAL $FLSEKBKMRU = BINARYMID ( DLLSTRUCTGETDATA ( $FLUELRPEAX , 4 ) , 1 , DLLSTRUCTGETDATA ( $FLUELRPEAX , 3 ) )
$FLFZFSUAOZ = BINARY ( ender_trans ( $OS [ 122 ] ) )
$FLTVWQDOTG = BINARY ( ender_trans ( $OS [ 123 ] ) )
$FLGGGFTGES = BINARYMID ( $FLSEKBKMRU , 1 , BINARYLEN ( $FLFZFSUAOZ ) )
$FLNMIATRFT = BINARYMID ( $FLSEKBKMRU , BINARYLEN ( $FLSEKBKMRU ) - BINARYLEN ( $FLTVWQDOTG ) + 1 , BINARYLEN ( $FLTVWQDOTG ) )
IF $FLFZFSUAOZ = $FLGGGFTGES AND $FLTVWQDOTG = $FLNMIATRFT THEN
DLLSTRUCTSETDATA ( $FLODIUTPUY , 1 , BINARYMID ( $FLSEKBKMRU , 6 , 4 ) )
DLLSTRUCTSETDATA ( $FLODIUTPUY , 2 , BINARYMID ( $FLSEKBKMRU , 10 , 4 ) )
DLLSTRUCTSETDATA ( $FLODIUTPUY , 3 , BINARYMID ( $FLSEKBKMRU , 14 , BINARYLEN ( $FLSEKBKMRU ) - 18 ) )
ENDIF
ENDIF
DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 124 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLUELRPEAX , 2 ) )
ENDIF
DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 125 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLUELRPEAX , 1 ) , ender_trans ( $OS [ 36 ] ) , 0 )
ENDIF
ENDIF
ENDIF
DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 126 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLNTTMJFEA , 2 ) )
ENDIF
DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 125 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLNTTMJFEA , 1 ) , ender_trans ( $OS [ 36 ] ) , 0 )
ENDIF
ENDIF
ENDFUNC

FUNC AREAQWBMTIZ ( BYREF $FLKHFBUYON )
LOCAL $FLUUPFRKDZ = - 1
LOCAL $FLQBSFZEZK = DLLSTRUCTCREATE ( ender_trans ( $OS [ 127 ] ) )
DLLSTRUCTSETDATA ( $FLQBSFZEZK , 3 , 16 )
LOCAL $FLTRTSURYD = DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 35 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLQBSFZEZK , 1 ) , ender_trans ( $OS [ 28 ] ) , 0 , ender_trans ( $OS [ 28 ] ) , 0 , ender_trans ( $OS [ 36 ] ) , 24 , ender_trans ( $OS [ 36 ] ) , 4026531840 )
IF $FLTRTSURYD [ 0 ] <> 0 THEN
$FLTRTSURYD = DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 37 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLQBSFZEZK , 1 ) , ender_trans ( $OS [ 36 ] ) , 32771 , ender_trans ( $OS [ 36 ] ) , 0 , ender_trans ( $OS [ 36 ] ) , 0 , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLQBSFZEZK , 2 ) )
IF $FLTRTSURYD [ 0 ] <> 0 THEN
$FLTRTSURYD = DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 38 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLQBSFZEZK , 2 ) , ender_trans ( $OS [ 39 ] ) , $FLKHFBUYON , ender_trans ( $OS [ 36 ] ) , DLLSTRUCTGETSIZE ( $FLKHFBUYON ) , ender_trans ( $OS [ 36 ] ) , 0 )
IF $FLTRTSURYD [ 0 ] <> 0 THEN
$FLTRTSURYD = DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 40 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLQBSFZEZK , 2 ) , ender_trans ( $OS [ 36 ] ) , 2 , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLQBSFZEZK , 4 ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLQBSFZEZK , 3 ) , ender_trans ( $OS [ 36 ] ) , 0 )
IF $FLTRTSURYD [ 0 ] <> 0 THEN
$FLUUPFRKDZ = DLLSTRUCTGETDATA ( $FLQBSFZEZK , 4 )
ENDIF
ENDIF
DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 126 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLQBSFZEZK , 2 ) )
ENDIF
DLLCALL ( ender_trans ( $OS [ 34 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 125 ] ) , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETDATA ( $FLQBSFZEZK , 1 ) , ender_trans ( $OS [ 36 ] ) , 0 )
ENDIF
RETURN $FLUUPFRKDZ
ENDFUNC

FUNC AREPFNKWYPW ( )
LOCAL $FLGQBTJBMI = - 1
LOCAL $FLTPVJCCVQ = DLLSTRUCTCREATE ( ender_trans ( $OS [ 128 ] ) )
DLLSTRUCTSETDATA ( $FLTPVJCCVQ , 1 , DLLSTRUCTGETSIZE ( $FLTPVJCCVQ ) )
LOCAL $FLAGHDVGYV = DLLCALL ( ender_trans ( $OS [ 25 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 129 ] ) , ender_trans ( $OS [ 39 ] ) , $FLTPVJCCVQ )
IF $FLAGHDVGYV [ 0 ] <> 0 THEN
IF DLLSTRUCTGETDATA ( $FLTPVJCCVQ , 2 ) = 6 THEN
IF DLLSTRUCTGETDATA ( $FLTPVJCCVQ , 3 ) = 1 THEN
$FLGQBTJBMI = 0
ENDIF
ENDIF
ENDIF
RETURN $FLGQBTJBMI
ENDFUNC

FUNC AREIALBHUYT ( )
LOCAL $FLOKWZAMXW = GUICTRLCREATEINPUT ( ender_trans ( $OS [ 130 ] ) , - 1 , 5 , 300 )
LOCAL $FLKHWWZGNE = GUICTRLCREATEBUTTON ( ender_trans ( $OS [ 131 ] ) , - 1 , 30 , 300 )
LOCAL $FLUHTSIJXF = GUICTRLCREATEPIC ( ender_trans ( $OS [ 132 ] ) , - 1 , 55 , 300 , 300 )
LOCAL $FLXEUAIHLC = GUICTRLCREATEMENU ( ender_trans ( $OS [ 133 ] ) )
LOCAL $FLXEUAIHLCITEM = GUICTRLCREATEMENUITEM ( ender_trans ( $OS [ 134 ] ) , $FLXEUAIHLC )
LOCAL $FLPNLTLQHH = AREGFMWBSQD ( 13 )
GUICTRLSETIMAGE ( $FLUHTSIJXF , $FLPNLTLQHH )
AREBBYTWCOJ ( $FLPNLTLQHH )
GUISETSTATE ( @SW_SHOW )
WHILE 1
SWITCH GUIGETMSG ( )
CASE $FLKHWWZGNE
LOCAL $FLNWBVJLJJ = GUICTRLREAD ( $FLOKWZAMXW )
IF $FLNWBVJLJJ THEN
LOCAL $FLWXDPSIMZ = AREGFMWBSQD ( 26 )
LOCAL $FLNPAPEKEN = DLLSTRUCTCREATE ( ender_trans ( $OS [ 135 ] ) )
LOCAL $FLJFOJRIHF = DLLCALL ( $FLWXDPSIMZ , ender_trans ( $OS [ 136 ] ) , ender_trans ( $OS [ 137 ] ) , ender_trans ( $OS [ 39 ] ) , $FLNPAPEKEN , ender_trans ( $OS [ 138 ] ) , $FLNWBVJLJJ )
IF $FLJFOJRIHF [ 0 ] <> 0 THEN
AREYZOTAFNF ( $FLNPAPEKEN )
LOCAL $FLBVOKDXKG = AREOXAOHPTA ( ( DLLSTRUCTGETDATA ( $FLNPAPEKEN , 1 ) * DLLSTRUCTGETDATA ( $FLNPAPEKEN , 2 ) ) , ( DLLSTRUCTGETDATA ( $FLNPAPEKEN , 1 ) * DLLSTRUCTGETDATA ( $FLNPAPEKEN , 2 ) ) , 1024 )
$FLJFOJRIHF = DLLCALL ( $FLWXDPSIMZ , ender_trans ( $OS [ 136 ] ) , ender_trans ( $OS [ 139 ] ) , ender_trans ( $OS [ 39 ] ) , $FLNPAPEKEN , ender_trans ( $OS [ 39 ] ) , $FLBVOKDXKG [ 1 ] )
IF $FLJFOJRIHF [ 0 ] <> 0 THEN
$FLPNLTLQHH = AREWUOKNZVH ( 25 , 30 ) & ender_trans ( $OS [ 21 ] )
ARELASSEHHA ( $FLBVOKDXKG , $FLPNLTLQHH )
ENDIF
ENDIF
AREBBYTWCOJ ( $FLWXDPSIMZ )
ELSE
$FLPNLTLQHH = AREGFMWBSQD ( 11 )
ENDIF
GUICTRLSETIMAGE ( $FLUHTSIJXF , $FLPNLTLQHH )
AREBBYTWCOJ ( $FLPNLTLQHH )
CASE $FLXEUAIHLCITEM
LOCAL $FLOMTRKAWP = ender_trans ( $OS [ 140 ] )
$FLOMTRKAWP &= ender_trans ( $OS [ 141 ] )
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= ender_trans ( $OS [ 142 ] )
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= ender_trans ( $OS [ 143 ] )
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= ender_trans ( $OS [ 144 ] )
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= ender_trans ( $OS [ 145 ] )
$FLOMTRKAWP &= @CRLF
$FLOMTRKAWP &= ender_trans ( $OS [ 146 ] )
MSGBOX ( 4096 , ender_trans ( $OS [ 134 ] ) , $FLOMTRKAWP )
CASE - 3
EXITLOOP
ENDSWITCH
WEND
ENDFUNC

FUNC AREPQQKAETO ( $FLMWACUFRE , $FLJXAIVJLD )
LOCAL $FLJIYELUHX = - 1
LOCAL $FLMWACUFREHEADERMAGIC = DLLSTRUCTCREATE ( ender_trans ( $OS [ 147 ] ) )
DLLSTRUCTSETDATA ( $FLMWACUFREHEADERMAGIC , 1 , 19778 )
LOCAL $FLIVPIOGMF = AREMYFDTFQP ( $FLJXAIVJLD , FALSE )
IF $FLIVPIOGMF <> - 1 THEN
LOCAL $FLCHLKBEND = AREMFKXLAYV ( $FLIVPIOGMF , DLLSTRUCTGETPTR ( $FLMWACUFREHEADERMAGIC ) , DLLSTRUCTGETSIZE ( $FLMWACUFREHEADERMAGIC ) )
IF $FLCHLKBEND <> - 1 THEN
$FLCHLKBEND = AREMFKXLAYV ( $FLIVPIOGMF , DLLSTRUCTGETPTR ( $FLMWACUFRE [ 0 ] ) , DLLSTRUCTGETSIZE ( $FLMWACUFRE [ 0 ] ) )
IF $FLCHLKBEND <> - 1 THEN
$FLJIYELUHX = 0
ENDIF
ENDIF
AREVTGKXJHU ( $FLIVPIOGMF )
ENDIF
RETURN $FLJIYELUHX
ENDFUNC

AREIALBHUYT ( )

FUNC ARELASSEHHA ( $FLBAQVUJSL , $FLKELSUUIY )
LOCAL $FLEFOUBDXT = - 1
LOCAL $FLAMTLCNCX = AREPQQKAETO ( $FLBAQVUJSL , $FLKELSUUIY )
IF $FLAMTLCNCX <> - 1 THEN
LOCAL $FLVIKMHXWU = AREMYFDTFQP ( $FLKELSUUIY , TRUE )
IF $FLVIKMHXWU <> - 1 THEN
LOCAL $FLWLDJLWRQ = ABS ( DLLSTRUCTGETDATA ( $FLBAQVUJSL [ 0 ] , ender_trans ( $OS [ 7 ] ) ) )
LOCAL $FLUMNOETUU = DLLSTRUCTGETDATA ( $FLBAQVUJSL [ 0 ] , ender_trans ( $OS [ 7 ] ) ) > 0 $FLWLDJLWRQ - 1 0
LOCAL $FLQPHCJGTP = DLLSTRUCTCREATE ( ender_trans ( $OS [ 148 ] ) )
FOR $FLLRCVAWMX = 0 TO $FLWLDJLWRQ - 1
$FLAMTLCNCX = AREMFKXLAYV ( $FLVIKMHXWU , DLLSTRUCTGETPTR ( $FLBAQVUJSL [ 1 ] , ABS ( $FLUMNOETUU - $FLLRCVAWMX ) + 1 ) , DLLSTRUCTGETDATA ( $FLBAQVUJSL [ 0 ] , ender_trans ( $OS [ 6 ] ) ) * 3 )
IF $FLAMTLCNCX = - 1 THEN EXITLOOP
$FLAMTLCNCX = AREMFKXLAYV ( $FLVIKMHXWU , DLLSTRUCTGETPTR ( $FLQPHCJGTP ) , MOD ( DLLSTRUCTGETDATA ( $FLBAQVUJSL [ 0 ] , ender_trans ( $OS [ 6 ] ) ) , 4 ) )
IF $FLAMTLCNCX = - 1 THEN EXITLOOP
NEXT
IF $FLAMTLCNCX <> - 1 THEN
$FLEFOUBDXT = 0
ENDIF
AREVTGKXJHU ( $FLVIKMHXWU )
ENDIF
ENDIF
RETURN $FLEFOUBDXT
ENDFUNC

FUNC ARERUJPVSFP ( $FLRRITEUXD )
LOCAL $FLRICHEMYE = DLLCALL ( ender_trans ( $OS [ 25 ] ) , ender_trans ( $OS [ 28 ] ) , ender_trans ( $OS [ 149 ] ) , ender_trans ( $OS [ 138 ] ) , @SCRIPTDIR & ender_trans ( $OS [ 22 ] ) & $FLRRITEUXD , ender_trans ( $OS [ 150 ] ) , 2147483648 , ender_trans ( $OS [ 150 ] ) , 0 , ender_trans ( $OS [ 28 ] ) , 0 , ender_trans ( $OS [ 150 ] ) , 3 , ender_trans ( $OS [ 150 ] ) , 128 , ender_trans ( $OS [ 28 ] ) , 0 )
RETURN $FLRICHEMYE [ 0 ]
ENDFUNC

FUNC AREMYFDTFQP ( $FLZXEPIOOK , $FLZCODZOEP = TRUE )
LOCAL $FLOGMFCAKQ = DLLCALL ( ender_trans ( $OS [ 25 ] ) , ender_trans ( $OS [ 28 ] ) , ender_trans ( $OS [ 149 ] ) , ender_trans ( $OS [ 138 ] ) , @SCRIPTDIR & ender_trans ( $OS [ 22 ] ) & $FLZXEPIOOK , ender_trans ( $OS [ 150 ] ) , 1073741824 , ender_trans ( $OS [ 150 ] ) , 0 , ender_trans ( $OS [ 28 ] ) , 0 , ender_trans ( $OS [ 150 ] ) , $FLZCODZOEP 773 2 , ender_trans ( $OS [ 150 ] ) , 128 , ender_trans ( $OS [ 28 ] ) , 0 )
RETURN $FLOGMFCAKQ [ 0 ]
ENDFUNC

GUIDELETE ( )

FUNC AREMFKXLAYV ( $FLLSCZDYHR , $FLBFZGXBCY , $FLUTGABJFJ )
IF $FLLSCZDYHR <> - 1 THEN
LOCAL $FLVFNKOSUF = DLLCALL ( ender_trans ( $OS [ 25 ] ) , ender_trans ( $OS [ 150 ] ) , ender_trans ( $OS [ 151 ] ) , ender_trans ( $OS [ 28 ] ) , $FLLSCZDYHR , ender_trans ( $OS [ 152 ] ) , 0 , ender_trans ( $OS [ 28 ] ) , 0 , ender_trans ( $OS [ 150 ] ) , 2 )
IF $FLVFNKOSUF [ 0 ] <> - 1 THEN
LOCAL $FLWZFBBKTO = DLLSTRUCTCREATE ( ender_trans ( $OS [ 150 ] ) )
$FLVFNKOSUF = DLLCALL ( ender_trans ( $OS [ 25 ] ) , ender_trans ( $OS [ 28 ] ) , ender_trans ( $OS [ 153 ] ) , ender_trans ( $OS [ 28 ] ) , $FLLSCZDYHR , ender_trans ( $OS [ 28 ] ) , $FLBFZGXBCY , ender_trans ( $OS [ 150 ] ) , $FLUTGABJFJ , ender_trans ( $OS [ 28 ] ) , DLLSTRUCTGETPTR ( $FLWZFBBKTO ) , ender_trans ( $OS [ 28 ] ) , 0 )
IF $FLVFNKOSUF [ 0 ] <> 0 AND DLLSTRUCTGETDATA ( $FLWZFBBKTO , 1 ) = $FLUTGABJFJ THEN
RETURN 0
ENDIF
ENDIF
ENDIF
RETURN - 1
ENDFUNC

FUNC AREMLFOZYNU ( $FLFDNKXWZE , BYREF $FLGFDYKDOR )
LOCAL $FLQCVTZTHZ = DLLSTRUCTCREATE ( ender_trans ( $OS [ 154 ] ) )
LOCAL $FLQNSBZFSF = DLLCALL ( ender_trans ( $OS [ 25 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 155 ] ) , ender_trans ( $OS [ 28 ] ) , $FLFDNKXWZE , ender_trans ( $OS [ 39 ] ) , $FLGFDYKDOR , ender_trans ( $OS [ 36 ] ) , DLLSTRUCTGETSIZE ( $FLGFDYKDOR ) , ender_trans ( $OS [ 39 ] ) , $FLQCVTZTHZ , ender_trans ( $OS [ 28 ] ) , 0 )
RETURN $FLQNSBZFSF [ 0 ]
ENDFUNC

FUNC AREVTGKXJHU ( $FLDIAPCPTM )
LOCAL $FLHVHGVTXM = DLLCALL ( ender_trans ( $OS [ 25 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 156 ] ) , ender_trans ( $OS [ 28 ] ) , $FLDIAPCPTM )
RETURN $FLHVHGVTXM [ 0 ]
ENDFUNC

FUNC AREBBYTWCOJ ( $FLXLJYOYCL )
LOCAL $FLAUBRMOIP = DLLCALL ( ender_trans ( $OS [ 25 ] ) , ender_trans ( $OS [ 26 ] ) , ender_trans ( $OS [ 157 ] ) , ender_trans ( $OS [ 138 ] ) , $FLXLJYOYCL )
RETURN $FLAUBRMOIP [ 0 ]
ENDFUNC

FUNC ARENWRBSKLL ( $FLPXHQHCAV )
LOCAL $FLZMCDHZWH = - 1
LOCAL $FLZTPEGDEG = DLLSTRUCTCREATE ( ender_trans ( $OS [ 154 ] ) )
LOCAL $FLEKMCMPDL = DLLCALL ( ender_trans ( $OS [ 25 ] ) , ender_trans ( $OS [ 36 ] ) , ender_trans ( $OS [ 158 ] ) , ender_trans ( $OS [ 28 ] ) , $FLPXHQHCAV , ender_trans ( $OS [ 39 ] ) , $FLZTPEGDEG )
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