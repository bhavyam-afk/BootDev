#include "objects.h"
#include <objects.c>
#include "mas.h"

bool set_array(object_tt *obj, size_t index, object_tt *value){
    if (!value || !obj){
        return false;
    }

    if (obj->kind != ARRAY){
        return false;
    }

    if ((index > (obj->data.v_array.size - 1))){
        return false;
    }
    
    object_tt *old = obj -> data.v_array.elements[index];
    if(old) refcount_dec(old);

    obj -> data.v_array.elements[index] = value;
    refcount_inc(value);
    return true;
}

object_tt *get_array(object_tt *obj, size_t index){
    if (!obj){
        return false;
    }

    if (obj->kind != ARRAY){
        return false;
    }

    if ((index > (obj->data.v_array.size - 1))){
        return false;
    }

    return obj -> data.v_array.elements[index];
}

int len_of_obj(object_tt *obj){
    if (obj == NULL) {
    return -1;
  }
  switch (obj->kind) {
  case INTEGER:
    return 1;
  case FLOAT:
    return 1;
  case VECTOR3:
    return 3;
  case STRING:
    return strlen(obj->data.v_string);
  case ARRAY:
    return obj->data.v_array.size;
  default:
    return -1;
  }
}
