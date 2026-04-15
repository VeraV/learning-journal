#!/bin/bash
export GIT_PAGER=cat
echo '|---------------------------------------------|'
echo '|      Welcome to Setup New Repo Script!      |'
echo '|---------------------------------------------|'
echo -e "\nI'll do everything, just tell me some details:"

echo -e "\nName of your remote new repo, type 'quit' to exit:"
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
      echo "Repo not found. Try again ('quit' to exit):"
    fi
  fi  
done  


echo -e "\nLocal repo relative to home (e.g. Desktop/my-repo), type 'quit' to exit:"
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
      echo "No such directory on you computer. Try again ('quit' to exit):"  
    fi
  fi    
done    


# if repo has commits captures the SHA hash 
# captures empty string "" if repo is empty
remote_head=$(git ls-remote "$remote_full_path" HEAD)
if [[ -z "$remote_head" ]]; then
    remote_is_empty=true
else
    remote_is_empty=false
fi

# ignores folders themselves, count lines (= files)
file_count=$(find "$local_full_path" -type f | wc -l | tr -d ' ')
if [[ $file_count -eq 0 ]]; then
    local_is_empty=true
else
    local_is_empty=false
fi



cd "$local_full_path"

# local - empty, remote - no
if [[ $local_is_empty == true && $remote_is_empty == false ]]; then
  git clone "$remote_full_path" .
else
  git init
  git remote add origin "$remote_full_path"
  git branch -M main

  if [[ $local_is_empty == false ]]; then
    git add .
    git commit -m "init commit"

    if [[ $remote_is_empty == false ]]; then
      git fetch origin
      git merge origin/main --allow-unrelated-histories --no-edit

      #if unresolved conflicts happened
      if [[ $? -ne 0 ]]; then
        echo -e "\n⚠️  Conflicts detected! Conflicted files:"
        git diff --name-only --diff-filter=U
        echo -e "\nPlease resolve conflicts manually:"
        echo "1. Open the files listed above and fix the conflicts"
        echo "2. Run: git add ."
        echo "3. Run: git commit"
        echo "4. Run: git push -u origin main"
        exit 1
      fi
    fi
    
    git push -u origin main
  fi  
fi

echo -e "\n✅ All done! Repo connected successfully."

# NOTES:
# git ls-tree origin/main --name-only — lists all files in the remote main branch after fetch
# grep "^\.gitignore$" — looks for exactly .gitignore
# ^ means start of line, $ means end — so it matches exactly, not partial names
# git diff --name-only --diff-filter=U — lists only the conflicted files (U = unmerged)
# exit 1 — stops the script so the user can go fix things manually
# tr -d ' ' - cut the spaces, bcz on MacOS wc -l returns number with spaces before to align numbers visually



