#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

long fibo(int n) {
    if (n == 0 || n == 1)
        return n;

    long prev = 0;
    long current = 1;

    for (int i = 2; i <= n; i++) {
        long temp = current;
        current = prev + current;
        prev = temp;
    }

    return current;
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
        printf("bay, I am child (fibo(50):%ld) (pid:%d)\n",
            fibo(50), (int) getpid());
        sleep(1);
    } else {
        // parent goes down this path (original process)
        printf("hello, I am parent of %d (pid:%d)\n",
           rc, (int) getpid());
        int wc = 0;
        // int wc = wait(NULL);
        printf("bay, I am parent of %d (wc:%d) (fibo(50):%ld) (pid:%d)\n",
           rc, wc, fibo(50), (int) getpid());
    }
    return 0;
}

/*
Sin el wait el hijo si termina la ejecución, pero el padre lo termina antes.
Con el wait el padre espera al hijo para terminar.
*/