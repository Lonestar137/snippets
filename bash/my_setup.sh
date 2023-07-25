
rustCoreUtilUpgrades(){
  # rust shell  (nushell)
  nu

  # ls rust replacement
  exa

  # Rust compilation cache(saves time on comp)s
  # dont forget to set, RUSTC_WRAPPER="/path/to/binary/sccache"
  sccache

  # Rust du util (cargo install du-dust)
  dust

  # Rust cat replacement
  bat

  # zellij (tmux replacement)
  zellij

  # mprocs like tmux but optimized for long running commands/processes I.e. databases etc. . .
  mprocs

  # ripgrep, combines find and grep(very fast)
  ripgrep

}

rustDevelopmentToolUpgrades(){
  # cargo install bob-nvim, neovim version manager
  bob install {the neovim version you want}

  # lazygit replacement(cargo install gitui)
  gitui
  
  # irust, interactive rust(cargo install irust)
  irust

  # bacon, refreshes your build automatically, must have for rust dev
  bacon

}

rustApplicationReplacements(){
  # Spotify CLI 
  ncspot

  # porsmo, CLI pomodoro timer
  porsmo
  
  # wiki-tui, cli wikipedia (cargo )
  wiki-tui

  # rtx-cli, runtime manager for lots of languages like Python
  # asdf rust clone
  rtx
}

pythonApplications(){
  # todo app, pip3 install pls-cli
  pls

}

applications(){
  # dual pane, vim file manager(amazing)
  vifm

  # blueman, for bluetooth management.
  # Bluetooth Manager  in rofi.
  # CLI bluetooth:
  bluetoothctl

  # mounting external drives
  # apt install udisks2
  lsblk # get devicename
  udisksctl mount -b {{device_name}} # i.e. /dev/sdb2

}

encryptedPartitions(){
  # I use LUKS encryption
  creation(){
    sudo apt install cryptsetup
    sudo fdisk /dev/sdaX # or gparted, however you make your partitions.
    sudo cryptsetup luksFormat /dev/sdX1 # or whatever partition number you want 
    sudo cryptsetup luksOpen /dev/sdX1 my_crypted_drive_name
    sudo mkfs.ntfs /dev/mapper/my_crypted_drive_name # mkfs.ext4 is also an option.
    sudo mkdir /mnt/my_crypted_drive_name
    sudo mount /dev/mapper/my_crypted_drive_name /mnt/my_crypted_drive_name
  }

  mounting(){
    # don't forget to unmount
    sudo cryptsetup luksOpen /dev/sdX1 my_crypted_drive_name
    sudo mount /dev/mapper/my_crypted_drive_name /mnt/my_crypted_drive_name
  }

  unmounting(){
    sudo umount /mnt/my_crypted_drive_name
    sudo cryptsetup luksClose my_crypted_drive_name
  }

}



