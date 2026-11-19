# 1. Download the installer script
curl -fsSL -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# 2. Run the installer in batch mode (-b accepts defaults, -p defines installation path)
bash Miniconda3-latest-Linux-x86_64.sh -b -p "$HOME/miniconda3"

# 3. Initialize your shell (bash and/or zsh)
"$HOME/miniconda3/bin/conda" init bash
"$HOME/miniconda3/bin/conda" init zsh

# 4. Clean up the installer script
rm Miniconda3-latest-Linux-x86_64.sh