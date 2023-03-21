#include <stdio.h>
int main(){
	int buxiaoxin, guyibuxiaoxin, buxiaoxinguyi;
	scanf("%d %d %d", &buxiaoxin, &guyibuxiaoxin,&buxiaoxinguyi);
	if(buxiaoxin){
		printf("不小心\n");
	}else if(guyibuxiaoxin){
		printf("故意不小心\n");
	}else if(buxiaoxinguyi){
		printf("不小心故意的\n");
	}else{
		printf("是故意的\n"); 
	}	
	return 0;
}
