# puppet declarative script to install flask from pip3.

package { 'python3':
  ensure => 'present'
}

package { 'python3-pip':
  ensure => 'present'
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

package { 'werkzeug':
  ensure => '2.1.1',
  provider => 'pip',
}
