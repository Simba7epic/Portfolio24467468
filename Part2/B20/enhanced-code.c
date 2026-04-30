#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 80

int main() {
    char buf[BUFFER_SIZE];

    printf("Enter input: ");

    if (fgets(buf, BUFFER_SIZE, stdin) == NULL) {
        printf("Input error occurred\n");
        return 1;
    }

    // remove newline safely
    buf[strcspn(buf, "\n")] = 0;

    // validate input
    if (strlen(buf) == 0) {
        printf("Invalid input: empty string\n");
        return 1;
    }

    printf("Securely processed input: %s\n", buf);

    return 0;
}
