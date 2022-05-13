/* You can compile and run this code with the following command
 *
 * gcc main.c -o donut -lm;./donut
 *
 * I have made as few edits to this code as reasonable, mostly reformatting.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

/* C assumes that values that have a undefined type are integers */
k;

/* Definition of functions, these are implemented in math.h, for simplicity */
double sin(), cos();

#define TERM_WIDTH  80
#define TERM_HEIGHT 22
#define PI 3.14

/* main is assumed to return type of int */
main() {
     float    A = 0,
  /* float */ B = 0,
  /* float */ i,
  /* float */ j,
  /* float */ z[TERM_HEIGHT][TERM_WIDTH]; /* Allocates space for z-index */

    char b[TERM_HEIGHT][TERM_WIDTH]; /* Allocates space to store to ascii art */

    printf("\x1b[2J"); /*clear the screen */

    for(;;) { /* INFINITE LOOP START */
        memset( b, ' ', TERM_HEIGHT * TERM_WIDTH * sizeof(char));
        memset( z,   0, TERM_HEIGHT * TERM_WIDTH * sizeof(float));

        for(j = 0; 2*PI > j; j += 0.07) // represents theta
            for(i = 0; 2*PI > i; i += 0.02) { // represents phi
            /* FOR-LOOP START*/


             float    c = sin(i),
          /* float */ d = cos(j),
          /* float */ e = sin(A),
          /* float */ f = sin(j),
          /* float */ g = cos(A),
          /* float */ h = d + 2,
          /* float */ D = 1 / (c * h * e + f * g + 5),
          /* float */ l = cos(i),
          /* float */ m = cos(B),
          /* float */ n = sin(B),
          /* float */ t = c * h * g - f * e;

                int    x = 40 + 30 * D * ( l * h * m - t * n ),
             /* int */ y = 12 + 15 * D * ( l * h * n + t * m ),
            /* int */ o = x + 80 * y,
             /* int */ N = 8 * ((f*e-c*d*g)*m-c*d*e-f*g-l*d*n);

                if ( TERM_HEIGHT > y && y > 0 && x > 0 && TERM_WIDTH > x && D > z[y][x] ) {
                    z[y][x]=D;;;
                    b[y][x]= ".,-~:;=!*#$@"[ N > 0 ? N : 0 ];
                    /* String here is a list of characters that will be  printed into array b. Value
                     * at N is used to determine if a character should be printed. o is the index.*/
                }

            } /* FOR-LOOP END */

        printf("\x1b[H");

        for(int k = 0; 1761 > k; k++)
            // could not be arsed to rewrite this as a loop over x and y
            putchar( k % TERM_WIDTH ? ((char*) b)[k] : '\n' );

        A += 0.04;
        B += 0.02;
    } /* INFINITE LOOP END */
}