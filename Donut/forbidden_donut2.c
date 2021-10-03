k;
double sin(),cos();
main()
{
float A=0, B=0,i,j,z[1760];
char b[1760];
printf("\x1b[2J");
for(;;){
  memset(b,32,1760);
  memset(z,0,7040);
  for(j=0;6.28>j;j+=0.07)
  for(i=0;6.28>i;i+=0.02){
    float c=sin(i),d=cos(j),e=sin(A),f=sin(j),g=cos(A),h=d+2,D=1/(c*h*e*+f*g+5),l=cos(i),m=cos(B),n=sin(B),t=c*h*g-f*e;}
}
}
