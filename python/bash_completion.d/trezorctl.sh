_detahardctl()
{
    export detahardCTL_COMPLETION_CACHE
    local cur prev cmds base

    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    if [ -z "$detahardCTL_COMPLETION_CACHE" ]; then
        help_output=$(detahardctl --help | grep '^  [a-z]' | awk '{ print $1 }')
        export detahardCTL_COMPLETION_CACHE="$help_output"
    fi

    cmds="$detahardCTL_COMPLETION_CACHE"

    COMPREPLY=($(compgen -W "${cmds}" -- ${cur}))
    return 0
}

complete -F _detahardctl detahardctl
