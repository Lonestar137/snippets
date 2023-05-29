#include "examples/stack.h"
#include <stdio.h>

// Just a demonstration of how to print different types and type checking.
// void* is a catchall pointer.
// - You must know what types will be passed to this function beforehand or risk errors.
void printingSnippet(void* someValue){
  // sizeof -- int = 4
  // sizeof -- unsigned long, signed long, double = 8 

  if(someValue == NULL){
    printf("Null value was passed to f(printingSnippet)");
    return;
  }

  if(sizeof(int) == sizeof(someValue)){
    int value = *(int*)someValue;
    printf("Integer: %d\n", value);
  } else if(sizeof(double) == sizeof(someValue)){
    double value = *(double*)someValue;
    printf("Double: %f\n", value);
  } else if(sizeof(size_t) == sizeof(someValue)){
    size_t value = *(size_t*)someValue; // unsigned int(size_t)

    printf("Unsigned Int: %zu\n", value);
  } else if(sizeof(unsigned long) == sizeof(someValue)){
    /*
     * unsigned long
     * - non-negative, min 0.
     * - max size varies based on system bit size for longs.
     * */
    unsigned long value = *(unsigned long*)someValue;
    printf("Unsigned Long: %lu\n", value); 
  } else if(sizeof(signed long) == sizeof(someValue)){
    /*
     * signed long
     * - Can be negative.
     * - max size varies based on system bit size for longs.
     * */
    signed long value = *(signed long*)someValue;
    printf("Signed Long: %lu\n", value); // supposedly, this is correct way.
  } else {
    printf("Unknown type");
  }
}

int main(){
  int a[18];
  size_t arraySize = sizeof(a)/sizeof(a[0]);
  int test = 100;
  double test2 = 3.14;
  int* pointer = &test;

  printingSnippet(&arraySize);
  printingSnippet(&test);
  printingSnippet(&test2);

  size_t capacity = 10;
  ULongStack stack = createULongStack(capacity);
  ulong_stack_push(&stack, &arraySize);
  ulong_stack_push(&stack, &arraySize);
  ulong_stack_print(&stack); // 18 18
  ulong_stack_pop(&stack);
  ulong_stack_print(&stack); // 18

}
