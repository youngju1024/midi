import tensorflow as tf
import note_seq 

from magenta.models.music_vae import configs,trained_model


model = trained_model.TrainedModel(config=configs.CONFIG_MAP['groovae_4bar'],batch_size=1,checkpoint_dir_or_path='train_50000/') 

generated_sequence = model.sample(n=10, length=16*4,temperature=1.)
for i in range(10):
    note_seq.sequence_proto_to_midi_file(generated_sequence[i], 'drum_4bar_' + str(i) +'.mid')