from struct import pack

def expt_patch():

    expt_pattern = [
        "33 c0 8b 00", # xor eax, eax; mov eax, [eax];
        "33 ff f7 f7", # xor edi, edi; div edi;
        "33 c0 f7 f0", # xor eax, eax; div eax;
        "33 f6 f7 f6", # xor esi, esi; div esi;
    ]

    end_ea = idc.get_segm_end(0)

    for i in expt_pattern:
        ea = ida_search.find_binary(0, end_ea, i, 16, idc.SEARCH_DOWN)
        while ea != ida_idaapi.BADADDR:
            print(hex(ea))
            offset = (0x4054b0 - (ea + 5) + 0x100000000) & 0xffffffff
            pb = b'\xe8'+pack("<I", offset)+b'\xff\xd0'
            ida_bytes.patch_bytes(ea, pb)
            
            ea = ida_search.find_binary(ea+4, end_ea, i, 16, idc.SEARCH_DOWN)

def edx_ecx_patch():
    ea = ida_search.find_text(0, 0, 0, 'call    resolve_api_4054B0', ida_search.SEARCH_CASE|ida_search.SEARCH_DOWN)
    cnt = 0
    while ea != ida_idaapi.BADADDR:
        if GetDisasm(next_head(ea)) == "call    eax":
            if ida_bytes.get_byte(ea-6) != 0x8b:
                continue
            if ida_bytes.get_byte(ea-3) != 0x8b:
                continue
            cnt += 1
            print(cnt)
            # r1 = ida_bytes.get_byte(ea-5)
            # r2 = ida_bytes.get_byte(ea-2)
            # ida_bytes.patch_byte(ea-2, r1)
            # ida_bytes.patch_byte(ea-5, r2)
            
        ea = ida_search.find_text(ea+5, 0, 0, 'call    resolve_api_4054B0', ida_search.SEARCH_CASE|ida_search.SEARCH_DOWN)

resolve_api_arglist = []

class my_super_visitor(idaapi.ctree_visitor_t):
    def __init__(self, ea):
        idaapi.ctree_visitor_t.__init__(self, idaapi.CV_FAST) # CV_FAST does not keep parents nodes in CTREE
        self.addr = ea
        
    def visit_insn(self, i):
        return 0
    '''
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__swig_destroy__', '__weakref__', '_acquire_ownership', '_citem_t__dbg_get_meminfo', '_citem_t__dbg_get_registered_kind', '_deregister', '_ensure_cond', '_ensure_no_obj', '_ensure_no_op', '_get_a', '_get_fpc', '_get_helper', '_get_insn', '_get_m', '_get_n', '_get_obj_ea', '_get_op', '_get_ptrsize', '_get_refwidth', '_get_string', '_get_x', '_get_y', '_get_z', '_maybe_disown_and_deregister', '_meminfo', '_obj_id', '_own_and_register', '_register', '_replace_by', '_set_a', '_set_fpc', '_set_helper', '_set_insn', '_set_m', '_set_n', '_set_obj_ea', '_set_op', '_set_ptrsize', '_set_refwidth', '_set_string', '_set_x', '_set_y', '_set_z', 'a', 'assign', 'calc_type', 'cexpr', 'cinsn', 'cleanup', 'compare', 'contains_comma', 'contains_comma_or_insn_or_label', 'contains_expr', 'contains_insn', 'contains_insn_or_label', 'contains_label', 'contains_operator', 'cpadone', 'ea', 'equal_effect', 'exflags', 'find_closest_addr', 'find_num_op', 'find_op', 'find_parent_of', 'fpc', 'get_1num_op', 'get_const_value', 'get_high_nbit_bound', 'get_low_nbit_bound', 'get_ptr_or_array', 'get_type_sign', 'get_v', 'has_side_effects', 'helper', 'index', 'insn', 'is_call_arg_of', 'is_call_object_of', 'is_child_of', 'is_const_value', 'is_cstr', 'is_expr', 'is_fpop', 'is_jumpout', 'is_negative_const', 'is_nice_cond', 'is_nice_expr', 'is_non_negative_const', 'is_non_zero_const', 'is_odd_lvalue', 'is_type_signed', 'is_type_unsigned', 'is_undef_val', 'is_vftable', 'is_zero_const', 'label_num', 'm', 'maybe_ptr', 'meminfo', 'n', 'numval', 'obj_ea', 'obj_id', 'op', 'op_to_typename', 'operands', 'opname', 'print1', 'ptrsize', 'put_number', 'refwidth', 'replace_by', 'requires_lvalue', 'set_cpadone', 'set_v', 'set_vftable', 'string', 'swap', 'theother', 'this', 'thisown', 'to_specific_type', 'type', 'v', 'x', 'y', 'z']
    
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__swig_destroy__', '__weakref__', '_acquire_ownership', '_citem_t__dbg_get_meminfo', '_citem_t__dbg_get_registered_kind', '_deregister', '_ensure_cond', '_ensure_no_obj', '_ensure_no_op', '_get_casm', '_get_cblock', '_get_cdo', '_get_cexpr', '_get_cfor', '_get_cgoto', '_get_cif', '_get_creturn', '_get_cswitch', '_get_cwhile', '_get_op', '_maybe_disown_and_deregister', '_meminfo', '_obj_id', '_own_and_register', '_print', '_register', '_replace_by', '_set_casm', '_set_cblock', '_set_cdo', '_set_cexpr', '_set_cfor', '_set_cgoto', '_set_cif', '_set_creturn', '_set_cswitch', '_set_cwhile', '_set_op', 'assign', 'casm', 'cblock', 'cdo', 'cexpr', 'cfor', 'cgoto', 'cif', 'cinsn', 'cleanup', 'collect_free_breaks', 'collect_free_continues', 'compare', 'contains_expr', 'contains_free_break', 'contains_free_continue', 'contains_insn', 'contains_label', 'create_if', 'creturn', 'cswitch', 'cwhile', 'details', 'ea', 'find_closest_addr', 'find_parent_of', 'index', 'insn_is_epilog', 'is_epilog', 'is_expr', 'is_ordinary_flow', 'label_num', 'meminfo', 'new_insn', 'obj_id', 'op', 'op_to_typename', 'opname', 'print1', 'replace_by', 'swap', 'this', 'thisown', 'to_specific_type', 'zero']
    '''
    def visit_expr(self, e):
        
        if e.op == idaapi.cot_call and e.ea == self.addr: # print(e.x.obj_ea) -> 0xcb54b0
            args = []
            for i in e.a:
                if i.op == idaapi.cot_num:
                    args.append(int(i.numval()))
                elif i.op == idaapi.cot_var: # TODO: find the var value.
                    return 0
                elif i.op == idaapi.cot_cast: # TODO: modify the ctree prop.
                    return 0
            #print(hex(e.ea), args)
            resolve_api_arglist.append((e.ea, args[0]&((1<<32)-1), args[1]&((1<<32)-1)))
        return 0
          
# https://github.com/likescam/APT_REPORT/blob/e4b91e3e42b3ce9ac6454583f2e057f3fb96df31/Oceanlotus/OL_OSX_decryptor.py
def mk_resolve_api_cmt():
    ea = ida_search.find_text(0, 0, 0, 'call    resolve_api_4054B0', ida_search.SEARCH_CASE|ida_search.SEARCH_DOWN)
    cnt = 0
    while ea != ida_idaapi.BADADDR:
        
        if ida_nalt.get_imagebase()+0x2FA9 != ea: # TODO: cannot decompile at this addr
            cfunc = idaapi.decompile(ea)
            v = my_super_visitor(ea)
            v.apply_to(cfunc.body, None)

        ea = ida_search.find_text(ea+5, 0, 0, 'call    resolve_api_4054B0', ida_search.SEARCH_CASE|ida_search.SEARCH_DOWN)
    
    #ida_dbg.start_process()
    
    need_to_modify = []
    for addr, arg1, arg2 in resolve_api_arglist:
        ida_dbg.wait_for_next_event(ida_dbg.WFNE_SUSP, -1)
        resolve_api_4054B0    = ida_idd.Appcall.typedobj("int __fastcall resolve_api_4054B0(int a1, int a2);")
        resolve_api_4054B0.ea = ida_name.get_name_ea(0, "resolve_api_4054B0")
        ret = resolve_api_4054B0(arg1, arg2)
        if ret == 0:
            ret = resolve_api_4054B0(arg2, arg1) # very tricky.
            print("ender:", api_name, hex(addr), arg1, arg2)
            if ida_bytes.get_byte(addr-6) != 0x8b:
                print("wrong1", hex(addr))
            elif ida_bytes.get_byte(addr-3) != 0x8b:
                print("wrong2", hex(addr))
            else:
                print("handling...")
                need_to_modify.append(addr)
                r1 = ida_bytes.get_byte(addr-5)
                r2 = ida_bytes.get_byte(addr-2)
                ida_bytes.patch_byte(addr-2, r1)
                ida_bytes.patch_byte(addr-5, r2)
        else:
            api_name = ida_name.get_ea_name(ret)
            print("ender:", api_name, hex(addr), arg1, arg2)
        #idc.set_cmt(addr, "ender: " + api_name, 1)
    print(need_to_modify)
    
print("*"*80)
mk_resolve_api_cmt()
'''
8B 55 F0                       mov     edx, [ebp+var_10]
8B 4D E8                       mov     ecx, [ebp+var_18]
E8 4D 30 00 00                 call    resolve_api_4054B0
FF D0                          call    eax

to 

8B 4D F0                       mov     ecx, [ebp+var_10]
8B 55 E8                       mov     edx, [ebp+var_18]
'''