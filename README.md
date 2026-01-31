This is my RICE.

# Fonts Configurations
1. The Fonts I use:
	1. Noto Sans
	2. Noto Serif
	3. Noto Sans Arabic
	4. Noto Kufi Arabic
	5. Noto Naskh Arabic
	6. Roboto
	7. Fira Code
	8. FiraCode Nerd Font
2.  1 - 7 Can be downloaded from google [Google Fonts](https://fonts.google.com/).
3. The last one can be downloaded from [Nerd Fonts](https://www.nerdfonts.com/font-downloads).
4. Install all the fonts any way you want(e.g. export all zip files and cp the content into ~/.local/share/fonts directory).
5. Clone the repo for config files:
   ``` bash 
	git clone https://github.com/z-systemz/z-linux.git && cd z-systemz
   ```
6. Use the Font configs for both user and system wide:
	``` bash
	cp -r fonts/fontconfig/ ~/.config/
	cp fonts/local.conf /etc/fonts/ 
	```
7. Install zsh shell.
8. Install [OH-MY-ZSH](https://ohmyz.sh/).
9. Install [Starship](https://starship.rs/) prompot.
10. Copy .zshrc config file into home directory:
 	``` bash
	cp ./.zshrc ~/
	```
11. Install [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions).
12. Install [wezterm](https://wezterm.org/).
13. Copy .wezterm.lua config file into your home directory:
	``` bash
	cp ./.wezterm.lua ~/
	```


