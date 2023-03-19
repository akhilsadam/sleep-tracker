import numpy as np
import io,sys,os

# patient IDs:
def configure(path_idfile):
    if(os.path.exists(path_idfile)):
        ids = np.loadtxt(path_idfile).astype(int)
    else:
        ids = np.array([int(ul.subtract(path.name,path_file[0])) for path in Path(path_data).rglob(star+path_file[0])])
        np.savetxt(path_idfile,ids,fmt='%i')
    return ids

def dataloadC(pf,id_in,pl):
    hr = np.genfromtxt(pf+str(id_in)+pl, dtype=float, delimiter=",")
    hr = hr[hr[:, 0].argsort()]
    return hr

def dataloadS(pf,id_in,pl):
    hr = np.genfromtxt(pf+str(id_in)+pl, dtype=float, delimiter=" ")
    hr = hr[hr[:, 0].argsort()]
    return hr