
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
