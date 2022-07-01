# GIT 

## Cloning the repository
```
git clone git@github.com:trivento/coding-guild-aws-hackathon-data.git
```

## Contribute

### Check your git profile

```
# show git config: user.email and user.name
git config  -l

# if needed, update globally:
git config --global user.email yourmail@yourdomain.com
git config --global user.name yourname

# or if needed, set for this repo only:
git config user.email yourmail@yourdomain.com
git config user.name yourname

# show git config: user.email and user.name
git config  -l
```

### Check your ssh identity

Git is using `$HOME/.ssh/id_rsa` as your default ssh identity for authentication.
The public key of this identity, stored in `$HOME/.ssh/id_rsa_pub`, should be uploaded to your github repo.

If your identity is in a different file, set the environment variable.
```
export GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa_example"
```

### Make a branch

```
# create and checkout
git branch new-feature-x
git checkout new-feature-x

# alternative - create and checkout
git checkout -b new-feature-x

# show current branch
git branch

# set as remote and push
git push --set-upstream origin new-feature-x

# delete
git branch -d new-feature-x
```

### Add code
```
git add yourfile.txt
git commit -m "new file"
git push
```

### Make pull request

Using the github web, create a pull request to merge your branch into main.
