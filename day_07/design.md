# Log Analyzer – Design Plan (Day 07)

## What problem am I solving?
- Log files are large and hard to analyze manually
- Important errors can be missed
- I need a quick summary of log levels

## What input does the script need?
- Log file path (example: app.log)
- Optional log level filter (INFO / WARNING / ERROR)

## What output should the script give?
- Log summary printed in terminal
- Same summary written into an output file

## What are the main steps?
1. Read the log file
2. Loop through each line
3. Identify log level
4. Count INFO, WARNING, and ERROR
5. Display summary
6. Save summary to file
