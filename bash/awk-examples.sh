
awkLanguage(){
  awk 'program' input-file1 input-file2
  awk -f program-file input-file1 input-file2

  # /{pattern}/ uses a regular expression.
  awk '/li/ { print $0 }' ${input_file} # prints out lines in input file with 'li'
  awk '/li/ { print $1 }' ${input_file} # print out the first column with lines containging 'li'

  # print every line longer than 80 chars.
  awk 'length($0) > 80' ${input_file}

  # print length of the longest line
  awk '{ if (length($0) > max) max = length($0)} END { print max }' ${input_file}
  awk '{ if (length($0) > max) max = length($0)} END { print $0 }' ${input_file} # would only print the longest line because END
  awk '{ if (length($0) > max) max = length($0)} { print $0 }' ${input_file} # would print all the lines anyway

  # get a substr
  awk '{ first_char = substr($1, 1, 1); print first_char}' ${input_file}

  # Print a substring(2,5) of the longest lines first column.
  awk '{if (length($1) > max) max = length($1)} END { first_char = substr($1, 2, 5); print first_char}' ${input_file}
}
