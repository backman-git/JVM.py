
from jvm import JVM
import sys
from classFileLoader import ClassFileLoader





def main():


# file load
	path = "./java/Test.class"
	jClass=ClassFileLoader.load(path)
	jvm=JVM()
	jvm.run(jClass)


main()