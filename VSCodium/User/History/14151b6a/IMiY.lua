-- Pull in the wezterm API
local wezterm = require 'wezterm'

-- This will hold the configuration.
local config = wezterm.config_builder()

-- This is where you actually apply your config choices.

-- For example, changing the initial geometry for new windows:
config.initial_cols = 120
config.initial_rows = 28
config.hide_tab_bar_if_only_one_tab = true
config.window_background_opacity = 0.85
config.enable_wayland = false
-- or, changing the font size and color scheme.
config.font_size = 16
config.font =
  wezterm.font('JetBrainsMono Nerd Font', { weight = 'Medium'})

--config.color_scheme = 'Everforest Dark (Gogh)'
config.color_scheme = 'Rosé Pine Moon (Gogh)'
-- Finally, return the configuration to wezterm:
return config
