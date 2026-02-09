#include "objects.h"
#include <objects.c>

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

    obj -> data.v_array.elements[index] = value;
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

object_tt *_add(object_tt *a, object_tt *b){
    if (!a || !b){
        return NULL;
    }
    if (a->kind == INTEGER){
        if (b->kind == INTEGER){
            return new_integer(a->data.v_int + b->data.v_int);
        }
        else if (b->kind == FLOAT){
            object_tt *ans = new_float(a->data.v_int + b->data.v_float);
            ans->kind = FLOAT;
            ans->data.v_float = a->data.v_int + b->data.v_float;
            return ans;
        }
        else return NULL;
    }
    else if (a->kind == FLOAT){
        if (b->kind == INTEGER){
            object_tt *ans = new_float(a->data.v_float + b->data.v_int);
            ans->kind = FLOAT;
            ans->data.v_float = a->data.v_float + b->data.v_int;
            return ans;
        }
        else if (b->kind == FLOAT){
            object_tt *ans = new_float(a->data.v_float + b->data.v_float);
            ans->kind = FLOAT;
            ans->data.v_float = a->data.v_float + b->data.v_float;
            return ans;
        }
        else return NULL;
    }
    else if (a->kind == STRING){
        if (b->kind != STRING){
            return NULL;
        }
        else{
            int len = 1 + strlen(a->data.v_string) + strlen(b->data.v_string);
            char *ans = (char *)malloc(len);
            strcat(ans, a->data.v_string);
            strcat(ans, b->data.v_string);
            return new_string(ans);
        }
    }
    else if (a->kind == VECTOR3){
        if (b->kind != VECTOR3){
            return NULL;
        }
        object_tt *x = _add(a->data.v_vector3.x, b->data.v_vector3.x);
        object_tt *y = _add(a->data.v_vector3.y, b->data.v_vector3.y);
        object_tt *z = _add(a->data.v_vector3.z, b->data.v_vector3.z);

        if (!x || !y || !z){
            return NULL;
        }
        return new_vector3(x, y, z);
    }

    else if (a->kind == ARRAY){
        if (b->kind != ARRAY){
            return NULL;
        }
        size_t size_a = a->data.v_array.size;
        size_t size_b = b->data.v_array.size;

        object_tt *result = new_array(size_a + size_b);
        if (!result){
            return NULL;
        }

        for (size_t i = 0; i < size_a; i++){
            set_array(result, i, get_array(a, i));
        }

        for (size_t i = 0; i < size_b; i++){
            set_array(result, size_a + i, get_array(b, i));
        }
        return result;
    }
    return NULL;
}