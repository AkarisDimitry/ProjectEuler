#include <cstdio>
#include <bits/stdc++.h>
#include <omp.h>
#include <iostream>
//#include <cmath>

using namespace std;

long maxN=0;

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

long combine(long a, long b) {
   int times = 1;
   while (times <= b)
      times *= 10;
   long com = a*times + b;
   return com;
} 
 
bool isPandigital(unsigned long long x)
{
  unsigned char used[10] = { 0 };
  while (x > 0)
  {
    auto digit = x % 10;
    // digit already used ?
    if (used[digit] == 1)
      return false;
    used[digit]++;
    x /= 10;
  }

  return true;
}

bool isPandigital2(unsigned long long x1, unsigned long long x2) {
  unsigned char used[10] = { 0 };
  while (x1 > 0)  {
    auto digit = x1 % 10;
    if (used[digit] == 1)
      return false;
    used[digit]++;
    x1 /= 10;
  }

  while (x2 > 0)  {
    auto digit = x2 % 10;
    if (used[digit] == 1)
      return false;
    used[digit]++;
    x2 /= 10;
  }

  return true;
}

bool isPandigital3(unsigned long long x1, unsigned long long x2, unsigned long long x3) {
  unsigned char used[10] = { 0 };
  while (x1 > 0)  {
    auto digit = x1 % 10;
    if (used[digit] == 1)
      return false;
    used[digit]++;
    x1 /= 10;
  }

  while (x2 > 0)  {
    auto digit = x2 % 10;
    if (used[digit] == 1)
      return false;
    used[digit]++;
    x2 /= 10;
  }

  while (x3 > 0)  {
    auto digit = x3 % 10;
    if (used[digit] == 1)
      return false;
    used[digit]++;
    x3 /= 10;
  }

  return true;
}


void dig2num1(		int n0, int *num ) {
	num[0] = n0;
}

void dig2num2(		int n0, int n1, int *num ) {
	num[0] = n0 + 10*n1;
}

void dig2num3(		int n0, int n1, int n2,  int *num ) {
	num[0] = n0 + 10*n1 + 100*n2;
}

void dig2num4(		int n0, int n1, int n2, int n3, int *num ) {
	num[0] = n0 + 10*n1 + 100*n2 + 1000*n3;
}

void dig2num5(		int n0, int n1, int n2, int n3, int n4, int *num ) {
	num[0] = n0 + 10*n1 + 100*n2 + 1000*n3 + 10000*n4;
}

void dig2num6(		int n0, int n1, int n2, int n3, int n4, int n5, int *num ) {
	num[0] = n0 + 10*n1 + 100*n2 + 1000*n3 + 10000*n4 + 100000*n5;
}

void dig2num7(		int n0, int n1, int n2, int n3, int n4, int n5, int n6, int *num ) {
	num[0] = n0 + 10*n1 + 100*n2 + 1000*n3 + 10000*n4 + 100000*n5 + 1000000*n6;
}

void dig2num8(		int n0, int n1, int n2, int n3, int n4, int n5, int n6, int n7, int *num ) {
	num[0] = n0 + 10*n1 + 100*n2 + 1000*n3 + 10000*n4 + 100000*n5 + 1000000*n6 + 10000000*n7;
}

void dig2num9(		int n0, int n1, int n2, int n3, int n4, int n5, int n6, int n7, int n8, int *num ) {
	num[0] = n0 + 10*n1 + 100*n2 + 1000*n3 + 10000*n4 + 100000*n5 + 1000000*n6 + 10000000*n7 + 100000000*n8;
}

void dig2num10(	int n0, int n1, int n2, int n3, int n4, int n5, int n6, int n7, int n8, int n9, int *num ) {
	num[0] = n0 + 10*n1 + 100*n2 + 1000*n3 + 10000*n4 + 100000*n5 + 1000000*n6 + 10000000*n7 + 100000000*n8 + 1000000000*n9;
}

void dig2num(int *num, int **digits, int Ndigits) {
	if      (Ndigits==1)  { dig2num1( digits[0][0], num ); }
	else if (Ndigits==2)  { dig2num2( digits[1][0], digits[0][0], num ); }
	else if (Ndigits==3)  { dig2num3( digits[2][0], digits[1][0], digits[0][0], num ); }
	else if (Ndigits==4)  { dig2num4( digits[3][0], digits[2][0], digits[1][0], digits[0][0], num ); }
	else if (Ndigits==5)  { dig2num5( digits[4][0], digits[3][0], digits[2][0], digits[1][0], digits[0][0], num ); }
	else if (Ndigits==6)  { dig2num6( digits[5][0], digits[4][0], digits[3][0], digits[2][0], digits[1][0], digits[0][0], num ); }
	else if (Ndigits==7)  { dig2num7( digits[6][0], digits[5][0], digits[4][0], digits[3][0], digits[2][0], digits[1][0], digits[0][0], num ); }
	else if (Ndigits==8)  { dig2num8( digits[7][0], digits[6][0], digits[5][0], digits[4][0], digits[3][0], digits[2][0], digits[1][0], digits[0][0], num ); }
	else if (Ndigits==9)  { dig2num9( digits[8][0], digits[7][0], digits[6][0], digits[5][0], digits[4][0], digits[3][0], digits[2][0], digits[1][0], digits[0][0], num ); }
	else if (Ndigits==10) { dig2num10(digits[9][0], digits[8][0], digits[7][0], digits[6][0], digits[5][0], digits[4][0], digits[3][0], digits[2][0], digits[1][0], digits[0][0], num ); }
}

void exploration2(int n0, int n1, int n2, int n3, int n4, 
						int n5, int n6, int n7, int n8, int n9,
						int s1, int s2, int s3, int s4, int s5, 
						int s6, int s7, int s8, int s9, int index) {
	int *Nm[10] = { &n0, &n1, &n2, &n3, &n4,
						&n5, &n6, &n7, &n8, &n9,  };
	int *Sm[9] = { &s1, &s2, &s3, &s4,
						&s5, &s6, &s7, &s8, &s9,  }; 
	if (index<9) {
		for (int n=0; n<2; n++) {	
			Sm[index][0] = n;
			exploration2(n0, n1, n2, n3, n4, 
						    n5, n6, n7, n8, n9,
						    s1, s2, s3, s4, s5, 
						    s6, s7, s8, s9, index+1);
		}	
	} else {

		int S_sum = s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9;
		if (S_sum>2 && S_sum<6) {

			long Narray[10] = {0}; 
			int number_position = 0;
			long number = (long)Nm[9][0];
			long exponent = 10;

			for (int n=8; n>=0; n--) {	
				
				if (Sm[n][0] == 0 || Nm[n+1][0] == 0 ) {
					number += (long)Nm[n][0]*exponent;
					exponent *= 10;
				}	else {

					Narray[number_position] = number; 
					number = (long)Nm[n][0];
					exponent = 10;
					number_position += 1;
				}
			}	 

			Narray[number_position] = number;
			long full_num = combine( 	(long) Narray[number_position]*Narray[number_position-1], 
												(long) Narray[number_position]*Narray[number_position-2]);
			for (int n=3; n<=number_position; n++) {	
				full_num = combine( 	full_num, (long) Narray[number_position]*Narray[number_position-n] );
			}

			if ( full_num>maxN && Narray[number_position-1] != 0 && Narray[number_position-2] != 0 && Narray[number_position-3] != 0) {
				if (isPandigital(full_num)) {
					maxN = full_num;
					printf("concatenating products %li \n", full_num);
				}
			}
		}
	}

}


void exploration(	int d0, int d1, int d2, int d3, int d4, 
						int d5, int d6, int d7, int d8, int d9,
						int n0, int n1, int n2, int n3, int n4, 
						int n5, int n6, int n7, int n8, int n9,
						int index   ) {
	int *Nm[10] = { &n0, &n1, &n2, &n3, &n4,
						&n5, &n6, &n7, &n8, &n9,  };

	int *Dm[10] = { &d0, &d1, &d2, &d3, &d4,
						&d5, &d6, &d7, &d8, &d9,  }; 

	if (index < 10) {
		if (index == 0) {
			for (int dn=1; dn<10; dn++) {
				printf("%i\n", dn);
				if (Dm[dn][0] == 0) {
					Dm[dn][0] = 1;
					Nm[index][0] = dn;
					exploration( d0, d1, d2, d3, d4, 
									 d5, d6, d7, d8, d9,
									 n0, n1, n2, n3, n4, 
									 n5, n6, n7, n8, n9,
									 index+1   );
					Dm[dn][0] = 0;
				}
			}
		} else {
			for (int dn=0; dn<10; dn++) {
				if (Dm[dn][0] == 0) {
					Dm[dn][0] = 1;
					Nm[index][0] = dn;
					exploration( d0, d1, d2, d3, d4, 
									 d5, d6, d7, d8, d9,
									 n0, n1, n2, n3, n4, 
									 n5, n6, n7, n8, n9,
									 index+1   );
					Dm[dn][0] = 0;
				}
			}
		}

	} else {
		
		int num1, num2, num3;
		for (int p1=1; p1<8; p1++) {
			if (Nm[p1][0] != 0) {

				dig2num(&num1, Nm, p1);
				for (int p2=p1+1; p2<9; p2++) {
					if (Nm[p2][0] != 0) {

						dig2num(&num2, &Nm[p1], p2-p1);
						dig2num(&num3, &Nm[p2], 10-p2);

						long full_num = combine( 	(long) num1*num2, 
															(long) num1*num3);

						if ( full_num>maxN) {
							if (isPandigital(full_num)) {
								maxN = full_num;
								printf("concatenating products %li \n", full_num);
								printf("%i*%i=%i \n%i*%i=%i \n", num1,num2,num1*num2, num1,num3,num1*num3);
								
							}
						}
					}
				}
			}

		}

		//exploration2(n0, n1, n2, n3, n4, 
		//				 n5, n6, n7, n8, n9,
		//				 0, 0, 0, 0, 0, 
		//				 0, 0, 0, 0, 0);
		
	}
}


int main() {
	clock_t start, end;

	start = clock();

	// P8
	//#pragma omp parallel for num_threads(12)
		
	exploration(	0,0,0,0,0, 
						0,0,0,0,0, 
						0,0,0,0,0,  
						0,0,0,0,0, 
						0   );

	end = clock();
    // Calculating total time taken by the program.
    double time_taken = double(end - start) / double(CLOCKS_PER_SEC);
    cout << "Time taken by program is : " << fixed 
         << time_taken << setprecision(5);
    cout << " sec " << endl;
	return 0;
}