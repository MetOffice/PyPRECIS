FROM continuumio/miniconda3

RUN apt-get update

# Set working directory for the project
WORKDIR  /app

SHELL ["/bin/bash", "--login", "-c"]

RUN apt-get install -y git

# Create Conda environment from the YAML file
COPY environment.yml .
RUN pip install --upgrade pip

RUN conda env create -f environment.yml

RUN conda init bash
RUN conda activate pyprecis-environment

RUN pip install ipykernel && \
    python -m ipykernel install --name pyprecis-training

