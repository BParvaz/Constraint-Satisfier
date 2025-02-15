#!/bin/sh

gitRemote="base"
gitUrl="https://gitlab.cs.man.ac.uk/a21674fl/comp24011_2024_labs.git"
gitBranch="lab2"

set -e
git remote remove "$gitRemote" 2>/dev/null || true
git remote add "$gitRemote" "$gitUrl"
git config checkout.defaultRemote origin
git fetch "$gitRemote"
git merge "$gitRemote/$gitBranch"

# vim:set et sw=2 ts=2:
