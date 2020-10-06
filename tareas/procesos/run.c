#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char *argv[])
{
    if (argc <= 1) {
        printf("%s need that you enter an unix command\n", argv[0]);
        exit(1);
    }

    printf("Executing: ");
    char* myargs[argc];
    for (int i = 1; i < argc; i++) {
        myargs[i-1] = argv[i];
        printf("%s ", argv[i]);
    }
    myargs[argc-1] = NULL;
    printf("\nResult:\n");
    execvp(myargs[0], myargs);
    perror("Return from execvp() not expected");
    exit(EXIT_FAILURE);
    return 0;
}