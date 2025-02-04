#!/bin/bash

# Current date in YYYY-MM-DD format
CURRENT_DATE=$(date +%Y-%m-%d)

# Find all markdown files in the docs directory
find /Users/niladridas/Documents/model/docs -name "*.md" | while read -r file; do
    # Replace date patterns in the files
    sed -i '' "s/\([0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}\)/$CURRENT_DATE/g" "$file"
    sed -i '' "s/Last Updated:.*/Last Updated: $CURRENT_DATE/g" "$file"
    sed -i '' "s/Version:.*/Version: 1.0.0/g" "$file"
    
    echo "Updated dates in $file"
done

# Update README.md
sed -i '' "s/\([0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}\)/$CURRENT_DATE/g" /Users/niladridas/Documents/model/README.md
sed -i '' "s/Last Updated:.*/Last Updated: $CURRENT_DATE/g" /Users/niladridas/Documents/model/README.md
