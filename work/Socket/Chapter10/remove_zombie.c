#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/wait.h>

void read_childproc(int sig)
{
	int status;
	pid_t id=waitpid(-1, &status, WNOHANG);
	if(WIFEXITED(status))
	{
		printf("Removed proc od: %d \n", id);
		printf("Child send: %d \n", WEXITSTATUS(status));
	}
}

int main(int argc, char *argv[])
{
	pid_t pid;
	struct sigaction act;
	act.sa_handler=read_childproc;
	sigemptyset(&act.sa_mask);
	act.sa_flags=0;
	sigaction(SIGCHLD, &act, 0);
	
	pid=fork();
	if(pid==0) // 자식 프로세스
	{
		puts("안녕 나는 자식 프로세스 응에");
		sleep(10);
		return 12;
	}		
	else // 부모 프로세스
	{
		printf("Child Process ID: %d \n", pid);
		pid=fork();
		if(pid==0)  // 다른 자식 프로세스
		{
			puts("안녕 나는 또 다른 자식 프로세스");
			sleep(10);
			exit(24);
		}
		else
		{
			int i;
			printf("Child Proc ID: %d \n", pid);
			for(i=0; i<5; i++)
			{
				puts("wait...");
				sleep(5);
			}
		}
	}
	return 0;	
}
