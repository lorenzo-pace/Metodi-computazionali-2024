#include <stdio.h>
#include <math.h> 

double fibonacci (int n) {

    unsigned long int f1=1, f2=1, f3;

    if (n<=0) {
        return -1;
    }
    if(n==1 || n==2) 
        return 1;
    else {
        for (int j = 3; j <=n; j++) {
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
        //printf("%d\n", f3);
        }
        f3=f1+f2;
        //printf("%d %d \n", f3, f2);
        return (double)f3/f2;
    }
    
}
