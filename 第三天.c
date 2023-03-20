#include <stdio.h>
int main(){
	int a;
	int b;
	while(1){
	    scanf("%d %d",&a,&b);
	    a = a ^ b;
	    b = a ^ b;
	    a = a ^ b;
	printf("%d %d\n",a,b);
	}	
	return 0;
}
