#include <stdio.h>                                                              
#include <stdlib.h>                                                             
#include <string.h>                                                             
#include <unistd.h>    

//gcc -m32 -g -w -o format_vuln_2 -z execstack format_vuln_2.c


//read_flag() by Prof. Brumley                                                                            
void read_flag() {                                                              
  FILE *f = fopen("./flag.txt", "r");                                                
  if(!f) {                                                                      
    fprintf(stderr, "Failed to read flag (are you running in the right directory?)\n");                                                                         
    fprintf(stderr, "(Also, make sure you are not running in a debugger, which drops privileges)\n");                                                           
    exit(1);                                                                    
  }                                                                             
  char flag[100];                                                               
  flag[fread(flag, 1, 99, f)] = 0;                                              
  printf("You've earned this. Your flag is: %s\n", flag);                       
}   

void vuln() {
    printf("Help the current value is currently set to unlucky number 13!\n");
    printf("Can you change it for me\n");
    fflush(0);

    char user_input[100];
    fgets(user_input, sizeof(user_input), stdin);
    int not_important  = 25;
    int value = 13;
    int *ptr = &value;
    printf("Below is an unsafe print\n");
    printf(user_input);
    printf("\n");
    if(*ptr != 13) {
        printf("Now the value is %d\n", *ptr);
        printf("You saved me!\n");
        read_flag();

    } else {
        printf("You didn't save me\n");
    }
    exit(1);
}

int main(int argc, char** argv) {
    vuln();
}