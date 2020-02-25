#Simple centos container with GNU tools

Stage0 += baseimage(image='centos:7')
Stage0 += gnu()
