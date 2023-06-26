#include <stdio.h>
#include <unistd.h>

int gval=10;
int main(int argc, char *argv[])
{
	pid_t pid=fork();

	if(pid==0) // 자식 프로세스
	{
		puts("안녕 나는 자식 프로세스 응에");
	}		
	else // 부모 프로세스
	{
		printf("Child Process ID: %d \n", pid);
		sleep(30); // sleep 30 sec.
	}
	  
	if(pid==0)
		puts("End Child Process");
	else
		puts("End Parent Process");
	return 0;
}
