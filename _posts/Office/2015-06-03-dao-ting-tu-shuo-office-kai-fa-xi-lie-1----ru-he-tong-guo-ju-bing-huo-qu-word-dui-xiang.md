---
layout: post
title: "道听途说Office开发系列1 - 如何通过句柄获取Word对象"
description: "Delphi下获取Word句柄的几种方式"
category: "Office"
modified: 2015-06-03 13:31
tags: "Office VBA COM Delphi ActiveX"
---
"test-jb-setup"

# 前言
断断续续做了很多年的OA，伴随整个OA生涯的是Office的研发，算是一个回忆吧。

通常Office控件分2种。  

* 嵌入  
   嵌入方式比较好理解，就是在ActiveX控件里面显示Word内容。  
   VC的版本，在微软早起有一个dso的源码。给大家很多思路。
   Delphi版本一般是直接使用OLEContainer控件。
   
   不管用哪种方式，开发成本都是不低的。如果是Delphi的版本，基本也需要自己重写这个对象了。
   国内2个比较有代表性的商业产品正好是2个不同的思路。
    
* 独立
   独立的意思是单独启动Office进程，然后进行交互。首当其冲的问题是如何获取Office对象，并进而让ActiveX和这个对象建立联系。
   
   2种方式都经历过，用得比较多的还是第2种方式。
   
   如果能获取到IDispath接口，就可以和Delphi自己的WordApplication建立关联，也就能捕获Office的事件。

# 如何获取Word对象


## 1、通过com对象
   通过Javascript把word对象传入到ActiveX控件中。
    {% highlight delphi %} 
   unit uCoGetServerPID;


// The web page is at http://www.winwonk.com/writing/cogetserverpid/

interface

uses Windows;

function CoGetServerPID (const unk: IUnknown; var dwPID: DWORD): HRESULT;

implementation

uses ActiveX, ComObj, Variants;

type
  // Used to verify the COM object's signature and to sniff the PID out of the header.
  TComObjRefHdr = packed record
    signature: DWORD;  	// Should be 'MEOW'
    padding  : array[0..47] of Byte;
    pid      : WORD;
  end;
  PComObjRefHdr = ^TComObjRefHdr;

function CoGetServerPID(const unk: IUnknown; var dwPID: DWORD): HRESULT;
var
  PObjRefHdr       : PComObjRefHdr;
  spProxyManager   : IUnknown;
  spMarshalStream  : IStream;
  liNewPos         : Int64;
  HG               : HGLOBAL;

const
  IID_IUnknown: TGUID = (D1:$00000000;D2:$0000;D3:$0000;D4:($C0,$00,$00,$00,$00,$00,$00,$46));

begin

  if VarIsNULL(unk) then begin
    Result := E_INVALIDARG;
    Exit;
  end;

  // Check if not standard proxy.  We can't make any assumptions about remote PID
  Result := unk.QueryInterface(IID_IProxyManager, spProxyManager);
  if Failed(Result) then Exit;

  // Marshall the interface to get a new OBJREF
  Result := CreateStreamOnHGlobal(0, True, spMarshalStream);
  if Failed(Result) then Exit;

  Result := CoMarshalInterface(spMarshalStream, IID_IUnknown, unk, MSHCTX_INPROC, nil, MSHLFLAGS_NORMAL);
  if Failed(Result) then Exit;

  // We just created the stream.  So go back to a raw pointer.
  Result := GetHGlobalFromStream(spMarshalStream, HG);

  if Succeeded(Result) then try

    // Start out pessimistic
    Result := RPC_E_INVALID_OBJREF;

    PObjRefHdr := GlobalLock(HG);

    if Assigned(PObjRefHdr) then begin
      // Verify that the signature is MEOW
      if PObjRefHdr^.signature = $574f454d then begin
        // We got the remote PID
        dwPID  := PObjRefHdr^.pid;
        Result := S_OK;
      end;
    end;

  finally
    GlobalUnlock(HG);
  end;

  // Rewind stream and release marshal data to keep refcount in order
  liNewPos := 0;
  spMarshalStream.Seek(0, STREAM_SEEK_SET, liNewPos);
  CoReleaseMarshalData(spMarshalStream);

end;

end.


{% endhighlight %} 

## 2、通过窗口标题
{% highlight delphi %} 
procedure TMainForm.Button3Click(Sender: TObject);
Const OBJID_NATIVEOM : Integer = $fffffff0;
var
    WordObject: IDispatch; // IDispatch;
    hWindow: hWnd;
    FDispatcher: TWordDocumentEventDispatcher;
    WordApp: _Application;
begin
    hWindow := GetWordHandle(Trim(LabeledEdit1.Text));
    ForegroundWindow(true, hWindow);
    hWindow := GetChildWndHandle(hWindow, '_WwG');

    if AccessibleObjectFromWindow(hWindow, OBJID_NATIVEOM, IID_IDispatch, WordObject) = S_OK
    then
    begin
        Caption := GetActiveDocPath(WordObject);
        GetProperty(WordObject, 'ActiveDocument', WordObject);
        caption := GetActiveDocPath(WordObject);
        InterfaceConnect(WordObject, WordDocEventIID, FDispatcher, FConnection);
    end
end;

function TMainForm.GetWordHandle(AFileName, AClassName, AFlagText: Widestring)
  : NativeUInt;
var
    Handle: NativeUInt;
    sCaption: array [0 .. 1023] of char;
    sClassName: array [0 .. 254] of char;
begin
    Handle := FindWindowW(PWideChar(AClassName), nil);
    while Handle <> 0 do
    begin
        FillChar(sClassName, Sizeof(sClassName), #0);
        FillChar(sCaption, Sizeof(sCaption), #0);
        GetClassName(Handle, sClassName, Sizeof(sClassName));
        if sClassName = AClassName then
        begin
            GetWindowText(Handle, sCaption, Sizeof(sCaption));
            if (Pos(AFileName, sCaption) > 0) and (Pos(AFlagText, sCaption) > 0)
            then
            begin
                Result := Handle;
                Exit;
            end;
        end;
        Handle := GetWindow(Handle, GW_HWNDNEXT);
    end;
    Result := 0;
end;

function EnumWindowsProc(Wnd: DWORD; var EI: TEnumInfo): BOOL; stdcall;
var
    Buf: array [0 .. 127] of widechar;
begin
    GetClassNameW(Wnd, Buf, 128);
    if Pos(Buf, EI.ClassName) > 0 then
    begin
        EI.hWnd := Wnd;
        Result := FALSE;
        Exit;
    end;
    Result := true;
end;

function TMainForm.GetChildWndHandle(AParentHandle: THandle; AClassName: string): THandle;
var
    EI: TEnumInfo;
begin
    EI.hWnd := 0;
    EI.ClassName := AClassName;
    EnumChildWindows(AParentHandle, @EnumWindowsProc, Integer(@EI));
    Result := EI.hWnd;
end;

function GetProperty(dispobj: IDispatch; PropertyName: Widestring;
  var retvalue: IDispatch): Boolean;
var
    hr: HResult;
    DispId1: Integer;
    value: Variant;
    Params: TDISPPARAMS;
    typeInfo: ITypeInfo;
    FuncDesc: pFuncDesc;
begin
    Result := FALSE;
    dispobj.GetTypeInfoCount(DispId1);
    dispobj.GetTypeInfo(0, LOCALE_SYSTEM_DEFAULT, typeInfo);
    typeInfo.GetFuncDesc(0, FuncDesc);
    //typeInfo.GetNames()
    //ShowMessage(IntToStr(DispId1));
    hr := dispobj.GetIDsOfNames(GUID_Null, @(PropertyName), 1,
      LOCALE_SYSTEM_DEFAULT, @DispId1);
    if (hr >= 0) then
    begin
        hr := dispobj.Invoke(DispId1, GUID_Null, LOCALE_SYSTEM_DEFAULT,
          DISPATCH_PROPERTYGET, Params, @value, nil, nil);
        if (hr >= 0) then
        begin
            retvalue := value;
            Result := true;
        end;
    end;
end;


{% endhighlight %} 

另外一个封装的东西

{% highlight delphi %} 

unit uDispatchLib;

interface

uses
    ActiveX,
    sysutils,
    classes,
    Windows,
    oleacc;

type
    exMethodNotSupported = class(Exception);
    exIDispatchCallError = class(Exception);
function ExecuteOnDispatchMultiParam(TargetObj: IDispatch; MethodName: string;
    ParamValues: array of const): OleVariant;
procedure DocumentIDispatch(ID: IDispatch; var SL: TStringList);
procedure DocumentIDispatch2(ID: IDispatch; var SLNames: TStringList);
function ElementDescriptionToString(a: TElemDesc): string;
procedure DisplayInfo(const aAccessible : IAccessible; const aOffset : string; slInterfaceinfo: TStringList);

function AccessibleObjectFromWindow(AHWnd: hWnd; dwObjectID: DWORD;
    const riid: TGUID; out ppvObject): HResult; stdcall;
    external 'OLEACC.DLL' name 'AccessibleObjectFromWindow';

function AccessibleChildren(paccContainer: Pointer; iChildStart: LONGINT;
    cChildren: LONGINT; out rgvarChildren: OleVariant; out pcObtained: LONGINT)
    : HResult; stdcall; external 'OLEACC.DLL' name 'AccessibleChildren';

const
    OBJID_NATIVEOM = $FFFFFFF0;
    IID_IDispatch: TGUID = '{00020400-0000-0000-C000-000000000046}';

implementation
uses
    Variants;

function ElementDescriptionToString(a: TElemDesc): string;
begin
    case a.tdesc.vt of
        VT_I4:
            Result := 'int';
        VT_R8:
            Result := 'double';
        VT_BSTR:
            Result := 'string';
    else
        Result := '';
    end;
end;

procedure DocumentIDispatch(ID: IDispatch; var SL: TStringList);
var
    res: HResult;
    Count, loop, loop2, loop3: integer;
    TI: ITypeinfo;
    pTA: PTypeAttr;
    pFD: PFuncDesc;
    varDesc: pVarDesc;
    numFunctions: integer;
    numParams: integer;
    funcDispID: integer;
    names: TBStrList;
    numReturned: integer;
    functionstr: widestring;
    hide: boolean;
begin
    assert(SL <> nil, 'SL may not be nil');
    SL.Clear;
    res := ID.GetTypeInfoCount(Count);
    if succeeded(res) then begin
        for loop := 0 to Count - 1 do begin
            res := ID.GetTypeInfo(loop, 0, TI);
            if succeeded(res) then begin
                res := TI.GetTypeAttr(pTA);
                if succeeded(res) then begin
                    if pTA^.typekind = TKIND_DISPATCH then begin
                        numFunctions := pTA^.cFuncs;
                        for loop2 := 0 to numFunctions - 1 do begin
                            res := TI.GetFuncDesc(loop2, pFD);
                            if succeeded(res) then begin
                                funcDispID := pFD^.memid;
                                numParams := pFD^.cParams;
                                res := TI.GetNames(funcDispID, @names,
                                    numParams + 1, numReturned);
                                if succeeded(res) then begin
                                    functionstr := '';
                                    if numReturned > 0 then
                                        functionstr := functionstr + names[0];
                                    if numReturned > 1 then begin
                                        functionstr := functionstr + '(';
                                        for loop3 := 1 to numReturned - 1 do
                                        begin
                                        if loop3 > 1 then
                                        functionstr := functionstr + ', ';
                                        functionstr := functionstr +
                                        names[loop3] + ':' +
                                        ElementDescriptionToString
                                        (pFD^.lprgelemdescParam^[loop3 - 1]);
                                        end;

                                        // functionstr := functionstr + names[numReturned - 1] + ')';
                                        functionstr := functionstr + ')';
                                    end;
                                    hide := False;


                                    // Hides the non-dispatch functions

                                    if (pFD^.wFuncFlags and
                                        FUNCFLAG_FRESTRICTED) = FUNCFLAG_FRESTRICTED
                                    then
                                        hide := True;

                                    // Hides the functions not intended for scripting: basically redundant functions
                                    if (pFD^.wFuncFlags and FUNCFLAG_FHIDDEN) = FUNCFLAG_FHIDDEN
                                    then
                                        hide := True;
                                    if not hide then
                                        SL.add(functionstr);
                                end;
                                TI.ReleaseFuncDesc(pFD);
                            end;
                        end;
                    end;
                    TI.ReleaseTypeAttr(pTA);
                end;
            end;
        end;
    end
    else
        raise Exception.Create('GetTypeInfoCount Failed');
end;

procedure DocumentIDispatch2(ID: IDispatch; var SLNames: TStringList);
var
    res: HResult;
    Count, loop, loop2, loop3: integer;
    TI: ITypeinfo;
    pTA: PTypeAttr;
    pFD: PFuncDesc;
    varDesc: pVarDesc;
    numFunctions: integer;
    numParams: integer;
    funcDispID: integer;
    names: TBStrList;
    numReturned: integer;
    functionstr: widestring;
    hide: boolean;
begin
    SLNames.Clear;
    res := ID.GetTypeInfoCount(Count);
    if succeeded(res) then begin
        for loop := 0 to Count - 1 do begin
            res := ID.GetTypeInfo(loop, 0, TI);
            if succeeded(res) then begin
                res := TI.GetTypeAttr(pTA);
                if succeeded(res) then begin
                    if pTA^.typekind = TKIND_DISPATCH then begin

                        numFunctions := pTA^.cFuncs;
                        for loop2 := 0 to numFunctions - 1 do begin
                            res := TI.GetFuncDesc(loop2, pFD);
                            if not succeeded(res) then
                                Continue;

                            funcDispID := pFD^.memid;
                            numParams := pFD^.cParams;
                            res := TI.GetNames(funcDispID, @names,
                                numParams + 1, numReturned);
                            if not succeeded(res) then begin
                                TI.ReleaseFuncDesc(pFD);
                                Continue;
                            end;
                            // Hides the non-dispatch functions
                            if (pFD^.wFuncFlags and FUNCFLAG_FRESTRICTED) = FUNCFLAG_FRESTRICTED
                            then
                                Continue;

                            // Hides the functions not intended for scripting: basically redundant functions

                            if (pFD^.wFuncFlags and FUNCFLAG_FHIDDEN) = FUNCFLAG_FHIDDEN
                            then
                                Continue;
                            functionstr := '';
                            if numReturned > 0 then begin
                                functionstr := functionstr + names[0];

                            end;
                            functionstr := functionstr + '(';
                            if numReturned > 1 then begin
                                for loop3 := 1 to numReturned - 1 do begin

                                    if loop3 > 1 then
                                        functionstr := functionstr + ',';

                                    functionstr := functionstr +
                                        ElementDescriptionToString
                                        (pFD^.lprgelemdescParam^[loop3 - 1]);

                                end;
                            end;
                            SLNames.add(functionstr + ')');
                            TI.ReleaseFuncDesc(pFD);
                        end;
                    end;
                    TI.ReleaseTypeAttr(pTA);
                end;
            end;
        end;
    end
    else
        raise Exception.Create('GetTypeInfoCount Failed');

end;

{ ////////////////////////////////////////////////////////////////

  Name: ExecuteOnDispatchMultiParam

  Purpose:

  To execute arbitrary method on given COM object.

  Author: VJ

  Date: 07.07.2001

  History:

  //////////////////////////////////////////////////////////////// }
function ExecuteOnDispatchMultiParam(TargetObj: IDispatch; MethodName: string;
    ParamValues: array of const): OleVariant;
var
    wide: widestring;
    disps: TDispIDList;
    panswer: ^OleVariant;
    answer: OleVariant;
    dispParams: TDispParams;
    aexception: TExcepInfo;
    pVarArg: PVariantArgList;
    res: HResult;
    ParamCount, I: integer;
begin
    Result := False;

    // prepare for function call
    ParamCount := High(ParamValues) + 1;
    wide := MethodName;
    pVarArg := nil;
    if ParamCount > 0 then
        GetMem(pVarArg, ParamCount * sizeof(TVariantArg));

    try
        // get dispid of requested method
        if not succeeded(TargetObj.GetIDsOfNames(GUID_NULL, @wide, 1, 0, @disps))
        then
            raise exMethodNotSupported.Create
                ('This object does not support this method');
        panswer := @answer;

        // prepare parameters
        for I := 0 to ParamCount - 1 do begin
            case ParamValues[ParamCount - 1 - I].VType of
                vtInteger: begin
                        pVarArg^[I].vt := VT_I4;
                        pVarArg^[I].lVal :=
                            ParamValues[ParamCount - 1 - I].VInteger;

                    end;
                vtExtended: begin
                        pVarArg^[I].vt := VT_R8;
                        pVarArg^[I].dblVal := ParamValues[ParamCount - 1 - I]
                            .VExtended^;
                    end;
                vtString, vtAnsiString, vtChar: begin
                        pVarArg^[I].vt := VT_BSTR;
                        pVarArg^[I].bstrVal :=
                            PWideChar(widestring
                            (PChar(ParamValues[ParamCount - 1 - I].VString)));

                    end;
            else
                raise Exception.CreateFmt
                    ('Unsuported type for parameter with index %d', [I]);

            end;
        end;
        // prepare dispatch parameters
        dispParams.rgvarg := pVarArg;
        dispParams.rgdispidNamedArgs := nil;
        dispParams.cArgs := ParamCount;
        dispParams.cNamedArgs := 0;
        // make IDispatch call
        res := TargetObj.Invoke(disps[0], GUID_NULL, 0, DISPATCH_METHOD or
            DISPATCH_PROPERTYGET, dispParams, panswer, @aexception, nil);

        // check the result
        if res <> 0 then
            raise exIDispatchCallError.CreateFmt
                ('Method call unsuccessfull. %s (%s).',
                [string(aexception.bstrDescription),
                string(aexception.bstrSource)]);
        // return the result
        Result := answer;
    finally
        if ParamCount > 0 then
            FreeMem(pVarArg, ParamCount * sizeof(TVariantArg));

    end;
end;



procedure DisplayInfo(const aAccessible : IAccessible; const aOffset : string; slInterfaceinfo: TStringList);

  procedure ProcessChild(const aChild : OleVariant);
  var
    ChildAccessible : IAccessible;
    ChildDispatch : IDispatch;
  begin
    ChildDispatch := nil;
    case VarType(aChild) of
      varInteger : aAccessible.Get_accChild(aChild, ChildDispatch);
      varDispatch : ChildDispatch := aChild;
    end;
    if (ChildDispatch <> nil) and (ChildDispatch.QueryInterface(IAccessible, ChildAccessible) = S_OK) then
      DisplayInfo(ChildAccessible, aOffset + ' ', slInterfaceInfo)
  end;

var
  Child, CurrentChild : OleVariant;
  ChildArray : array of OleVariant;
  dwNum : DWord;
  Enum : IEnumVARIANT;
  i, iChildCount, iObtained : Integer;
  wsText : WideString;
begin
  if aAccessible <> nil then begin
      if aAccessible.get_AccName(CHILDID_SELF, wsText) = S_OK then
        slInterfaceInfo.Add(aOffset + 'Name: ' + wsText)
      else
        slInterfaceInfo.Add(aOffset + 'Name: Empty');
      if aAccessible.get_AccValue(CHILDID_SELF, wsText) = S_OK then
        slInterfaceInfo.Add(aOffset + ' Value: ' + wsText);
      if aAccessible.get_AccDescription(CHILDID_SELF, wsText) = S_OK then
        slInterfaceInfo.Add(aOffset + ' Description: ' + wsText);

      if (aAccessible.Get_accChildCount(iChildCount) = S_OK) and (iChildCount > 0) then begin
          slInterfaceInfo.Add(aOffset + ' Children: ' + IntToStr(iChildCount));
          SetLength(ChildArray, iChildCount);
          if AccessibleChildren(Pointer(aAccessible), 0, iChildCount, ChildArray[0], iObtained) = S_OK then begin
              for i := 0 to iObtained - 1 do
                ProcessChild(ChildArray[i])
            end else if aAccessible.QueryInterface(IEnumVARIANT, Enum) = S_OK then begin
              Enum := aAccessible as IEnumVARIANT;
              for i := 0 to iChildCount - 1 do
                if Enum.Next(1, Child, dwNum) = S_OK then
                  ProcessChild(Child);
            end else begin
              if aAccessible.accNavigate(NAVDIR_FIRSTCHILD, CHILDID_SELF, CurrentChild) = S_OK then begin
                  repeat
                    ProcessChild(CurrentChild)
                  until aAccessible.accNavigate(NAVDIR_NEXT, CurrentChild, CurrentChild) <> S_OK;
                end
            end
        end
    end
end;

end.

{% endhighlight %} 