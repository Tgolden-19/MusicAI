from magenta.models.shared import events_rnn_graph
#from magenta.scripts import convert_dir_to_note_sequences
#import magenta.models.performance_rnn.performance_sequence_generator
import tensorflow as tf
#from magenta.models.performance_rnn import performance_rnn_create_dataset
#import magenta.models.performance_rnn.performance_rnn_train
from magenta.models.performance_rnn import performance_rnn_generate
#from magenta.protobuf import generator_pb2
#from magenta.protobuf import music_pb2
#import magenta.music as mm
from magenta.models.performance_rnn import performance_model

source_folder = './classical_music_database' #input('Enter the path of the midi files.')#current value of file was local dataset locations and names. if person locations are preffered uncomment input line and delete preset value
out_file = './performance_dataset.tfrecord'#input('Enter the path for the output sequence training file:')#current value of file was local dataset locations and names. if person locations are preffered uncomment input line and delete preset value
run_directory='./AIVersionsPerformance'
training_file_dest = '/home/student/MusicAI/output_datasets_performance'
training_file ='/home/student/MusicAI/output_datasets_performance/training_performances.tfrecord' #'/home/student/magenta_test_output/training_performances.tfrecord'
gen_out = '/home/student/MusicAI/generate_output_performance'

#the first None arg is usually the python file name
args = [None, '--input_dir', source_folder, '--output_file', out_file]
#tf.app.run(convert_dir_to_note_sequences.main, args)#uncomment if midi files need to be converted to usable data(1)
to_dataset_args = [None, '--input', out_file, '--output_dir', training_file_dest]
#tf.app.run(performance_rnn_create_dataset.main, to_dataset_args)

train_args = [None, '--run_dir', run_directory, '--sequence_example_file', training_file]#, '--num_training_steps', "10", '--num_eval_examples', '10']
#training algorithim
def train():
    for i in range(0, 200):

        try:
            #tf.app.run(magenta.models.performance_rnn.performance_rnn_train.main, train_args)
            print("Done!")
        except Exception as err:
            print(err)
        print(i)
#train()


generator_args =[None, "--run_dir", run_directory, '--output_dir', gen_out, '--num_outputs', '1', '--num_steps', '3000', '--temperature', '1.2']
tf.app.run(performance_rnn_generate.main, generator_args)#run generator based on models in AI folder







