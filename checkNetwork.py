import os

if not os.path.exists('network.flag'):
    os.system('tapinstall.exe install OemVista.inf tap0901')
    f = open('network.flag','w')
    f.write('network is install')
    f.close()
