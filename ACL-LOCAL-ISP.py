ip access-list extended acl-local-isp-in
 remark #ONLINE#
 permit ip any 203.189.128.0 0.0.31.255
 permit ip any 124.248.160.0 0.0.31.255
 permit ip any 202.62.32.0 0.0.31.255
 permit ip any 103.239.52.0 0.0.3.255
 permit ip any 43.230.192.0 0.0.3.255
 remark #EZECOM#
 permit ip any 110.74.192.0 0.0.31.255
 permit ip any 113.130.252.0 0.0.3.255
 permit ip any 119.82.248.0 0.0.7.255
 permit ip any 103.9.252.0 0.0.3.255
 permit ip any 163.47.252.0 0.0.3.255
 remark #MekongNet#
 permit ip any 111.90.176.0 0.0.15.255
 permit ip any 116.212.128.0 0.0.31.255
 permit ip any 203.176.240.0 0.0.15.255
 remark #Metfone#
 permit ip any 36.37.28.0 0.0.127.255
 permit ip any 45.64.124.0 0.0.3.255
 permit ip any 103.253.180.0 0.0.3.255
 permit ip any 111.118.128.0 0.0.31.255
 permit ip any 117.120.24.0 0.0.7.255
 permit ip any 175.100.0.0 0.0.127.255
 permit ip any 202.150.0.0 0.0.3.255
 remark #wicam#
 permit ip any 43.245.216.0 0.0.3.255
 permit ip any 49.156.224.0 0.0.31.255
 permit ip any 103.17.252.0 0.0.3.255
 permit ip any 119.15.240.0 0.0.15.255
 permit ip any 202.79.248.0 0.0.7.255
 remark #chunwie#
 permit ip any 103.246.252.0 0.0.3.255
 permit ip any 111.64.240.0 0.0.15.255
 permit ip any 124.108.252.0 0.0.3.255
 permit ip any 150.129.252.0 0.0.3.255

ip access-list extended acl-local-isp-out
 remark #ONLINE#
 permit ip 203.189.128.0 0.0.31.255 any
 permit ip 124.248.160.0 0.0.31.255 any
 permit ip 202.62.32.0 0.0.31.255 any
 permit ip 103.239.52.0 0.0.3.255 any
 permit ip 43.230.192.0 0.0.3.255 any
 remark #EZECOM#
 permit ip 110.74.192.0 0.0.31.255 any
 permit ip 113.130.252.0 0.0.3.255 any
 permit ip 119.82.248.0 0.0.7.255 any
 permit ip 103.9.252.0 0.0.3.255 any
 permit ip 163.47.252.0 0.0.3.255 any
 remark #MekongNet#
 permit ip 111.90.176.0 0.0.15.255 any
 permit ip 116.212.128.0 0.0.31.255 any
 permit ip 203.176.240.0 0.0.15.255 any
 remark #Metfone#
 permit ip 36.37.28.0 0.0.127.255 any
 permit ip 45.64.124.0 0.0.3.255 any
 permit ip 103.253.180.0 0.0.3.255 any
 permit ip 111.118.128.0 0.0.31.255 any
 permit ip 117.120.24.0 0.0.7.255 any
 permit ip 175.100.0.0 0.0.127.255 any
 permit ip 202.150.0.0 0.0.3.255 any
 remark #wicam#
 permit ip 43.245.216.0 0.0.3.255 any
 permit ip 49.156.224.0 0.0.31.255 any
 permit ip 103.17.252.0 0.0.3.255 any
 permit ip 119.15.240.0 0.0.15.255 any
 permit ip 202.79.248.0 0.0.7.255 any
 remark #chunwie#
 permit ip 103.246.252.0 0.0.3.255 any
 permit ip 111.64.240.0 0.0.15.255 any
 permit ip 124.108.252.0 0.0.3.255 any
 permit ip 150.129.252.0 0.0.3.255 any