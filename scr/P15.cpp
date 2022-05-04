#include <cstdio>

const int N=17;
int counter[1] = {0};

void move(int x, int y) {
	if (x < N) { move(x+1, y ); }
	if (y < N) { move(x  , y+1); }
	if (x==N && y==N) { counter[0]++; }
}

int main()
{ 	
	move(0, 0);
	printf("%i \n", counter[0]);
	return 0;
}