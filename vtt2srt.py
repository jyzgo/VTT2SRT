#coding = utf-8
import os
import shlex, subprocess
import sys, getopt


def main(argv):

    
    # print('path is ' + argv[0]);
    path = "";
    if(len(argv) == 0):
      path = os.getcwd()
    else:
      path = os.getcwd() + "\\" + argv[0]

    
    if(not os.path.isdir(path)):
        print(path  + " is not a dir")
        return


    vttName = []                                     

    for i in os.listdir(path):
        name = i.split('.')
        if name[-1] == 'vtt':
            vttName.append(i)

    for vttname in vttName:
        vtt = open(path  + vttname)
        filevtt = vtt.read()
        vtt.close()
        #print filevtt
        listvtt = filevtt.split('.')
        #print listvtt
        #print listvtt[0][8:]
        strvtt = listvtt[0][7:]
        for i in range(1 , len(listvtt) ):
            strvtt = strvtt + "," + listvtt[i]
        
        #print strvtt
        # srtName = vttname.split('.')

        if vttname.endswith('.vtt'):
            srtName = vttname[:-4]
        else:
            srtName = vttname.split('.')[0]

        subprocess.call(['ffmpeg', '-i', path + vttname, path + srtName + '.srt'])

    pass

if __name__ == "__main__":
 main(sys.argv[1:])

