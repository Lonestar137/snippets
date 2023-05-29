
rustCoreUtilUpgrades(){
  # rust shell  (nushell)
  nu

  # ls rust replacement
  exa

  # Rust compilation cache(saves time on comp)s
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



