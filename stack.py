



class LocalVars():

    def __init__(self,size):
        self._varListLen = size
        self._varList=[None]*self._varListLen

    def setInt(self,idx,intValue):
        self._varList[idx] = intValue

    def getInt(self,idx):
        return self._varList[idx]

    def setRef(self,idx,refValue):
        self._varList[idx] = refValue

    def getRef(self,idx):
        return self._varList[idx]

    def getThis(self):
        return self.getRef(0)


class OPStack():

    def __init__(self,size):
        self.size =size
        self.stack =[]


    def pushInt(self,value):
        if len(self.stack) > self.size :
            raise Exception("OPStack overflow")
        self.stack.append(value)

    def popInt(self):
        v=self.stack.pop()
        return v

    def pushRef(self,value):
        if len(self.stack) > self.size :
            raise Exception("OPStack overflow")
        self.stack.append(value)


    def popRef(self):
        v=self.stack.pop()
        return v

    def pop(self):
        v = self.stack.pop()
        return v

    def push(self,value):
        self.stack.append(value)

class JVMFrame():

    def __init__(self,methodRef,localVarsSize,localOPStackSize):
        self.methodRef = methodRef
        self._localVarsSize =localVarsSize
        self._localOPStackSize=localOPStackSize
        self._localVars= LocalVars(self._localVarsSize)
        self._opStack= OPStack(self._localOPStackSize)


class JvmStack():

    def __init__(self,frameSize):
        self.frames=[]
        self._frameSize=frameSize


    def push(self,frame):
        self.frames.append(frame)

    def pop(self):
        return self.frames.pop()