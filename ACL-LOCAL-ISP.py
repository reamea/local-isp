ip access-list extended acl-local-isp-in
 remark #ONLINE#
 permit ip any 203.189.128.0 0.0.31.255
 permit ip any 124.248.160.0 0.0.31.255
 permit ip any 202.62.32.0 0.0.31.255
 permit ip any 103.239.52.0 0.0.3.255
 permit ip any 43.230.192.0 0.0.3.255
 remark #EZECOM#

ip access-list extended acl-local-isp-out
 remark #ONLINE#
 permit ip 203.189.128.0 0.0.31.255 any
 permit ip 124.248.160.0 0.0.31.255 any
 permit ip 202.62.32.0 0.0.31.255 any
 permit ip 103.239.52.0 0.0.3.255 any
 permit ip 43.230.192.0 0.0.3.255 any
 remark #EZECOM#