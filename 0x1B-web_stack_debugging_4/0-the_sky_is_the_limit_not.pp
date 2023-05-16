# configuring nginx to allow maximum number of open files

exec { 'config_nginx':
  command => 'sed -i "s/^\(.*ULIMIT.*\)=.*/\1=4096" /etc/default/nginx',
  path    => '/usr/local/bin/:bin/',
  onlyif  => 'grep -q "ULIMIT" /etc/default/nginx',
} ->

exec { 'restart_nginx':
  command => 'service nginx restart',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
  require => Exec['config_nginx'],
}
