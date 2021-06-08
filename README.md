# Research Paper - Tabular Data Augmentation

Part of my research paper on tabular data augmentation, I applied different data augmentation algorithms on four different datasets in an attempt to increase the performance of classification algorithms. 

More specifically, I increased the size of the minority classes only using the following algorithms:
- SMOTE
- Gaussian Copula
- Variational Autoencoder
- CTGAN
- TGAN

## Launch Project

To launch the project, you will need to create two different environments:
- **Environment n°1**: works with all algorithms except for TGAN, therefore only the notebook `noTGAN.ipynb` will execute
 ```  
 # Create virtual environment
 python3 -m venv notgan_env
# Activate the virtual environment
source notgan_env/bin/activate
# Install dependencies
pip install -r requirements_notgan.txt
 ```

- **Environment n°2**: specific environment for the TGAN algorithm, therefore only the notebook `TGAN.ipynb` will execute
 ```  
 # Create virtual environment
 python3 -m venv tgan_env
# Activate the virtual environment
source tgan_env/bin/activate
# Install dependencies
pip install -r requirements_tgan.txt
 ```

## Sources

To carry out this project, the following sources were used
- https://github.com/sdv-dev/TGAN
- https://github.com/sdv-dev/SDV
- https://github.com/sdv-dev/Copulas

## Authors

Arthur Krieff
