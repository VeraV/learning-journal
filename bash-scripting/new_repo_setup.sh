#!/bin/bash
echo '|---------------------------------------------|'
echo '|      Welcome to Setup New Repo Script!      |'
echo '|---------------------------------------------|'
echo -e "\nI'll do everything, just tell me some details:"

echo -e "\nName of your remote new repo, type 'quit' to exit::"
while read remote_repo_name
do
  if [[ "$remote_repo_name" == "quit" ]]; then
    echo "Bye!"
    exit 0
  else  
    remote_full_path="git@github.com:VeraV/$remote_repo_name.git"
    git ls-remote "$remote_full_path" &> /dev/null

    if [[ $? -eq 0 ]]; then
      echo "Got it!"
      break
    else
      echo "Nope. Repo not found. Try again ('quit' to exit):"
    fi
  fi  
done  


echo -e "\nLocal repo relative to home (e.g. Desktop/my-repo or Documents/projects/my-repo), type 'quit' to exit:"
while read local_path
do
  if [[ "$local_path" == "quit" ]]; then
    echo "Bye!"
    exit 0  
  else
    local_full_path="$HOME/$local_path"

    if [[ -d "$local_full_path" ]]; then
      echo "Got it!"
      break  
    else
      echo "Nope. No such directory on you computer. Try again ('quit' to exit): "  
    fi
  fi    
done     

# remote repo - empty, local - empty
# remote repo - empty, local - not empty
# remote repo - not empty, local - empty
# remote repo - not empty, local - not empty