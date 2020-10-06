#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
#include <time.h>

int maxrand(int max) {
    srand(time(0));
    return rand()%max;
}

int main(int argc, char *argv[]) {
    printf("hello world (pid:%d)\n", (int) getpid());
    int rc = fork();
    if (rc < 0) {
        // fork failed; exit
        fprintf(stderr, "fork failed\n");
        exit(1);
    } else if (rc == 0) {
        // child (new process)
        printf("hello, I am child (pid:%d)\n", (int) getpid());
        int exit_val = maxrand(255);
        // int exit_val = 256;
        // int s = 4 / (exit_val - exit_val);
        printf("bay, I am child (exit value:%d) (pid:%d)\n",
            exit_val, (int) getpid());
	    sleep(1);
        exit(exit_val);
    } else {
        // parent goes down this path (original process)
        int status;
        printf("hello, I am parent of %d (pid:%d)\n",
	       rc, (int) getpid());
        int wc = wait(&status);
        if (WIFEXITED(status)) {
            printf("bay, I am parent of %d (wc:%d) (child_status:%d) (pid:%d)\n",
	            rc, wc, WEXITSTATUS(status), (int) getpid());
        }
        else {
            printf("bay, I am parent of %d (wc:%d) (child_status:not_exit) (pid:%d)\n",
	            rc, wc, (int) getpid());
        }
    }
    return 0;
}

/*
El valor maximo debe ser 255
*/