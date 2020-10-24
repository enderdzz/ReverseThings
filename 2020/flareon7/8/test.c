#include <sys/auxv.h>

int main(){
    int *v22 = getauxval(33);
    printf("%d\n", *(v22+56)); // 4
    printf("%016x\n", *(v22 + *(v22+32) + 16)); // 4
    
    return 0;
}
