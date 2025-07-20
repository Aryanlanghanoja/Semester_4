#include <stdio.h>

int main() {
    int num = 0; 

    for (num = 0; num <= 255; num++) {
        printf("Hexadecimal value of %d is 0x%x\n", num, num);
    }
        return 0;
}
