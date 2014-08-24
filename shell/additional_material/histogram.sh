#!/bin/bash
new_text=$(cat gettysburg_address.txt | tr ' ' '\n' | tr '[:upper:]' '[:lower:]' | sed 's/[\._,-]//g' | sort)
wordlist=(); 

for word in ${new_text}; do 
    new=1 
    for wl in ${wordlist[@]}; do 
        if [[ "$wl" == "$word" ]]; then 
            new=0
            break 
        fi 
    done
    if [ $new == 1 ]; then 
        wordlist=( ${wordlist[@]} $word ); 
        echo "${word}: $(echo $new_text | tr ' ' '\n' | grep -i -c "^$word$")" 
    fi; 
done
