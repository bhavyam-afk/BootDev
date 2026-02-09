#include "objects.h"

void refcount_inc(object_tt *obj);
void refcount_dec(object_tt *obj);
void refcount_free(object_tt *obj);