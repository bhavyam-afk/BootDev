#include <stddef.h>
#include "stack.h"

// what things we need to track
typedef struct virtual_machine{
    stack_tt *frames; // address of stack of "stack frames" pushed or popped as we enter new scopes of function.
    stack_tt *objects; // address of stack holding pointers to objects.
}vm_t;

// Stack frame struct 
typedef struct stack_frame{
    stack_tt *references; // address of a stack that has pointers to objects that are referenced in the stack frame.
}frame_t;

vm_t *vm_new(); 
void vm_free(vm_t *vm);
void vm_frame_push(vm_t *vm, frame_t *frame);
frame_t *vm_new_frame(vm_t *vm);
void frame_free(frame_t *frame);
void vm_track_object(vm_t *vm, object_tt *obj);
void frame_reference_object(frame_t *frame, object_tt *obj);
