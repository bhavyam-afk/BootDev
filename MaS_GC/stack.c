#include "stack.h"
#include <stdlib.h>

stack_tt *stack_new(size_t capacity){
    stack_tt *ptr = (stack_tt *)malloc(sizeof(stack_tt));
    if(!ptr) return NULL;

    ptr -> count = 0;
    ptr -> capacity = capacity;
    ptr -> data = (void *)malloc(ptr -> capacity * sizeof(void *));
    if(!ptr->data){
        free(ptr);
        return NULL;
    }
    
    return ptr;
}

void stack_push(stack_tt *stack, void *obj){
    if(stack->count == stack->capacity){
        stack->capacity *= 2;
        void **new_data = realloc(stack->data, stack->capacity);
        if(!new_data){
            stack->capacity /= 2;
            return;
        }
        stack->data = new_data;
    }
    stack->data[stack->count] = obj;
    stack->count++;
}

void *stack_pop(stack_tt *stack){
    if(!stack || !stack->data) return;
    stack->count--;
    return stack->data[stack->count];
}

void stack_free(stack_tt *stack){
    if(!stack) return;
    if(stack->data) free(stack->data);
    free(stack);
    return;
}

void stack_remove_nulls(stack_tt *stack) {
  size_t new_count = 0;

  // Iterate through the stack and compact non-NULL pointers.
  for (size_t i = 0; i < stack->count; ++i) {
    if (stack->data[i] != NULL) {
      stack->data[new_count++] = stack->data[i];
    }
  }

  // Update the count to reflect the new number of elements.
  stack->count = new_count;

  // Optionally, you might want to zero out the remaining slots.
  for (size_t i = new_count; i < stack->capacity; ++i) {
    stack->data[i] = NULL;
  }
}