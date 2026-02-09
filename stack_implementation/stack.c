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
