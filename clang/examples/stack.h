#include <stdlib.h>
#include <stdio.h>

typedef struct {
  size_t** data;
  size_t capacity;
  size_t size;
} ULongStack;

void ulong_stack_init(ULongStack* stack, size_t capacity){
  stack -> data = malloc(capacity * sizeof(size_t*));
  stack -> capacity = capacity;
  stack -> size = 0;
}

void ulong_stack_push(ULongStack* stack, void* item){
  if(stack -> size < stack -> capacity){
    stack -> data[stack->size++] = item;
  }
}

void* ulong_stack_pop(ULongStack* stack){
  if(stack -> size > 0){
    return stack->data[--stack->size];
  }
  return NULL;
}

void ulong_stack_print(ULongStack* stack){
  for(size_t i = 0; i < stack->size; i++){
    printf("%zu ", *(size_t*)stack->data[i]);
  }
  printf("\n");
}


ULongStack createULongStack(size_t capacity){
  ULongStack stack;
  ulong_stack_init(&stack, capacity);
  return stack;
}
