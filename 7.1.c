#include <stdio.h>
int f(int n) {
	if(n <= 1) {
		return 1;
	}
	return n * f(n-1);
}
int main() {
	int n;
	while(scanf("%d", &n) != EOF) {
		printf("%d\n", f(n));
	}
	return 0;
}
