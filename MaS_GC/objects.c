#include "mas.h"
#include "objects.h"

object_tt *new_object(vm_t *vm){
    object_tt *ptr = (object_tt *)malloc(sizeof(object_tt));
    if(!ptr) return NULL;
    ptr -> is_marked = false;
    vm_track_object(vm, ptr);
    return ptr;
}

object_tt *new_integer(int value, vm_t *vm){
    object_tt *ptr = new_object(vm);
    if(!ptr) return NULL;

    ptr -> kind = INTEGER;
    ptr -> data.v_int = value;
    return ptr;
}

object_tt *new_float(float value, vm_t *vm){
    object_tt *ptr = new_object(vm);
    if(!ptr) return NULL;

    ptr -> kind = FLOAT;
    ptr -> data.v_float = value;
    return ptr;
}

object_tt *new_string(char *value, vm_t *vm){
    object_tt *ptr = new_object(vm);
    if(!ptr) return NULL;
    int len = strlen(value)+1;
    // string ko store krne ki space.
    char *length = (char *)malloc(len+1);
    // make string at this alloctaed space.
    strcpy(length, value);
    ptr -> kind = STRING;
    // object ke data ko we give first index only but in heap now we have complete space.
    ptr -> data.v_string = length;
    return ptr;
}

object_tt *new_vector3(object_tt *x, object_tt *y, object_tt *z, vm_t *vm){
    if(!x || !y || !z) return NULL;
    object_tt *ptr = new_object(vm);
    if(!ptr) return NULL;
    ptr -> kind = VECTOR3;
    ptr -> data.v_vector3 = (vector_tt){.x = x, .y = y, .z = z};
}

object_tt *new_array(size_t size, vm_t *vm){
    object_tt *ptr = new_object(vm);
    if(!ptr) return NULL;
    object_tt **space = (object_tt **)calloc(size, sizeof(object_tt *));
    if(!space){
        free(ptr);
        return NULL;
    }
    ptr -> kind = ARRAY;
    ptr -> data.v_array.size = size;
    ptr -> data.v_array.elements = space;
    return ptr;
}


