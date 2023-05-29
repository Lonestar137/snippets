

ncat(){
  WhatCanItDo(){
    # CAN:
    #   Act as a quick proxy.
    #     Can also use it to connect to a proxy server.
    #   Transfer files.
    #   Provide internet connectivity to devices.
    #   Listen for connections on port.
    #
    # LIMITATIONS:
    #

  }

  Examples(){
    # Connect to example.org on TCP port 8000.
    ncat example.org 8080

    # Listen for connections on TCP port 8080.
    ncat -l 8080

    # Redirect TCP port 8080 on the local machine to host on port 80.
    ncat --sh-exec "ncat example.org 80" -l 8080 --keep-open

    # Bind to TCP port 8081 and attach /bin/bash for the world to access freely.
    ncat --exec "/bin/bash" -l 8081 --keep-open

    # Bind a shell to TCP port 8081, limit access to hosts on a local network, and limit the maximum number of simultaneous connections to 3.
    ncat --exec "/bin/bash" --max-conns 3 --allow 192.168.0.0/24 -l 8081 --keep-open

    # Connect to smtphost:25 through a SOCKS4 server on port 1080.
    ncat --proxy socks4host --proxy-type socks4 --proxy-auth joe smtphost 25

    # Connect to smtphost:25 through a SOCKS5 server on port 1080.
    ncat --proxy socks5host --proxy-type socks5 --proxy-auth joe:secret smtphost 25

    # Create an HTTP proxy server on localhost port 8888.
    ncat -l --proxy-type http localhost 8888

    # Send a file over TCP port 9899 from host2 (client) to host1 (server).
    HOST1$ ncat -l 9899 > outputfile

    HOST2$ ncat HOST1 9899 < inputfile

    # Transfer in the other direction, turning Ncat into a “one file” server.
    HOST1$ ncat -l 9899 < inputfile

    HOST2$ ncat HOST1 9899 > outputfile
  }

}

