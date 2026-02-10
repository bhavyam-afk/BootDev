#include "vm.h"
#include "stack.h"
#include "objects.h"
 
vm_t *vm_new(){
    vm_t *ptr = (vm_t *)malloc(sizeof(vm_t));
    if(!ptr) return NULL;

    ptr -> frames = stack_new(8);
    ptr -> objects = stack_new(8);

    return ptr;
}

void vm_free(vm_t *vm){
    if(!vm) return NULL;

    for (int i = 0; i < vm->frames->count; i++) {
        frame_free(vm->frames->data[i]);
    }
    stack_free(vm -> frames);
    stack_free(vm -> objects);

    free(vm);
}

void vm_frame_push(vm_t *vm, frame_t *frame){
    if(!vm || !frame) return;
    stack_push(vm -> frames, frame);
    return;
}

frame_t *vm_new_frame(vm_t *vm){
    if(!vm) return NULL;
    frame_t *ptr = (frame_t *)malloc(sizeof(frame_t));

    ptr -> references = stack_new(8);
    vm_frame_push(vm, ptr);

    return ptr;
}

void frame_free(frame_t *frame){
    stack_free(frame -> references);
    free(frame);
}

void vm_track_object(vm_t *vm, object_tt *obj) {
    if(!vm || !obj) return;
    stack_push(vm -> objects, obj);
    return;
}

void frame_reference_object(frame_t *frame, object_tt *obj) {
    if(!frame || !obj) return;
    stack_push(frame -> references, obj);
    return;
}