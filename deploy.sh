#!/bin/bash

# Script to setup rENGex to be used by the quick command line function 'regex'

script_dir_path=$(dirname "$(readlink -f "$0")")
code_path="/code/rENGex.py"
absolute_path="$script_dir_path$code_path"

# Check if the script is being run from within the repository
if [ ! -f "$absolute_path" ]; then
    echo "Please run this script from within the repository."
    exit 0
fi

# Get the user's shell configuration file
if [ -n "$(zsh --version)" ]; then
    shellrc_file="$HOME/.zshrc"
else
    shellrc_file="$HOME/.bashrc"
fi

# Insert regex function into shell configuration file
cat <<EOF >> "$shellrc_file"

# Function to run rENGex, an interpreter from rENGex an english-regex hybrid, to regex.
function regex()  {
    $(which python3) $absolute_path \$@
}
EOF

echo "Setup complete"
echo "To use, restart your terminal, then type: regex '<input>'"
