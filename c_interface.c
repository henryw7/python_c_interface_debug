#include <stdio.h>

void reorder_case_1(int int_1, int int_2, int* array_pointer_1, int* array_pointer_2, float float_1, float float_2)
{
    printf("     C side: int_1 = %d, int_2 = %d, array_pointer_1 = %p (%ld), array_pointer_2 = %p (%ld), float_1 = %f, float_2 = %f\n",
        int_1, int_2, array_pointer_1, (long)array_pointer_1, array_pointer_2, (long)array_pointer_2, float_1, float_2);
}

void reorder_case_2(int int_1, int int_2, float float_1, float float_2, double double_1, double double_2)
{
    printf("     C side: int_1 = %d, int_2 = %d, float_1 = %f, float_2 = %f, double_1 = %f, double_2 = %f\n",
        int_1, int_2, float_1, float_2, double_1, double_2);
}

void reorder_case_3(int int_1, int int_2, int int_3, int int_4, int int_5, int int_6, int int_7, int int_8,
                    int int_9, int int_10, int int_11, int int_12, int int_13, int int_14, int int_15, int int_16,
                    int int_17, int int_18, int int_19, int int_20, int int_21, int int_22, int int_23, int int_24,
                    float float_1, float float_2, float float_3, float float_4, float float_5, float float_6,
                    float float_7, float float_8, float float_9, float float_10, float float_11, float float_12)
{
    printf("     C side: int_1-24 = %d,%d,%d,%d,%d,%d,%d,%d, %d,%d,%d,%d,%d,%d,%d,%d, %d,%d,%d,%d,%d,%d,%d,%d\n"
           "             float_1-12 = %f,%f,%f,%f, %f,%f,%f,%f, %f,%f,%f,%f\n",
        int_1, int_2, int_3, int_4, int_5, int_6, int_7, int_8,
        int_9, int_10, int_11, int_12, int_13, int_14, int_15, int_16,
        int_17, int_18, int_19, int_20, int_21, int_22, int_23, int_24,
        float_1, float_2, float_3, float_4, float_5, float_6,
        float_7, float_8, float_9, float_10, float_11, float_12);
}
