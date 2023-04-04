from magenta.models.music_vae import music_vae_train, configs
import tensorflow.compat.v1 as tf

tf.disable_eager_execution()
flags = tf.app.flags
FLAGS = flags.FLAGS

FLAGS.config = 'groovae_4bar'
FLAGS.num_steps = 50000
FLAGS.cache_dataset = True
FLAGS.run_dir = 'train_50000/'
FLAGS.examples_path = 'dataset.tfrecord'

music_vae_train.run(configs.CONFIG_MAP)