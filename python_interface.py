
import cupy as cp
import ctypes

libc_interface = ctypes.cdll.LoadLibrary("libc_interface_debug.so")

int_1 = 7
int_2 = 8

array_1 = cp.zeros((2,2), dtype = int)
array_pointer_1 = ctypes.cast(array_1.data.ptr, ctypes.c_void_p)
array_2 = cp.eye(3)
array_pointer_2 = ctypes.cast(array_2.data.ptr, ctypes.c_void_p)

float_1 = 7.8
float_2 = 8.7

print(f"Python side: int_1 = {int_1}, int_2 = {int_2}, array_pointer_1 = 0x{array_pointer_1.value:x} ({array_pointer_1.value}), array_pointer_2 = 0x{array_pointer_2.value:x} ({array_pointer_2.value}), float_1 = {float_1}, float_2 = {float_2}")

print("Correct call")
libc_interface.reorder_case_1(
    ctypes.c_int(int_1),
    ctypes.c_int(int_2),
    array_pointer_1,
    array_pointer_2,
    ctypes.c_float(float_1),
    ctypes.c_float(float_2),
)

print("Move float_1 to some random position above float_2, on C side, nothing changed")
libc_interface.reorder_case_1(
    ctypes.c_float(float_1),
    ctypes.c_int(int_1),
    ctypes.c_int(int_2),
    array_pointer_1,
    array_pointer_2,
    ctypes.c_float(float_2),
)

print("Move float_2 to some random position above float_1, on C side, only the two floats interchanged")
libc_interface.reorder_case_1(
    ctypes.c_int(int_1),
    ctypes.c_float(float_2),
    ctypes.c_int(int_2),
    array_pointer_1,
    array_pointer_2,
    ctypes.c_float(float_1),
)

float_3 = 9.9
float_4 = 10.01

print("Add more floats below, on C side, nothing changed")
libc_interface.reorder_case_1(
    ctypes.c_float(float_1),
    ctypes.c_float(float_2),
    ctypes.c_float(float_3),
    ctypes.c_float(float_4),
    ctypes.c_int(int_1),
    ctypes.c_int(int_2),
    array_pointer_1,
    array_pointer_2,
)

print("Add more floats above, on C side, the first two floats are taken as float_1 and float_2")
libc_interface.reorder_case_1(
    ctypes.c_float(float_3),
    ctypes.c_float(float_4),
    ctypes.c_float(float_1),
    ctypes.c_float(float_2),
    ctypes.c_int(int_1),
    ctypes.c_int(int_2),
    array_pointer_1,
    array_pointer_2,
)

float_1 = 1.0 / 3.0
float_2 = 2.0 / 3.0
double_1 = 1.0 / 7.0
double_2 = 2.0 / 7.0

print()
print(f"Python side: int_1 = {int_1}, int_2 = {int_2}, float_1 = {float_1:.6f}, float_2 = {float_2:.6f}, double_1 = {double_1:.6f}, double_2 = {double_2:.6f}")

print("Correct call")
libc_interface.reorder_case_2(
    ctypes.c_int(int_1),
    ctypes.c_int(int_2),
    ctypes.c_float(float_1),
    ctypes.c_float(float_2),
    ctypes.c_double(double_1),
    ctypes.c_double(double_2),
)

print("No reorder within float or double, just put them in between integer arugments, on C side, nothing changed")
libc_interface.reorder_case_2(
    ctypes.c_float(float_1),
    ctypes.c_int(int_1),
    ctypes.c_float(float_2),
    ctypes.c_double(double_1),
    ctypes.c_int(int_2),
    ctypes.c_double(double_2),
)

print("Mess up float and double, on C side, the result also get messed up")
libc_interface.reorder_case_2(
    ctypes.c_int(int_1),
    ctypes.c_int(int_2),
    ctypes.c_double(double_1),
    ctypes.c_double(double_2),
    ctypes.c_float(float_1),
    ctypes.c_float(float_2),
)

print("Only mess up the order between float_2 and double_1, the other two are preserved")
libc_interface.reorder_case_2(
    ctypes.c_int(int_1),
    ctypes.c_int(int_2),
    ctypes.c_float(float_1),
    ctypes.c_double(double_1),
    ctypes.c_float(float_2),
    ctypes.c_double(double_2),
)

int_1 = 11
int_2 = 12
int_3 = 13
int_4 = 14
int_5 = 15
int_6 = 16
int_7 = 17
int_8 = 18
int_9 = 19
int_10 = 110
int_11 = 111
int_12 = 112
int_13 = 113
int_14 = 114
int_15 = 115
int_16 = 116
int_17 = 117
int_18 = 118
int_19 = 119
int_20 = 120
int_21 = 121
int_22 = 122
int_23 = 123
int_24 = 124
float_1 = 1.1
float_2 = 2.2
float_3 = 3.3
float_4 = 4.4
float_5 = 5.5
float_6 = 6.6
float_7 = 7.7
float_8 = 8.8
float_9 = 9.9
float_10 = 10.10
float_11 = 11.11
float_12 = 12.12

print("24 integer and 12 float, the call stack is larger than register space")

print("Correct call")
libc_interface.reorder_case_3(
    ctypes.c_int(int_1),
    ctypes.c_int(int_2),
    ctypes.c_int(int_3),
    ctypes.c_int(int_4),
    ctypes.c_int(int_5),
    ctypes.c_int(int_6),
    ctypes.c_int(int_7),
    ctypes.c_int(int_8),
    ctypes.c_int(int_9),
    ctypes.c_int(int_10),
    ctypes.c_int(int_11),
    ctypes.c_int(int_12),
    ctypes.c_int(int_13),
    ctypes.c_int(int_14),
    ctypes.c_int(int_15),
    ctypes.c_int(int_16),
    ctypes.c_int(int_17),
    ctypes.c_int(int_18),
    ctypes.c_int(int_19),
    ctypes.c_int(int_20),
    ctypes.c_int(int_21),
    ctypes.c_int(int_22),
    ctypes.c_int(int_23),
    ctypes.c_int(int_24),
    ctypes.c_float(float_1),
    ctypes.c_float(float_2),
    ctypes.c_float(float_3),
    ctypes.c_float(float_4),
    ctypes.c_float(float_5),
    ctypes.c_float(float_6),
    ctypes.c_float(float_7),
    ctypes.c_float(float_8),
    ctypes.c_float(float_9),
    ctypes.c_float(float_10),
    ctypes.c_float(float_11),
    ctypes.c_float(float_12),
)

print("Move float_1 to some random position above other floats, on C side, nothing changed")
libc_interface.reorder_case_3(
    ctypes.c_float(float_1),
    ctypes.c_int(int_1),
    ctypes.c_int(int_2),
    ctypes.c_int(int_3),
    ctypes.c_int(int_4),
    ctypes.c_int(int_5),
    ctypes.c_int(int_6),
    ctypes.c_int(int_7),
    ctypes.c_int(int_8),
    ctypes.c_int(int_9),
    ctypes.c_int(int_10),
    ctypes.c_int(int_11),
    ctypes.c_int(int_12),
    ctypes.c_int(int_13),
    ctypes.c_int(int_14),
    ctypes.c_int(int_15),
    ctypes.c_int(int_16),
    ctypes.c_int(int_17),
    ctypes.c_int(int_18),
    ctypes.c_int(int_19),
    ctypes.c_int(int_20),
    ctypes.c_int(int_21),
    ctypes.c_int(int_22),
    ctypes.c_int(int_23),
    ctypes.c_int(int_24),
    ctypes.c_float(float_2),
    ctypes.c_float(float_3),
    ctypes.c_float(float_4),
    ctypes.c_float(float_5),
    ctypes.c_float(float_6),
    ctypes.c_float(float_7),
    ctypes.c_float(float_8),
    ctypes.c_float(float_9),
    ctypes.c_float(float_10),
    ctypes.c_float(float_11),
    ctypes.c_float(float_12),
)

print("Move float_1 to float_9 to some random position above other floats, on C side, float_9 (9-th arguments or more) and integers get messed up")
libc_interface.reorder_case_3(
    ctypes.c_float(float_1),
    ctypes.c_float(float_2),
    ctypes.c_float(float_3),
    ctypes.c_float(float_4),
    ctypes.c_float(float_5),
    ctypes.c_float(float_6),
    ctypes.c_float(float_7),
    ctypes.c_float(float_8),
    ctypes.c_float(float_9),
    ctypes.c_int(int_1),
    ctypes.c_int(int_2),
    ctypes.c_int(int_3),
    ctypes.c_int(int_4),
    ctypes.c_int(int_5),
    ctypes.c_int(int_6),
    ctypes.c_int(int_7),
    ctypes.c_int(int_8),
    ctypes.c_int(int_9),
    ctypes.c_int(int_10),
    ctypes.c_int(int_11),
    ctypes.c_int(int_12),
    ctypes.c_int(int_13),
    ctypes.c_int(int_14),
    ctypes.c_int(int_15),
    ctypes.c_int(int_16),
    ctypes.c_int(int_17),
    ctypes.c_int(int_18),
    ctypes.c_int(int_19),
    ctypes.c_int(int_20),
    ctypes.c_int(int_21),
    ctypes.c_int(int_22),
    ctypes.c_int(int_23),
    ctypes.c_int(int_24),
    ctypes.c_float(float_10),
    ctypes.c_float(float_11),
    ctypes.c_float(float_12),
)
