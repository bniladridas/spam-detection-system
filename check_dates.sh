#!/bin/bash

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Target date
TARGET_DATE="2025-02-04"

# Find all markdown files in the docs directory
find /Users/niladridas/Documents/model/docs -name "*.md" | while read -r file; do
    echo -e "\n${GREEN}Checking file: $file${NC}"
    
    # Search for date patterns
    date_lines=$(grep -E "([0-9]{4}-[0-9]{2}-[0-9]{2}|Last Updated:|Version:)" "$file")
    
    if [ -z "$date_lines" ]; then
        echo -e "${RED}No date-related lines found in $file${NC}"
    else
        echo "$date_lines" | while read -r line; do
            # Check if the line contains the target date
            if [[ "$line" =~ $TARGET_DATE ]]; then
                echo -e "${GREEN}✓ Correct date found: $line${NC}"
            else
                echo -e "${RED}✗ Incorrect date or format: $line${NC}"
            fi
        done
    fi
done
