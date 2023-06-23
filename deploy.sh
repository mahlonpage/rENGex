#!/bin/bash

script_path="./code/rENGex.py"

# Check if the script is being run from within the repository
if [ -f "$script_path" ]; then
    # Get the user's shell configuration file
    shellrc_file="$HOME/.bashrc" # Default to bashrc
    if [ -n "$ZSH_VERSION" ]; then
        shellrc_file="$HOME/.zshrc" # Use zshrc if running in Zsh
    fi
    echo "alias regex='$(which python3) $script_path \$@'" >> "$shellrc_file"
    echo "Setup complete"
    echo "To use, restart your terminal, then type: regex '<input>'
else
    echo "Please run this script from within the repository."
fi