#coding = utf-8
import os
import shlex, subprocess


def main():
    path = os.getcwd()

    vttName = []                                     

    for i in os.listdir(path):
        name = i.split('.')
        if name[-1] == 'vtt':
            vttName.append(i)

    for vttname in vttName:
        vtt = open(path + "\\" + vttname)
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
        srtName = vttname.split('.')

        subprocess.call(['ffmpeg', '-i', vttname, srtName[0] + '.srt'])

    pass

main()

