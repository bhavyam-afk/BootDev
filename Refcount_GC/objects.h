#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct object{
    object_kind_tt kind;
    object_data_tt data;
    int refcount;
}object_tt;

typedef enum kind{
    INTEGER,
    FLOAT,
    STRING,
    VECTOR3,
    ARRAY
} object_kind_tt;

typedef union data{
    int v_int;
    float v_float;
    char *v_string;
    vector_tt v_vector3;
    array_tt v_array;
}object_data_tt;

typedef struct vector3{
    object_tt *x;
    object_tt *y;
    object_tt *z;
}vector_tt;

typedef struct array{
    size_t size;
    object_tt **elements;
}array_tt;

object_tt *new_object();
object_tt *new_integer(int value); //creates a pointer to object of type integer in heap memory. 
object_tt *new_float(float value); // creates a pointer to object of type float in heap memory. 
object_tt *new_string(char *value); // creates a pointer to object of type char * in heap memory.
object_tt *new_vector3(object_tt *x, object_tt *y, object_tt *z); // creates a pointer to object of type vector3 in heap memory.
object_tt *new_array(size_t size); // creates a variable that stores address of an object of type array in the heap memory. here we do not need to allocate memory for x,y,z because they are already object addresses so they would already have allocated memory.

bool set_array(object_tt *obj, size_t index, object_tt *value);
object_tt *get_array(object_tt *obj, size_t index);
int len_of_obj(object_tt *obj);
object_tt *_add(object_tt *a, object_tt *b);