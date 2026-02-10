#include <stddef.h>

typedef struct {
    size_t count;
    size_t capacity;
    void **data;
}stack_tt;

stack_tt *stack_new(size_t capacity); // returns a pointer having address of stack.
void stack_push(stack_tt *stack, void *obj); // just pushes to the stack.
void *stack_pop(stack_tt *stack); // return top element after pop that is a pointer having address of the top element.
void stack_free(stack_tt *stack); // free's memory of stack that was made by us only.
void stack_remove_nulls(stack_tt *stack); // removes nulls from the stack and compacts it.