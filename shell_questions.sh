# list all text files in the current directory (excluding subdirectories) that have been modified in the last 30 days
find . -maxdepth 1 -name "*.txt" -type f -mtime -30