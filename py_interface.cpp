#include "py_interface.h"
#include <iostream>
//g++ -c -fPIC py_interface.cpp -o py_interface.o -D_LINUX_
//g++ -shared -Wl,-soname,py_interface.so -o py_interface.so py_interface.o
py_interface::py_interface(){
    val = 0;
}
void py_interface::func1() {
    printf("fdsa");
}
void py_interface::func2(int v) {

}
int py_interface::func3() {
    return 3;
}
int py_interface::func4(int v) {
    return 4;
}

extern "C" __declspec(dllexport) py_interface * init(int n) { return new py_interface(); }
extern "C" __declspec(dllexport) void f1(py_interface* ins) { ins->func1(); }
extern "C" __declspec(dllexport) void f2(py_interface * ins, int v) { ins->func2(v); }
extern "C" __declspec(dllexport) int f3(py_interface * ins) { return ins->func3(); }
extern "C" __declspec(dllexport) int f4(py_interface * ins, int v) { return ins->func4(v); }



