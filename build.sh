g++ -c -fPIC py_interface.cpp -o py_interface.o -D_LINUX_
g++ -shared -Wl,-soname,py_interface.so -o py_interface.so py_interface.o