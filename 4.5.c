#include <stdio.h>
int main(){
	int a, b;
	scanf("%d %d", &a, &b);
    printf("%s\n", (b == 0 || a % b != 0) ? "NO" : "YES");
	return 0;
}
