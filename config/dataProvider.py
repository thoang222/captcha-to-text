import tensorflow as tf

from config.dataProvider1 import DataProvider as dataProvider1

class DataProvider(dataProvider1, tf.keras.utils.Sequence):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
