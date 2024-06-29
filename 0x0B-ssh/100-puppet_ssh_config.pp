#!/usr/bin/env bash
# Using puppet to connect without typing password

# define the type of file
file { '/etc/ssh/ssh_config':
  # ensure the file exists before anything further
  ensure => present,
}

file_line { 'Turn off passwd auth':
  # specifies the path to the file being modified.
  path    => '/etc/ssh/ssh_config',
  # defines the line to be modified
  line    => 'PasswordAuthentication no',
  # specifies a regular expression to match the existing line before modifying it.
  match   => '^#PasswordAuthentication',
}

file_line { 'Declare identity file':
  # # specifies the path to the file being modified.
  path    => '/etc/ssh/ssh_config',
  # defines the line to be modified
  line    => 'IdentityFile ~/.ssh/school',
  # specifies a regular expression to match the existing line before modifying it.
  match   => '^#IdentityFile',
}
