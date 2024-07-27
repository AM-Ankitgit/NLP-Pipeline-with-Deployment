import os

project_name = "hate"
from pathlib import Path

list_of_folder =[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/aws_cloud.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/train_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/ml/__init__.py",
    f"{project_name}/ml/model.py",
    "app.py",
    "requirement.txt",
    "Dockerfile",
    "setup.py",
    ".dockerignore"
]



for file in  list_of_folder:
    full_path = Path(file)
    filedir,filename = os.path.split(full_path)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)

    if not os.path.exists(full_path) or os.path.getsize(full_path)==0:
        with open(full_path,'w') as f:
            pass
    

