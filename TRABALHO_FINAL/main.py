import os
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

# Verifica as GPUs disponíveis
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"GPUs disponíveis: {len(gpus)}")
    for gpu in gpus:
        print(f" - Nome: {gpu.name}, Tipo: {gpu.device_type}")
else:
    print("Nenhuma GPU disponível")