# ---------------------
# This script automates the process of creating and switching to a new branch
# while ensuring the local master branch is up to date with the remote.
#
# Usage:
#   ./branch_workflow.sh <branch-name>
#
# The script will:
# 1. Fetch all remote changes
# 2. Switch to master branch
# 3. Pull latest changes from remote master
# 4. Delete all local branches except master
# 5. Create a new branch with the provided name
#
# Arguments:
#   branch-name: The name of the branch to create or checkout
#
# Example:
#   ./branch_workflow.sh feature/new-feature


#!/bin/bash
set -e

if [ $# -eq 0 ]; then
    echo "Error: Please provide a branch name as an argument"
    echo "Usage: $0 <branch-name>"
    exit 1
fi

BRANCH_NAME=$1

# Fetch all remote changes
echo "Fetching remote changes..."
git fetch --all

echo "Switching to master branch..."
git checkout master

echo "Deleting all branches except master..."
git branch | grep -v "master" | xargs git branch -D

# Pull latest changes from remote master
echo "Pulling latest changes from remote master..."
git pull origin master


git checkout -b "$BRANCH_NAME"
