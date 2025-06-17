import os
from datetime import date

# Mongo DB constants
DATABASE_NAME = "Proj1"
COLLECTION_NAME = "Proj1-Data"
MONGODB_URI_KEY = "mongodb+srv://abhisekmaharana9861:cpVT83E59WyecGzA@vi-processing.zxpbuvh.mongodb.net/?retryWrites=true&w=majority&appName=vi-processing"

PIPELINE_NAME: str = ""
ARTIFACTS_DIR: str = "artifact"


MODEL_FILE_NAME: str = "rf_model.pkl"

TARGET_COLUMN: str = "Response"
CURRENT_YEAR: str = date.today().year


PREPROCESSING_OBJECT_FILE_NAME: str = "preprocessing.pkl"

FILE_NAME = "data.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

AWS_ACCESS_KEY_ID_ENV_KEY = "AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY = "AWS_SECRET_ACCESS_KEY"

REGION_NAME = "us-east-1"



"""
Data Ingestion related constants start with `DATA_INGESTION' VAR NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_REPORT_FILE_NAME: str = "report.yaml"

"""
Data Transformation related constants start with `DATA_TRANSFORMATION' VAR NAME
"""

DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRASFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRASFORMED_OBJECT_DIR: str = "transformed_object"

"""
Model Trainer related constants start with `DATA_TRANSFORMATION' VAR NAME
"""

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR: str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME: str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE: float = 0.6
MODEL_TRAINER_MODEL_CONFIG_FILE_PATH: str = os.path.join("config", "model.yaml")
MODEL_TRAINER_N_ESTIMATORS: int = 100
MODEL_TRAINER_MIN_SAMPLES_SPLIT: int = 7
MODEL_TRAINER_MIN_SAMPLES_LEAF: int = 6
MIN_SAMPLES_SPLIT_MAX_DEPTH: int = 10
MIN_SAMPLES_SPLIT_CRITERION: str = 'entropy'
MIN_SAMPLES_SPLIT_RANDOM_STATE: int = 101

"""
Model Evaluation related constants start with `DATA_TRANSFORMATION' VAR NAME
"""
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE: float = 0.01
MODEL_BUCKET_NAME: str = "my-model-mlopsproj"
MODEL_PUSHER_S3_KEY: str = "model-registry"

APP_HOST = "0.0.0.0"
APP_PORT = 5000