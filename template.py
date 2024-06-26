import os
from pathlib import Path

list_of_files = [
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    "src/mongodb_connect/__init__.py",
    "src/mongodb_connect/mongo_crud.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/training_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/int.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "pyproject.toml",
    "setup.py",
    "setup.cfg",
    "tox.ini",
    "experiment/experiments.ipynb"

]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    if filedir != "":
        try:
            os.makedirs(filedir,exist_ok=True)
        except Exception as e:
            print("The creation of folder failed: {}".format(e))
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) > 0):
        with open(filepath,"w") as f:
            pass # create an empty file