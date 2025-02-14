#include <stdio.h>

void reorder_case_1(int int_1, int int_2, int* array_pointer_1, int* array_pointer_2, float float_1, float float_2)
{
    printf("     C side: int_1 = %d, int_2 = %d, array_pointer_1 = %p (%ld), array_pointer_2 = %p (%ld), float_1 = %f, float_2 = %f\n",
        int_1, int_2, array_pointer_1, (long)array_pointer_1, array_pointer_2, (long)array_pointer_2, float_1, float_2);
}
