//#include <stdio.h>
//#include <unistd.h> 
#include <dlfcn.h> // for dlopen() dlsym()
#include <sys/user.h> // for struct user_regs_struct
//#include <sys/stat.h> // for chmod() mode_t data type 
#include <sys/utsname.h> // for uname() struct utsname

#define NULL 0

typedef long(*my_ptrace)(int, int, void*, void*);
typedef int(*my_setvbuf)(void*, char*, int, int);
typedef int(*my_waitpid)(int, int*, int);
typedef int(*my_strlen)(char*);
typedef int(*my_execve)(char*, char*, char*);
typedef int(*my_memcmp)(char*, char*, int);
typedef int(*my_pivot_root)(char*, char*);
typedef int(*my_chmod)(char*, long);
typedef int(*my_uname)(struct utsname*);

// https://man7.org/linux/man-pages/man2/ptrace.2.html
long setvbuf(int request, int pid, void *addr, void *data) {
    // my own code
    // write(1, "hooked.", 7); 
    // write(fd, &foo, sizeof foo);
    printf("ptrace_req: %d,\tpid: %d,\taddr: %08x,\tdata: %08x\n", request, pid, (int)addr, (int)data);

    static void *handle = NULL;
    static my_ptrace o_ptrace = NULL;
    static my_setvbuf o_setvbuf = NULL;
    handle = dlopen("libc.so.6", RTLD_LAZY);
    o_ptrace = (my_ptrace)dlsym(handle, "ptrace");
    o_setvbuf = (my_setvbuf)dlsym(handle, "setvbuf");
    if ( (int)pid == 0 && (int)addr == 2 && (int)data == 0 ) {
        return o_setvbuf((void*)request, (char*)pid, (int)addr, (int)data); 
    }
    
    long ret = o_ptrace(request, pid, addr, data);
    
    struct user_regs_struct *tmp = (struct user_regs_struct *)data;
    // something can be obtained AFTER the ptrace call.
    if ( request == 12) {
        printf("ORIG_EAX: %08x\n", (int)(tmp->orig_eax));
        // printf("EIP: %08x\n", (int)( *(int *)((char *)data+0x30) ) );
        printf("EIP: %08x\n", (int)(tmp->eip));
        printf("EAX: %08x\n", (int)(tmp->eax));
        printf("ECX: %08x\n", (int)(tmp->ecx));
        printf("EDX: %08x\n", (int)(tmp->edx));
        printf("ESP: %08x\n", (int)(tmp->esp));
        // char cmd[100] = {};
        // sprintf(cmd, "%s%d%s", "cat /proc/", pid, "/maps");
        // puts(cmd);
        // system(cmd);
    } else if ( request == 2) {
        printf("DAT: %08x\n", (int)ret);
    }
    
    return ret;
}

void view_mem(char *mem, int len) {
    for (int i = 0; i < len; i++){
        printf("%02x", *(char *)(mem+i));
    }
    puts("");
}

// int strlen(char *buf) {
//     static void *handle = NULL;
//     static my_strlen o_strlen = NULL;
//     handle = dlopen("libc.so.6", RTLD_LAZY);
//     o_strlen = (my_strlen)dlsym(handle, "strlen");

//     int res =  o_strlen(buf);
//     //view_mem(buf, res);
//     //printf("Strlen: %d\n", res);
//     return res;
// }

// int execve(char *path, char *argv, char *envp) {
//     static void *handle = NULL;
//     static my_execve o_execve = NULL;
//     handle = dlopen("libc.so.6", RTLD_LAZY);
//     o_execve = (my_execve)dlsym(handle, "execve");
//     int res =  o_execve(path, argv, envp);
//     printf("==================================OOOOOOOOOOOOOOOOOOOONo!\n");
//     printf("EXECVE: %s %s %s\n", path, argv, envp);
//     return res;
// }

int waitpid(int pid, int *stat, int options) {
    printf("waitpid: %d, Oops: %d", pid, ((*stat)&0x7f)==0);
    if( ((*stat)&0xff) == 127 ) {
        printf(", stat: %d\n", ((*stat)&0xff00)>>8);
    } else { printf("\n"); }
    
    static void *handle = NULL;
    static my_waitpid o_waitpid = NULL;
    static int ret = 0;
    handle = dlopen("libc.so.6", RTLD_LAZY);
    o_waitpid = (my_waitpid)dlsym(handle, "waitpid");
    ret = o_waitpid(pid, stat, options);
    printf("waitpid_ret: %d\n", ret);
    return ret;
}

// int memcmp(char *s1, char *s2, int n) {

//     if (n == 0x10 && s2 == 0x81A50EC) {
//         printf("MEMCMP: %s\n", s2);
//     }
    
//     static void *handle = NULL;
//     static my_memcmp o_memcmp = NULL;
//     handle = dlopen("libc.so.6", RTLD_LAZY);
//     o_memcmp = (my_memcmp)dlsym(handle, "memcmp");
//     int res =  o_memcmp(s1, s2, n);
    
//     return res;
// }

/* NOTE: have problems with following three functions hook,
    pivot_root, chmod, uname.
 */

// int pivot_root(char* s1, char* s2) {
    
//     print("PIVOT: %08x %08x\n", *(int *)s1, *(int *)s2);

//     static void *handle = NULL;
//     static my_pivot_root o_pivot_root = NULL;
//     handle = dlopen("libc.so.6", RTLD_LAZY);
//     o_pivot_root = (my_pivot_root)dlsym(handle, "pivot_root");
//     int res =  o_pivot_root(s1, s2);
//     return res;
// }

// int chmod(char* path, long m) {

//     print("CHMOD: %08x\n", m);

//     static void *handle = NULL;
//     static my_chmod o_chmod = NULL;
//     handle = dlopen("libc.so.6", RTLD_LAZY);
//     o_chmod = (my_chmod)dlsym(handle, "chmod");
//     int res =  o_chmod(path, m);
//     return res;
// }

// int uname(struct utsname* buf) {

//     print("UNAME: %016x\n", *(char *)buf);

//     static void *handle = NULL;
//     static my_uname o_uname = NULL;
//     handle = dlopen("libc.so.6", RTLD_LAZY);
//     o_uname = (my_uname)dlsym(handle, "uname");
//     int res =  o_uname(buf);
//     return res;
// }