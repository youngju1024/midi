from magenta.scripts.convert_dir_to_note_sequences import convert_directory

output = 'dataset.tfrecord'

convert_directory('midi/',output,recursive=True)