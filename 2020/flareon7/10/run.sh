export LD_PRELOAD=""; gcc -fPIC hook.c -m32 -shared -o test.so
export LD_PRELOAD=./test.so; ./break
