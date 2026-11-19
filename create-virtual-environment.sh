# Acknowledge terms
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

# Create the environment
conda create -n pdf-tools python=3.13 -y


# Activate it
#conda init 
#conda activate pdf-tools