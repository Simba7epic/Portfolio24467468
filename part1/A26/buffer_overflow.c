// file: buffer_overflow.c
#include <stdio.h>
#include <string.h>

int main() {
    char buf[8];
    printf("Enter a string: ");
    scanf("%s", buf); // Unsafe: no bounds checking
    printf("You entered: %s\n", buf);
    return 0;
}