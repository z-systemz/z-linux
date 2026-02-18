if status is-interactive
    # Commands to run in interactive sessions can go here
    function fish_greeting

    end
    starship init fish | source
    fastfetch -l arch_small -c examples/13.jsonc

    fish_config theme choose "Rosé Pine Moon Auto"

    function mkcd
        mkdir -p $argv
        cd $argv
    end

    alias frun='uv tool run flask run --debug'
    alias hx='helix'
    alias venv-create="python3 -m venv .venv"
    alias venv="source .venv/bin/activate.fish"
    alias py="python3"
    alias pip-upgrade='pip install --upgrade pip'
    alias code="codium"
end
