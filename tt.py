import ctypes
import sys
import zlib

libfile="./py_interface" +(".dll" if(sys.platform=="win32") else ".so")
lib = ctypes.cdll.LoadLibrary(libfile)

class Sim(object):
	def __init__(self):
		self.obj = lib.init()
		#self.setFuncType(lib.init,[[ctypes.c_void_p],None])
		self.setFuncType(lib.f1,[[ctypes.c_void_p],None])
		#self.setFuncType(lib.init,[[ctypes.c_void_p],None])
		#self.setFuncType(lib.init,[[ctypes.c_void_p],None])
		self.idls=dict()
		

	def setFuncType(self,func,types):
		func.artypes, func.restype=types

	def bar(self):
		lib.f1(self.obj)


if __name__ == "__main__":
	f=Sim()
	f.bar()
	