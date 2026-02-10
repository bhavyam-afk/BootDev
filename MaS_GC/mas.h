#include "objects.h"

void trace(vm_t *vm);
void trace_blacken_object(stack_tt *gray_objects, object_tt *obj);
void trace_mark_object(stack_tt *gray_objects, object_tt *obj);
void mark(vm_t *vm);
void vm_collect_garbage(vm_t *vm);
void sweep(vm_t *vm);
void object_free(object_tt *obj); 