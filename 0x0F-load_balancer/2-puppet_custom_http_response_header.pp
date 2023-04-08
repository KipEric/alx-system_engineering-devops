class response_header {

  $header_name = 'X-Served-By'
  $header_value = $::hostname

  if package('nginx') {

    $config_file = '/etc/nginx/sites-available/default'

    file_line { "Add ${header_name} header to ${config_file}":
      path  => $config_file,
      line  => "    add_header ${header_name} ${header_value};",
      match => "^    listen 80 default_server;$",
    }

    service { 'nginx':
      ensure => 'running',
      enable => true,
      require => File_line["Add ${header_name} header to ${config_file}"],
    }

  } else {
    package { 'nginx':
      ensure => installed,
    }
  }

}

include response_header
