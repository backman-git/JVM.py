
from thread import Thread
from stack import JvmStack, JVMFrame
from instructionFactory import InstructionFactory



class JVM:

    def __init__(self):
        self.runningThread=None
        self.threadStackSize=10
        #could optimizd for memory
        self.methodArea = {}
        self.iFactory=InstructionFactory()
        #tem
        self.mainClass=None
        self.constantPool ={}


    def run(self,jClass):

        #put a jClass inside it
        self.methodArea[jClass.className] = jClass
        self.constantPool[jClass.className] = jClass.constant_pool
        self.mainClass = jClass
        #entry point

        #generate a  main frame temp
        mainMethod = self.mainClass.getMethod("main")
        frame = JVMFrame(mainMethod,mainMethod.attributes[0].max_locals,mainMethod.attributes[0].max_stack)
        frame._localVars.setRef(0,"this")
        self.runningThread = Thread(frame)
        self.runThread(self.runningThread)

    #rethink a better way to put
    def getCurrentOpCode(self,frame,pc):
        method=frame.methodRef
        code = method.attributes[0].code
        return '0x{0:0{1}x}'.format((code[pc]),2)


    def runThread(self,thread):

        while 1:
            frame=thread.currentFrame()
            opcode = self.getCurrentOpCode(frame,thread.pc)
            #machine dependency
            instruction = self.iFactory.cookInstruction(opcode)
            instruction(frame,thread,self)