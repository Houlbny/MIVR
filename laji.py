import nrrd
import numpy as np

label_path = './17/17mmm.nrrd'
clean_path = './17/17_clean2.nrrd'

label_array, _ = nrrd.read(label_path)
label_array_np = np.array(label_array,dtype=float)

clean_array, _ = nrrd.read(clean_path)
clean_array_np = np.array(clean_array,dtype=float)

label_array_np_fan = (label_array_np == False)

merge = clean_array_np * label_array_np_fan

nrrd.write('./17/tttmerge.nrrd', merge)
