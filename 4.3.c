#include <stdio.h>
int main(){
	int a, b;
	scanf("%d %d", &a, &b);
	if(b == 0 || a % b !=0) {
		printf("NO\n");
	}else {
		printf("YES\n"); 
	}	
	return 0;
}
