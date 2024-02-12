from os import listdir
from os.path import isfile, join
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new ChatBot instance
chatbot = ChatBot('MyChatBot')

# Step 1: Train the ChatBot on multiple YAML files in a folder
def train_chatbot(folder_path):

    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)

    # Get a list of all YAML files in the specified folder
    yaml_files = [join(folder_path, f) for f in listdir(folder_path) if isfile(join(folder_path, f)) and f.endswith('.yml')]

    # Train the chatbot on each YAML file
    for yaml_file in yaml_files:
        trainer.train(yaml_file)


# Specify the folder containing your training YAML files and where to save the model
training_folder_path = 'SparkMate_convoCraft_app\data\generalTrainingData'

# Call the function to train and save the model
train_chatbot(training_folder_path)


