import os
from datetime import datetime


ROOT_DIR = 'c:\\Users\\91973\\Downloads\\ML_Projects\\Machine-Learning-Project'

CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME)

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

#Training pipeline related variables

TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"

