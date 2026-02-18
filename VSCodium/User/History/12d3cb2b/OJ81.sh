#!/bin/bash

sudo pacman -S --needed base-devel rustup
rustup default stable
git clone https://aur.archlinux.org/paru.git
cd paru
makepkg -si