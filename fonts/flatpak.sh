#!/bin/bash

# Script to link ~/.config/fontconfig into all ~/.var/app/* config folders

for app_dir in ~/.var/app/*; do
    ln -s ~/.config/fontconfig $app_dir/config/fontconfig
done

echo "Done."