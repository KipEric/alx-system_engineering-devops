# OS configuration that make it possible to login with the holberton

file { '/etc/security/limits.d/holberton.cofig':
  content => "holberton soft nofile 4096\nholberton hard nofile 8192",
}

exec { 'pam-auth-update':
  command     => 'pam-auth-update --force',
  refreshonly => true,
}
