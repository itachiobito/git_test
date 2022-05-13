#include <stdio.h> 
#include <string.h>

int k; 
double sin(), cos();
int main()
{
    float A=0, B=0,i,j,z[1760];
    char b[1760];
    printf("\x1b[2J");
    for(;;){
        memset(b,32,1760);
        memset(z,0,7040);
        for(j=0;6.28>j;j+=0.07)
        for(i=0;6.28>i;i+=0.02){
            printf("%d ",j);
        }
        return 0;
    }
}