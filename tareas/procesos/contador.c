#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int contador = 1;

int main(int argc, char *argv[]) {
    printf("hello world (pid:%d)\n", (int) getpid());
    int rc = fork();
    if (rc < 0) {
        // fork failed; exit
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {
        // child (new process)
        contador += 5;
        printf("hello, I am child (contador:%d)(pid:%d)\n",
            contador, (int) getpid());
        
    } else {
        // parent goes down this path (original process)
        contador += 2;
        printf("hello, I am parent of %d (contador:%d)(pid:%d)\n",
	       rc, contador, (int) getpid());
    }
    return 0;
}

/*
Que puede decir de dicho comporatamiento?

R: Que el proceso nuevo aunque comparte las mismas instrucciónes no comparten
   las mismas variables, esto es debido a que el fork crea una copia.
*/