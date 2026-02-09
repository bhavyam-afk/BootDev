#include "useful_functions.c"
#include "refcounting.h"

void refcount_inc(object_tt *obj){
    if(!obj) return;
    (obj -> refcount)++ ;
    return;
}

void refcount_dec(object_tt *obj) {
    if(!obj) return;
    (obj -> refcount)--;
    if(obj -> refcount == 0){
        refcount_free(obj);
    }
    return;
}

void refcount_free(object_tt *obj) {
    if(!obj) return;
    else if(obj -> kind == STRING){
        free(obj -> data.v_string);
    }
    else if(obj -> kind == VECTOR3){
        refcount_dec(obj -> data.v_vector3.x);
        refcount_dec(obj -> data.v_vector3.y);
        refcount_dec(obj -> data.v_vector3.z);
    }
    else if(obj -> kind == ARRAY){
        for (size_t i = 0; i < obj->data.v_array.size; i++) {
            if (obj->data.v_array.elements[i]) {
                refcount_dec(obj->data.v_array.elements[i]);
            }
        }
        free(obj->data.v_array.elements);
    }
    free(obj);
    return;
}
