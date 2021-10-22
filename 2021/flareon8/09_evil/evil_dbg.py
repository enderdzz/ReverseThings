import time

def veh_handle():
    
    ida_dbg.add_bpt(ida_nalt.get_imagebase()+0x6b9b, 1, ida_idd.BPT_DEFAULT)
    ida_dbg.start_process()
    ida_dbg.wait_for_next_event(ida_dbg.WFNE_SUSP, -1)

    while True:
        # bp reached
        
        ida_dbg.wait_for_next_event(ida_dbg.WFNE_SUSP, -1)
        
        lib_addr = ida_dbg.get_reg_val("EDI")
        ept_addr = ida_dbg.get_reg_val("EAX")
        print(hex(lib_addr))
        call_eax_addr = ept_addr + 3
        ida_dbg.add_bpt(call_eax_addr, 1, ida_idd.BPT_DEFAULT)
        api_name = ida_name.get_ea_name(lib_addr)
        
        idc.set_cmt(call_eax_addr, api_name, 1)
        ida_bytes.patch_byte(ept_addr+2, 0x90)
        
        if api_name == "kernel32_ExitProcess":
            break
        
        ida_dbg.continue_process()
        ida_dbg.wait_for_next_event(ida_dbg.WFNE_SUSP, -1)
        ida_dbg.continue_process()
        #time.sleep(1)

def api_resolve():
    
    for ea in XrefsTo(ida_nalt.get_imagebase()+0x54B0):
        bp = next_head(ea.frm)
        ida_dbg.add_bpt(bp, 1, ida_idd.BPT_DEFAULT)
    
    ida_dbg.start_process()
    
    while True:
        ida_dbg.wait_for_next_event(ida_dbg.WFNE_SUSP, -1)
        
        lib_addr = ida_dbg.get_reg_val("EAX")
        api_name = ida_name.get_ea_name(lib_addr)
        prev = idc.get_cmt(idc.get_screen_ea(), 1)
        if prev == None:
            idc.set_cmt(idc.get_screen_ea(), api_name, 1)
        elif api_name not in prev:
            idc.set_cmt(idc.get_screen_ea(), prev+', '+api_name, 1)
        
        ida_dbg.continue_process()
    
api_resolve()