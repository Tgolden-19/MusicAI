#from magenta.scripts import convert_dir_to_note_sequences
import tensorflow as tf
#from magenta.models.melody_rnn import melody_rnn_create_dataset
#import magenta.models.melody_rnn.melody_rnn_train
from magenta.models.melody_rnn import melody_rnn_generate
#from magenta.models.performance_rnn import performance_model

source_folder = './classical_music_database' #input('Enter the path of the midi files.')#current value of file was local dataset locations and names. if person locations are preffered uncomment input line and delete preset value
out_file = './classical_test_dataset.tfrecord'#input('Enter the path for the output sequence training file:')#current value of file was local dataset locations and names. if person locations are preffered uncomment input line and delete preset value
run_directory='./AIVersionsMelody'
training_file_dest = '/home/student/MusicAI/output_datasets_melody'
training_file ='/home/student/MusicAI/output_datasets_melody/training_melodies.tfrecord' #'/home/student/magenta_test_output/training_performances.tfrecord'
gen_out = '/home/student/MusicAI/generate_output_melody'
encoder = 'key'

#the first None arg is usually the python file name
args = [None, '--input_dir', source_folder, '--output_file', out_file]
#tf.app.run(convert_dir_to_note_sequences.main, args)#uncomment if midi files need to be converted to usable data(1)
to_dataset_args = [None, '--input', out_file, '--output_dir', training_file_dest, '--melody_encoder_decoder', encoder]
#tf.app.run(melody_rnn_create_dataset.main, to_dataset_args)

train_args = [None, '--run_dir', run_directory, '--sequence_example_file', training_file, '--melody_encoder_decoder', encoder]#, '--num_training_steps', "10", '--num_eval_examples', '10']
#training algorithim
def train():
    for i in range(0, 200):
        try:
            #tf.app.run(magenta.models.melody_rnn.melody_rnn_train.main, train_args)
            print("Done!")
        except Exception as err:
            print(err)
        print(i)
#train()


generator_args =[None, "--run_dir", run_directory, '--output_dir', gen_out, '--num_outputs', '3', '--num_steps', '1000', '--temperature', '1.0', '--melody_encoder_decoder', encoder]
tf.app.run(melody_rnn_generate.main, generator_args)#run generator based on models in AI folder







