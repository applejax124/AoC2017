#include <stdio.h>

int main(){
  int d=0, e=0, f=0, g=0, h=0;
  int b = 57*100 + 100000;
  int c = b + 17000;
  
  do{
  
    f=1, d=2;
  
    do{
    
      e = 2;
  
      do{
  
        g = b - (d*e);
        if (g == 0)
          f = 0;
        
        e++;
  
      } while (e != b);
  
      d++;
  
    } while (d != b);
  
    if (f == 0)
      h++;
  
    b += 17;
  
  } while (b != c);
  
  printf("%d", h);
}
