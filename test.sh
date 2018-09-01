#create temporary files from test files with unsorted imports
for file in *.test; 
    do cp "$file" "$(echo "$file" | rev | cut -c 6- | rev).temp";
done

#sort imports in temporary files
ls | grep .*temp$ | python sort.py

#set color constants for output
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

#for each temporary file
for file in *.temp; do
    #compare temporary file with expected result file
    cmp "$file" "$(echo "$file" | rev | cut -c 6- | rev).verify";

    #print comparison status
    status=$?
    if [[ $status = 0 ]]; then
        echo "${green}$(echo "$file" | rev | cut -c 6- | rev) test passed.${reset}"
    else
        echo "${red}$(echo "$file" | rev | cut -c 6- | rev) test failed.${reset}"
    fi

    #remove temporary file
    rm -f "$file"
done