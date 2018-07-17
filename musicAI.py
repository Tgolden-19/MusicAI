from absl import app
#import magenta.scripts.convert_dir_to_note_sequences
import magenta.models.performance_rnn.performance_sequence_generator
import tensorflow as tf
import magenta.models.performance_rnn.performance_rnn_train
import os
from magenta.models.performance_rnn import performance_sequence_generator
from magenta.protobuf import generator_pb2
from magenta.protobuf import music_pb2

import magenta.music as mm


source_folder = 'C:\\Users\\iD Student\\PycharmProjects\\MusicAI\\midiFiles' #input('Enter the path of the midi files.')
out_file = 'C:\\Users\\iD Student\\PycharmProjects\MusicAI\\large_dataset_test.tfrecord'#input('Enter the path for the output sequence training file:')
#the first None arg is usually the python file name
args = [None, '--input_dir', source_folder, '--output_file', out_file]



#app.run(magenta.scripts.convert_dir_to_note_sequences.main, args)

run_directory='C:\\Users\\iD Student\\PycharmProjects\\MusicAI\\AIVerisions'
train_args = [None, '--run_dir', run_directory, '--sequence_example_file', out_file]
app.run(magenta.models.performance_rnn.performance_rnn_train.main, train_args)

#generator = magenta.models.performance_rnn.performance_sequence_generator
#gen_map = generator.get_generator_map()
