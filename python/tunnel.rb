#!/usr/bin/env ruby
require 'localtunnel/tunnel'

# Port number
port = ARGV[0]

# The webhook that should be notified when the tunnel is created. In this case, a
# webhook handled by a Kynetx ruleset.
app_url = ARGV[1]

# The key file can be provided either as a command-line argument 
# or by finding the first *.pub file in the user's .ssh directory
key_file_name = ARGV[2] ? ARGV[2] : Dir[File.expand_path('~/.ssh/*.pub')].first
key_file = File.open(key_file_name, "rb")
key = key_file.read

# Create and open the tunnel
tunnel = LocalTunnel::Tunnel.new(port, key, app_url)
tunnel.register_tunnel()
tunnel.start_tunnel()


