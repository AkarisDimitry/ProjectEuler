#include <cstdio>
#include <bits/stdc++.h>
#include <omp.h>
#include <iostream>
// g++ P68.cpp

using namespace std;

int concat(int a, int b){
    // Convert both the integers to string
    string s1 = to_string(a);
    string s2 = to_string(b);
 
    // Concatenate both strings
    string s = s1 + s2;

    // Convert the concatenated string
    // to integer
    int c = stoi(s);

    // return the formed integer
    return c;
}


void sum_0(int *num, int *suma) {suma[0] = num[0] + num[10] + num[12];}
void sum_1(int *num, int *suma) {suma[2] = num[2] + num[12] + num[14];}
void sum_2(int *num, int *suma) {suma[4] = num[4] + num[14] + num[16];}
void sum_3(int *num, int *suma) {suma[6] = num[6] + num[16] + num[18];}
void sum_4(int *num, int *suma) {suma[8] = num[8] + num[18] + num[10];}

bool valid_solution(int s0, int s1, int s2, int s3, int s4){
	if (s0 == s1 && s0 == s2 && s0 == s3 && s0 == s4) {	return 1;
	}	else { return 0; }
}

void sumas(int **num, int **suma) {
	sum_0(num[0], suma[0]);
	sum_1(num[0], suma[0]);
	sum_2(num[0], suma[0]);
	sum_3(num[0], suma[0]);
	sum_4(num[0], suma[0]);
}

void concatenate_solution(int *cocant, int *num) {
	concat(num[0],concat(num[5], num[6]));
	concat(num[1],concat(num[6], num[7]));
	concat(num[2],concat(num[7], num[8]));
	concat(num[3],concat(num[8], num[9]));
	concat(num[4],concat(num[9], num[5]));
}

void exploration(int d0, int d1, int d2, int d3, int d4, 
								int d5, int d6, int d7, int d8, int d9,

								int n0, int n1, int n2, int n3, int n4, 
								int n5, int n6, int n7, int n8, int n9,

								int s0, int s1, int s2, int s3, int s4,
								int index   ) {
	int *Nm[10] = { &n0, &n1, &n2, &n3, &n4,
									&n5, &n6, &n7, &n8, &n9,  };

	int *Dm[10] = { &d0, &d1, &d2, &d3, &d4,
								  &d5, &d6, &d7, &d8, &d9,  }; 

	if (index < 10) {

		for (int dn=0; dn<10; dn++) {	

			if (Dm[dn][0] == 0) {
					Dm[dn][0] = 1;
					Nm[index][0] = dn+1;
					exploration( d0, d1, d2, d3, d4, 
									 d5, d6, d7, d8, d9,
									 n0, n1, n2, n3, n4, 
									 n5, n6, n7, n8, n9,
									 s0, s1, s2, s3, s4,
									 index+1   );
					Dm[dn][0] = 0;
			}
		}
	} else {
		int *Sm[5] = { &s0, &s1, &s2, &s3, &s4};
		sumas(Nm, Sm);
		if ( valid_solution(s0, s1, s2, s3, s4) == 1) {
			printf("%i%i%i  %i%i%i  %i%i%i  %i%i%i  %i%i%i \n", n0,n5,n6, n1,n6,n7, n2,n7,n8, n3,n8,n9, n4,n9,n5);
		} 
	} 
}



int main() {
	clock_t start, end;

	start = clock();

	// P68
	//#pragma omp parallel for num_threads(12)
	
	exploration( 0,0,0,0,0, 
							 0,0,0,0,1, 

							10,0,0,0,0,  
							 0,0,0,0,0, 

							0,0,0,0,0, 
							1  );

	end = clock();
    // Calculating total time taken by the program.
    double time_taken = double(end - start) / double(CLOCKS_PER_SEC);
    cout << "Time taken by program is : " << fixed 
         << time_taken << setprecision(5);
    cout << " sec " << endl;
	return 0;
}