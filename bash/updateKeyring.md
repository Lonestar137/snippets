Updating the apt keyring to trust a source.

### Auto recover key:

```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BE3E6EA534E8243F
```

#### TLDR

You can use this method if apt is complaining about some package key is missing. This would attempt to automatically download the key for you.

### Manual:

```bash
wget -o- https://hub.unity3d.com/linux/keys/public

file public

gpg --no-default-keyring --keyring ./unity_keyring.gpg --import public

gpg --no-default-keyring --keyring ./unity_keyring.gpg --export > ./unity-archive-keyring.gpg

sudo mv ./unity-archive-keyring.gpg /etc/apt/trusted.gpg.d/

sudo apt update

sudo apt-get install unityhub
```

#### TLDR:

Basically, download the key, check the file, prepare to import the key, move the key, update the repo, install the hub.
