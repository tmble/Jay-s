#include <stdio.h>
int main(){
	int buxiaoxin, guyibuxiaoxin, buxiaoxinguyi;
	scanf("%d %d %d", &buxiaoxin, &guyibuxiaoxin,&buxiaoxinguyi);
	if(buxiaoxin){
		printf("��С��\n");
	}else if(guyibuxiaoxin){
		printf("���ⲻС��\n");
	}else if(buxiaoxinguyi){
		printf("��С�Ĺ����\n");
	}else{
		printf("�ǹ����\n"); 
	}	
	return 0;
}
