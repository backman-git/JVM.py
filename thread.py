
from stack import JvmStack, JVMFrame

class Thread :

	def __init__(self,initFrame):
		self._pc=0
		self._stack = []
		self.pushFrame(initFrame)

	@property
	def pc(self):
		return self._pc

	@pc.setter
	def pc(self,value):
		self._pc = value

	def currentFrame(self):
		return self._stack[-1]

	def pushFrame(self,frame):
		self._stack.append(frame)

	def popFrame(self):
		return self._stack.pop()

	def invokeMethod(self,methodRef):
		frame =JVMFrame(methodRef,methodRef.attributes[0].max_locals,methodRef.attributes[0].max_stack)
		frame._localVars.setRef(0,"this")
		self.pushFrame(frame)


