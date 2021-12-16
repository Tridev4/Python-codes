import os
def filecopy(file1,file2):
    f1=open(file1,'r')
    f2=open(file2,'w')
    line=f1.readline()
    while line!='':
        f2.write(line)
        line=f1.readline()
    f1.close()
    f2.close()
def main():
    fileName1=input('Enter the source file name:')
    fileName2=input('Enter the destination file name:')
    filecopy(fileName1,fileName2)
if __name__=='__main__':
    main()