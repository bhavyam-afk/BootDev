#include "useful_functions.c"
#include "mas.h"
#include "objects.h"


void mark(vm_t *vm) {
    if(!vm) return;
    for(size_t i = 0; i < vm -> frames -> count; i++){
        frame_t *frame = vm -> frames -> data[i];
        for(size_t j = 0; j < frame -> references -> count; j++){
            object_tt *obj = frame -> references -> data[j];
            obj -> is_marked = true;    
        }
    }
}

void trace(vm_t *vm) {
    if(!vm) return;
    stack_tt *gray_objects = new_stack(8, vm);
    if(!gray_objects) return;
    for(int i=0 ; i<vm->objects->count; i++){
        object_tt *obj = vm -> objects -> data[i];
        if(obj -> is_marked){
            stack_push(gray_objects, obj);
        }
    }
    while(gray_objects -> count != 0){
        trace_blacken_object(gray_objects, stack_pop(gray_objects));
        stack_free(gray_objects);
    }
}

void trace_blacken_object(stack_tt *gray_objects, object_tt *obj) {
    if(!obj || !gray_objects) return;
    switch(obj -> kind){
        case INTEGER:
        case FLOAT:
        case STRING:
            break;
        case VECTOR3:{
            trace_mark_object(gray_objects, obj -> data.v_vector3.x);
            trace_mark_object(gray_objects, obj -> data.v_vector3.y);
            trace_mark_object(gray_objects, obj -> data.v_vector3.z);
            break;
        }
        case ARRAY:{
            for(int i=0 ; i < obj -> data.v_array.size; i++){
                trace_mark_object(gray_objects, obj -> data.v_array.elements[i]);
            }
            break;
        }
        default:
            break;
    }
}

void trace_mark_object(stack_tt *gray_objects, object_tt *obj) {
    if(!obj || obj -> is_marked) return;
    obj -> is_marked = true;
    stack_push(gray_objects, obj);
    return;
}


void vm_collect_garbage(vm_t *vm) {
    mark(vm);
    trace(vm);
    sweep(vm);
}

void sweep(vm_t *vm) {
    for(int i=0 ; i<vm->objects->count; i++){
        object_tt *obj = vm -> objects -> data[i];
        if(obj -> is_marked){
            obj -> is_marked = false;
        }
        else{
            object_free(obj);
            vm -> objects -> data[i] = NULL;
        }
    }
    stack_remove_nulls(vm -> objects);
}


void object_free(object_tt *obj){
    switch (obj->kind){
        case INTEGER:
        case FLOAT:
            break;
        case STRING:
            free(obj->data.v_string);
            break;
        case VECTOR3:{
            break;
        }
        case ARRAY:{
            array_tt *array = &obj->data.v_array;
            free(array->elements);
            break;
        }
    }
    free(obj);
}



