# new_repo_setup.sh

A Bash script that automates connecting a new local folder to a new GitHub repository — handling all the fiddly git commands and edge cases so you don't have to remember the sequence.

## Problem it solves

Every time you create a new project you need to connect a local folder to a GitHub repo. The sequence of commands changes depending on whether each side already has files or not — and getting it wrong leads to confusing git errors. This script detects the state of both sides and runs the correct sequence automatically.

## What it covers

| Local     | Remote    | What the script does                                                    |
| --------- | --------- | ----------------------------------------------------------------------- |
| Empty     | Empty     | Connects repos, ready for your first commit                             |
| Not empty | Empty     | Commits local files and pushes to remote                                |
| Empty     | Not empty | Clones remote directly into local folder                                |
| Not empty | Not empty | Commits local, fetches remote, merges — or guides you through conflicts |

## Requirements

- macOS or Linux
- Bash
- SSH key configured for GitHub ([GitHub SSH setup guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh))
- Git installed

## Setup

1. Download or copy `new_repo_setup.sh` to your machine
2. Grant execute permission:

```bash
chmod u+x new_repo_setup.sh
```

## How to use

1. Create your new repo on GitHub (with or without initial files)
2. Create your local folder (with or without files)
3. Run the script from anywhere:

```bash
./new_repo_setup.sh
```

4. When prompted enter:
   - Your GitHub repo name (just the name, not the full URL)
   - Your local folder path relative to home (e.g. `Desktop/my-project`)

## Example

```
|--------------------------------------------|
|     Welcome to Setup New Repo Script!      |
|--------------------------------------------|

I'll do everything, just tell me some details:

Name of your remote new repo, type 'quit' to exit:
my-new-project
Got it!

Local repo relative to home (e.g. Desktop/my-repo), type 'quit' to exit:
Desktop/my-new-project
Got it!

Initialized empty Git repository...
[main (root-commit)] init commit
...
✅ All done! Repo connected successfully.
```

## Conflict handling

If both local and remote have the same file with different content, Git will detect a conflict and the script will stop gracefully with instructions:

```
⚠️  Conflicts detected! Conflicted files:
README.md

Please resolve conflicts manually:
1. Open the files listed above and fix the conflicts
2. Run: git add .
3. Run: git commit
4. Run: git push -u origin main
```

Everything the script already did (git init, remote connection, fetch) remains intact — just resolve the conflicts and follow the printed steps.

## Constraints

- **SSH only** — script uses SSH format (`git@github.com`). HTTPS not supported.
- **Username is hardcoded** — the GitHub username `VeraV` is hardcoded in the script. Edit line 10 to change it to your own username.
- **Main branch only** — always uses `main` as the branch name.
- **New repos only** — designed for first-time connection of a local folder to a remote repo. Not intended for repos that are already connected.
- **Home-relative paths** — local path must be entered relative to your home directory (e.g. `Desktop/project` not `/Users/vera/Desktop/project`).
- **Single level of conflict handling** — if merge conflicts occur the script exits and hands control to the user. It does not attempt auto-resolution.

## What it does NOT do

- Create the GitHub repo for you (do this manually on GitHub first)
- Handle existing git remotes (run on folders with no prior `git init`)
- Support multiple branches
- Support HTTPS authentication
