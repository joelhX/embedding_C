#ifdef _LINUX_
#define __declspec(dllexport)
#endif

class py_interface {
public:
	py_interface();
	void func1();
	void func2(int);
	int func3();
	int func4(int);

private:
	int val;
};
