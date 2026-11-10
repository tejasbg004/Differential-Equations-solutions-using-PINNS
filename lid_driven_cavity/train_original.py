"""Train Tejas's ORIGINAL lid-driven cavity PINN exactly as in PINNS.ipynb (cells 35-49),
with only the changes needed to run: Keras 3 import, the undefined `loss_bc` line removed,
no .h5 model saving. Saves the trained weights for comparison."""
import os, json
os.environ["KERAS_BACKEND"] = "tensorflow"
import numpy as np, tensorflow as tf, keras
from time import time
tf.random.set_seed(0); np.random.seed(0)
c = json.load(open('../PINNS.ipynb'))['cells']
g = {"tf": tf, "np": np, "keras": keras, "time": time}
for i in [35, 37, 39, 41, 43, 45, 47, 48]:
    exec(''.join(c[i]['source']), g)
src = ''.join(c[49]['source'])
src = src.replace("    histbc.append(loss_bc.numpy())\n", "")
src = src.rsplit("model.save('lid_driven_cavitys.h5')", 1)[0]   # stop before saving/plotting
exec(src, g)
g["model"].save_weights("weights/original_pinn_cavity.weights.h5")
print("saved original weights")
