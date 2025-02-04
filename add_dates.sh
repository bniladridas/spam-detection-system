#!/bin/bash

# Target date
TARGET_DATE="2025-02-04"

# Find all markdown files in the docs directory
find /Users/niladridas/Documents/model/docs -name "*.md" | while read -r file; do
    # Skip project_narrative.md as it's already updated
    if [[ "$file" == *"project_narrative.md" ]]; then
        continue
    fi

    # Add date and version to the end of the file
    echo -e "\n---\n\n**Version**: 1.0.0\n**Last Updated**: $TARGET_DATE" >> "$file"
    
    echo "Added date to $file"
done
