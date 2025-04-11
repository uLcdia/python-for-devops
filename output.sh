#!/bin/bash

# Set timeout in seconds
TIMEOUT=5

# Enable globstar for ** pattern
shopt -s globstar

# Find all .py files in the specified directories
for py_file in ./*.py ./**/*.py; do
  # Skip if the pattern didn't match any files
  [[ -f "$py_file" ]] || continue
  
  echo "Processing file: $py_file"

  # Run the Python script with timeout and capture output
  run_output=$(timeout "$TIMEOUT" python "$py_file" 2>&1)
  run_status=$?

  if [ "$run_status" -eq 124 ]; then
    echo "Script '$py_file' timed out after $TIMEOUT seconds."
  else
    echo "Script '$py_file' finished within time limit."

    # Append the output docstring to the end of the Python file
    if [ -s "$py_file" ]; then # Check if file is not empty to avoid issues with empty files
      cat << EOF >> "$py_file"

"""
$run_output
"""
EOF

      if [ $? -eq 0 ]; then
        echo "Output appended to '$py_file'."
      else
        echo "Error: Failed to append output to '$py_file'."
      fi
    else
      echo "Warning: '$py_file' is empty, skipping output append."
    fi
  fi
  echo "-------------------------"
done

echo "Script finished processing all .py files."