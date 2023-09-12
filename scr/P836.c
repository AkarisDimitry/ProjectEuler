#include <stdio.h>
#include <time.h>
/*  <p>Let $A$ be an <b>affine plane</b> over a <b>radically integral local field</b> $F$ with 
    residual characteristic $p$.</p>
    <p>We consider an <b>open oriented line section</b> $U$ of $A$ with normalized Haar measure
     $m$.</p>
    <p>Define $f(m, p)$ as the maximal possible discriminant of the <b>jacobian</b> associated
     to the <b>orthogonal kernel embedding</b> of $U$ <span style="white-space:nowrap;">into
      $A$.</span></p>
    <p>Find $f(20230401, 57)$. Give as your answer the concatenation of the first letters of 
    each bolded word.</p>
*/

// Function P836
char* P836(int N) {
    return "aprilfoolsjoke";
}

int main() {
    clock_t start, end;
    double cpu_time_used;
    
    start = clock();
    char* result = P836(0); // Calling the P836 function
    end = clock();
    
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Result of P836 : %s (execution time %f seconds)\n", result, cpu_time_used);
    return 0;
}
