# -*- coding: utf-8 -*-
"""
------------------------------
 @Date    : 2022/6/30 上午9:51
 @Author  : Cristiano Ronalda
------------------------------
"""
import subprocess

def cmd(command):
    subp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    subp.wait(3)
    if subp.poll() == 0:
        return subp.communicate()[1]
    else:
        return


if __name__ == '__main__':
    cmd("java -version")
