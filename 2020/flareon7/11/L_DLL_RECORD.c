//**    NewinRegionsea_export.dll 搞笑
//**    KeyboardtimerWolib_export.dll 搞笑

//**    InfspellTimerver_export.dll 搞笑


///**  CaclibRegionmap_export.dll

void __fastcall sub_180001070(int a1, __int64 a2)
{
  wchar_t *v3; // rax
  const wchar_t *v4; // rbx
  wchar_t *v5; // rax
  const WCHAR *v6; // rcx

  if ( a1 == 1 )
  {
    v3 = 8576b0d0_10(**(a2 + 8) + 2);
    v4 = v3;
    if ( v3 )
    {
      memcpy(v3, *(*(a2 + 8) + 8i64), **(a2 + 8));
      v4[**(a2 + 8) >> 1] = 0;
      v5 = wcsrchr(v4, '\\');
      if ( v5 )
        v6 = v5 + 1;
      else
        v6 = v4;
      if ( !StrCmpNIW(v6, (&unk_180005060 + qword_180003010), 6) && !e6954637_8(0i64) )
        e6954637_3();
      8576b0d0_11(v4);
    }
  }
}

///*  CalccalcLogicnew_export.dll

BOOL __stdcall DllEntryPoint(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)
{
  __int64 v3; // rbp
  unsigned int v5; // eax
  int v6; // eax
  LPCSTR lpText[2]; // [rsp+0h] [rbp-48h]
  __m128i v8; // [rsp+10h] [rbp-38h]
  __m128i v9; // [rsp+20h] [rbp-28h]
  const char *v10; // [rsp+30h] [rbp-18h]
  __int64 v11; // [rsp+40h] [rbp-8h]

  if ( fdwReason == 1 )
  {
    v11 = v3;
    *(__m128i *)lpText = _mm_unpacklo_epi64(
                           (__m128i)(unsigned __int64)"What are you up to? I've got my eye on you!",
                           (__m128i)(unsigned __int64)"Did you really think this was going to work?");
    v10 = "I see what you are doing, but that's not gonna work.";
    v8 = _mm_unpacklo_epi64(
           (__m128i)(unsigned __int64)"Please don't do that, you are hurting my feelings.",
           (__m128i)(unsigned __int64)"Come on, you don't think I can let you win this easily, do you?");
    v9 = _mm_unpacklo_epi64(
           (__m128i)(unsigned __int64)"Don't be a noob. You need to try a bit harder than this...",
           (__m128i)(unsigned __int64)"I am at a loss for words as to how you even made it this far in the challenges.");
    v5 = GetTickCount();
    srand(v5);
    v6 = rand();
    MessageBoxA(0i64, lpText[v6 % 7], "Hey", 0x40u);
    ExitProcess(0);
  }
  return 1;
}

///*  CalciconLogicthre_export.dll

BOOL __stdcall DllEntryPoint(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)
{
  __int64 v3; // rbp
  unsigned int v5; // eax
  int v6; // eax
  LPCSTR lpText[2]; // [rsp+0h] [rbp-48h]
  __m128i v8; // [rsp+10h] [rbp-38h]
  __m128i v9; // [rsp+20h] [rbp-28h]
  const char *v10; // [rsp+30h] [rbp-18h]
  __int64 v11; // [rsp+40h] [rbp-8h]

  if ( fdwReason == 1 )
  {
    v11 = v3;
    *(__m128i *)lpText = _mm_unpacklo_epi64(
                           (__m128i)(unsigned __int64)"What are you up to? I've got my eye on you!",
                           (__m128i)(unsigned __int64)"Did you really think this was going to work?");
    v10 = "I see what you are doing, but that's not gonna work.";
    v8 = _mm_unpacklo_epi64(
           (__m128i)(unsigned __int64)"Please don't do that, you are hurting my feelings.",
           (__m128i)(unsigned __int64)"Come on, you don't think I can let you win this easily, do you?");
    v9 = _mm_unpacklo_epi64(
           (__m128i)(unsigned __int64)"Don't be a noob. You need to try a bit harder than this...",
           (__m128i)(unsigned __int64)"I am at a loss for words as to how you even made it this far in the challenges.");
    v5 = GetTickCount();
    srand(v5);
    v6 = rand();
    MessageBoxA(0i64, lpText[v6 % 7], "Hey", 0x40u);
    ExitProcess(0);
  }
  return 1;
}

///****   DatethrWorkscreen_export.dll

__int64 __fastcall start(__int64 a1, int a2)
{
  unsigned int v3; // ebx
  DWORD v4; // eax
  __int64 v6; // [rsp+48h] [rbp+20h] BYREF

  v3 = 1;
  if ( !a2 )
  {
    _InterlockedAdd(&dword_180003000, 0xFFFFFFFF);
    return v3;
  }
  if ( a2 == 1 && _InterlockedIncrement(&dword_180003000) == 1 )
  {
    qword_180003008 = 8576b0d0_2();
    v4 = 8576b0d0_25(a1, 0i64, &dword_180003004);
    if ( v4 )
    {
LABEL_10:
      SetLastError(v4);
      return 0;
    }
    if ( (dword_180003004 ^ *(_DWORD *)(qword_180003008 + 324)) != 0xFA90AC2 )
    {
      v4 = 1;
      goto LABEL_10;
    }
    v6 = 0i64;
    v4 = e6954637_9(&v6, 0i64, 0i64);
    if ( v4 )
      goto LABEL_10;
    v4 = e6954637_4();
    if ( v4 )
      goto LABEL_10;
    v4 = e6954637_3();
    if ( v4 )
      goto LABEL_10;
  }
  return v3;
}

//*****    DiskproIdbui_export.dll

BOOL __stdcall DllEntryPoint(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)
{
  __int64 v3; // rbp
  unsigned int v5; // eax
  int v6; // eax
  LPCSTR lpText[2]; // [rsp+0h] [rbp-48h]
  __m128i v8; // [rsp+10h] [rbp-38h]
  __m128i v9; // [rsp+20h] [rbp-28h]
  const char *v10; // [rsp+30h] [rbp-18h]
  __int64 v11; // [rsp+40h] [rbp-8h]

  if ( fdwReason == 1 )
  {
    v11 = v3;
    *(__m128i *)lpText = _mm_unpacklo_epi64(
                           (__m128i)(unsigned __int64)"What are you up to? I've got my eye on you!",
                           (__m128i)(unsigned __int64)"Did you really think this was going to work?");
    v10 = "I see what you are doing, but that's not gonna work.";
    v8 = _mm_unpacklo_epi64(
           (__m128i)(unsigned __int64)"Please don't do that, you are hurting my feelings.",
           (__m128i)(unsigned __int64)"Come on, you don't think I can let you win this easily, do you?");
    v9 = _mm_unpacklo_epi64(
           (__m128i)(unsigned __int64)"Don't be a noob. You need to try a bit harder than this...",
           (__m128i)(unsigned __int64)"I am at a loss for words as to how you even made it this far in the challenges.");
    v5 = GetTickCount();
    srand(v5);
    v6 = rand();
    MessageBoxA(0i64, lpText[v6 % 7], "Hey", 0x40u);
    ExitProcess(0);
  }
  return 1;
}


//****       InflibExplorertru_export

BOOL __stdcall DllEntryPoint(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)
{
  __int64 v3; // rbp
  unsigned int v5; // eax
  int v6; // eax
  LPCSTR lpText[2]; // [rsp+0h] [rbp-48h]
  __m128i v8; // [rsp+10h] [rbp-38h]
  __m128i v9; // [rsp+20h] [rbp-28h]
  const char *v10; // [rsp+30h] [rbp-18h]
  __int64 v11; // [rsp+40h] [rbp-8h]

  if ( fdwReason == 1 )
  {
    v11 = v3;
    *(__m128i *)lpText = _mm_unpacklo_epi64(
                           (__m128i)(unsigned __int64)"What are you up to? I've got my eye on you!",
                           (__m128i)(unsigned __int64)"Did you really think this was going to work?");
    v10 = "I see what you are doing, but that's not gonna work.";
    v8 = _mm_unpacklo_epi64(
           (__m128i)(unsigned __int64)"Please don't do that, you are hurting my feelings.",
           (__m128i)(unsigned __int64)"Come on, you don't think I can let you win this easily, do you?");
    v9 = _mm_unpacklo_epi64(
           (__m128i)(unsigned __int64)"Don't be a noob. You need to try a bit harder than this...",
           (__m128i)(unsigned __int64)"I am at a loss for words as to how you even made it this far in the challenges.");
    v5 = GetTickCount();
    srand(v5);
    v6 = rand();
    MessageBoxA(0i64, lpText[v6 % 7], "Hey", 0x40u);
    ExitProcess(0);
  }
  return 1;
}


//****   PrintsolutSavetheme_export.dll


__int64 __fastcall sub_18000303C(__int64 a1)
{
  __int64 result; // rax
  __int64 v3; // [rsp+50h] [rbp+18h] BYREF

  qword_1800053C0 = 8576b0d0_2();
  result = 8576b0d0_75(a1, &unk_1800070A8, 0i64, &dword_180007000, &qword_180005270);
  if ( !(_DWORD)result )
  {
    if ( (dword_180007000 ^ *(_DWORD *)(qword_1800053C0 + 324)) == 1057008383 )
    {
      v3 = 0i64;
      result = e6954637_9(&v3, &unk_180005210, 0i64);
      if ( !(_DWORD)result )
      {
        result = e6954637_3();
        if ( !(_DWORD)result )
        {
          if ( (unsigned int)sub_180002160() )
          {
            result = 0i64;
          }
          else
          {
            qword_180005008 = (__int64)&_ImageBase + qword_180005270 + 29259;
            qword_180005000 = (__int64)&_ImageBase + qword_180005270 + 28676;
            qword_180005030 = (__int64)&_ImageBase + qword_180005270 + 29282;
            qword_180005028 = (__int64)&_ImageBase + qword_180005270 + 28676;
            qword_180005058 = (__int64)&_ImageBase + qword_180005270 + 29298;
            qword_180005050 = (__int64)&_ImageBase + qword_180005270 + 28676;
            qword_180005080 = (__int64)&_ImageBase + qword_180005270 + 29324;
            qword_180005078 = (__int64)&_ImageBase + qword_180005270 + 28676;
            qword_1800050A8 = (__int64)&_ImageBase + qword_180005270 + 29343;
            qword_1800050A0 = (__int64)&_ImageBase + qword_180005270 + 28676;
            qword_1800050C8 = (__int64)&_ImageBase + qword_180005270 + 28676;
            qword_1800050D0 = (__int64)&_ImageBase + qword_180005270 + 29363;
            result = 8576b0d0_32(&unk_180005180, 6i64, &unk_1800050F0, 6i64, 0i64);
          }
        }
      }
    }
    else
    {
      result = 1i64;
    }
  }
  return result;
}

//****  ProtocolmagicWordeskt_export.dll Email账户 和注册表相关

//****  RowmapGuiprotocol_export.dll AVI File Init

//****  ScreenserProtocolacces_export.dll

__int64 __fastcall start(__int64 a1, int a2)
{
  unsigned int v3; // ebx
  DWORD v4; // eax
  __int64 v6; // [rsp+48h] [rbp+20h] BYREF

  v3 = 1;
  if ( !a2 )
  {
    _InterlockedAdd(&dword_180003000, 0xFFFFFFFF);
    return v3;
  }
  if ( a2 == 1 && _InterlockedIncrement(&dword_180003000) == 1 )
  {
    qword_180003008 = 8576b0d0_2();
    v4 = 8576b0d0_25(a1, 0i64, &dword_180003004);
    if ( v4 )
    {
LABEL_10:
      SetLastError(v4);
      return 0;
    }
    if ( (dword_180003004 ^ *(_DWORD *)(qword_180003008 + 324)) != -874826905 )
    {
      v4 = 1;
      goto LABEL_10;
    }
    v6 = 0i64;
    v4 = e6954637_9(&v6, 0i64, 0i64);
    if ( v4 )
      goto LABEL_10;
    v4 = e6954637_4();
    if ( v4 )
      goto LABEL_10;
    v4 = e6954637_3();
    if ( v4 )
      goto LABEL_10;
  }
  return v3;
}

//****  SoflogicMagiclink_export.dll  iexplore.hlp (ULONG_PTR)L"cert_ovr.htm";
              v13 = 0;
              v14 = L"iexplore.chm > iedefault";

//**** TasknetCharconso_export.dll 搞笑

//****  ThemespellDaytheme_export.dll 和第一个一样

void __fastcall sub_180001070(int a1, __int64 a2)
{
  wchar_t *v3; // rax
  const wchar_t *v4; // rbx
  wchar_t *v5; // rax
  const WCHAR *v6; // rcx

  if ( a1 == 1 )
  {
    v3 = (wchar_t *)8576b0d0_10((unsigned int)**(unsigned __int16 **)(a2 + 8) + 2);
    v4 = v3;
    if ( v3 )
    {
      memcpy(v3, *(const void **)(*(_QWORD *)(a2 + 8) + 8i64), **(unsigned __int16 **)(a2 + 8));
      v4[(unsigned __int64)**(unsigned __int16 **)(a2 + 8) >> 1] = 0;
      v5 = wcsrchr(v4, 0x5Cu);
      if ( v5 )
        v6 = v5 + 1;
      else
        v6 = v4;
      if ( !StrCmpNIW(v6, (PCWSTR)((char *)&unk_180005060 + qword_180003010), 6) && !(unsigned int)e6954637_8(0i64) )
        e6954637_3();
      8576b0d0_11(v4);
    }
  }
}

//****  TimermagSelink_export.dll 搞笑

//**** WebmodeThemearchive_export.dll  inet_addr DNS相关

//****  WebsoftwareProcesstemplate_export.dll 看到和主病毒一样的结构和代码

//****  WordlibSystemser_export.dll  复杂函数，用来做撤退的感觉