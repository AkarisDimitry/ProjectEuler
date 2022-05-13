#include <cstdio>
#include <bits/stdc++.h>
#include <omp.h>
using namespace std;

const int N=17;

void Triangle  (int n, int *T)   { T[0] = n*(n+1)/2; }
void Square    (int n, int *T)   { T[0] = n*n; }
void Pentagonal(int n, int *T)   { T[0] = n*(3*n-1)/2; }
void Hexagonal (int n, int *T)   { T[0] = n*(2*n-1); }
void Heptagonal(int n, int *T)   { T[0] = n*(5*n-3)/2; }
void Octagonal (int n, int *T)   { T[0] = n*(3*n-2); }

int P3[100] = {0};	int n3=0;
int P4[100] = {0};	int n4=0;
int P5[100] = {0};	int n5=0;
int P6[100] = {0};	int n6=0;
int P7[100] = {0};	int n7=0;
int P8[100] = {0};	int n8=0;

void exploration(	int p3, int p4, int p5, int p6, int p7, int p8,
						int U3, int U4, int U5, int U6, int U7, int U8,
						int D, int last) {

		if (U3==1 && U4==1 && U5==1 && U6==1 && U7==1 && U8==1 && int(p8/100) == last%100) {
			printf("%i %i %i %i %i %i  %i\n", p3, p4, p5, p6, p7, p8,  p3+p4+p5+p6+p7+p8);
		}
		// Pn -> P3
		if (U3 == 0) {
			#pragma omp parallel for num_threads(12)
			for (int i3=0; i3<n3; i3++) {
				if ( D == int(P3[i3]/100) ) {
					exploration( P3[i3], p4, p5, p6, p7, p8,
						1, U4, U5, U6, U7, U8,
						P3[i3]%100, P3[i3]);
		}	}	}

		// Pn -> P4
		if (U4 == 0) {
			#pragma omp parallel for num_threads(12)
			for (int i4=0; i4<n4; i4++) {
				if ( D == int(P4[i4]/100) ) {
					exploration( p3, P4[i4], p5, p6, p7, p8,
						U3, 1, U5, U6, U7, U8,
						P4[i4]%100, P4[i4]);
		}	}	}

		// Pn -> P5
		if (U5 == 0) {
			#pragma omp parallel for num_threads(12)
			for (int i5=0; i5<n5; i5++) {
				if ( D == int(P5[i5]/100) ) {
					exploration( p3, p4, P5[i5], p6, p7, p8,
						U3, U4, 1, U6, U7, U8,
						P5[i5]%100, P5[i5]);
		}	}	}

		// Pn -> P4
		if (U6 == 0) {
			#pragma omp parallel for num_threads(12)
			for (int i6=0; i6<n6; i6++) {
				if ( D == int(P6[i6]/100) ) {
					exploration( p3, p4, p5, P6[i6], p7, p8,
						U3, U4, U5, 1, U7, U8,
						P6[i6]%100, P6[i6]);
		}	}	}

		// Pn -> P4
		if (U7 == 0) {
			#pragma omp parallel for num_threads(12)
			for (int i7=0; i7<n7; i7++) {
				if ( D == int(P7[i7]/100) ) {
					exploration( p3, p4, p5, p6, P7[i7], p8,
						U3, U4, U5, U6, 1, U8,
						P7[i7]%100, P7[i7]);
		}	}	}

		// Pn -> P8
		if (U8 == 0) {
			#pragma omp parallel for num_threads(12)
			for (int i8=0; i8<n8; i8++) {
				if ( D == int(P8[i8]/100) ) {
					exploration( p3, p4, p5, p6, p7, P8[i8],
						U3, U4, U5, U6, U7, 1,
						P8[i8]%100, P8[i8]);
		}	}	}

}

int main() {
	clock_t start, end;

	start = clock();
	// Store Pn numbers 
	int num = 0;
	for (int n=0; n<500; n++) {
		Triangle(n, &P3[num]);
		if (P3[num]>999) {
			if (P3[num]<9999) {	
				num += 1;
				n3 += 1;
			}	else { break; }
	}	}

	num = 0;
	for (int n=0; n<500; n++) {
		Square(n, &P4[num]);
		if (P4[num]>999) {
			if (P4[num]<9999) {	
				num += 1;
				n4 += 1;
			}	else { break; }
	}	}

	num = 0;
	for (int n=0; n<500; n++) {
		Pentagonal(n, &P5[num]);
		if (P5[num]>999) {
			if (P5[num]<9999) {	
				num += 1;
				n5 += 1;
			}	else { break; }
	}	}

	num = 0;
	for (int n=0; n<500; n++) {
		Hexagonal(n, &P6[num]);
		if (P6[num]>999) {
			if (P6[num]<9999) {	
				num += 1;
				n6 += 1;
			}	else { break; }
	}	}

	num = 0;
	for (int n=0; n<500; n++) {
		Heptagonal(n, &P7[num]);
		if (P7[num]>999) {
			if (P7[num]<9999) {	
				num += 1;
				n7 += 1;
			}	else { break; }
	}	}

	num = 0;
	for (int n=0; n<500; n++) {
		Octagonal(n, &P8[num]);
		if (P8[num]>999) {
			if (P8[num]<9999) {	
				num += 1;
				n8 += 1;
			}	else { break; }
	}	}

	printf("P3:%i  P4:%i  P5:%i  P6:%i  P7:%i  P8:%i \n", n3, n4, n5, n6, n7, n8);

	// P8
	#pragma omp parallel for num_threads(12)
	for (int i8=0; i8<n8; i8++) {
		exploration(	0, 0, 0, 0, 0, P8[i8],
						0, 0, 0, 0, 0, 1,
						P8[i8]%100, P8[i8]);
	}

	end = clock();
    // Calculating total time taken by the program.
    double time_taken = double(end - start) / double(CLOCKS_PER_SEC);
    cout << "Time taken by program is : " << fixed 
         << time_taken << setprecision(5);
    cout << " sec " << endl;
	return 0;
}