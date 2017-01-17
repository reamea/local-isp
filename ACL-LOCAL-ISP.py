ip access-list extended acl-local-isp-in
 remark #ONLINE#
 permit ip any 203.189.128.0 0.0.31.255
 permit ip any 124.248.160.0 0.0.31.255
 permit ip any 202.62.32.0 0.0.31.255
 permit ip any 103.239.52.0 0.0.3.255
 permit ip any 43.230.192.0 0.0.3.255
 remark #EZECOM#
 permit ip any 110.74.192.0 0.0.31.255
 permit ip any 113.130.124.0 0.0.3.255
 permit ip any 119.82.248.0 0.0.7.255
 permit ip any 103.9.188.0 0.0.3.255
 permit ip any 163.47.172.0 0.0.3.255
 remark #MekongNet#
 permit ip any 111.90.176.0 0.0.15.255
 permit ip any 116.212.128.0 0.0.31.255
 permit ip any 203.176.128.0 0.0.15.255
 remark #Metfone#
 permit ip any 36.37.128.0 0.0.127.255
 permit ip any 45.64.124.0 0.0.3.255
 permit ip any 103.253.180.0 0.0.3.255
 permit ip any 111.118.128.0 0.0.31.255
 permit ip any 117.120.24.0 0.0.7.255
 permit ip any 175.100.0.0 0.0.127.255
 permit ip any 202.150.0.0 0.0.3.255
 remark #wicam#
 permit ip any 43.245.216.0 0.0.3.255
 permit ip any 49.156.32.0 0.0.15.255
 permit ip any 103.17.212.0 0.0.3.255
 permit ip any 119.15.80.0 0.0.15.255
 permit ip any 202.79.24.0 0.0.7.255
 remark #chunwie#
 permit ip any 103.246.228.0 0.0.3.255
 permit ip any 111.67.96.0 0.0.15.255
 permit ip any 124.108.4.0 0.0.3.255
 permit ip any 150.129.20.0 0.0.3.255
 remark #AngkorNet#
 permit ip any 202.178.112.0 0.0.15.255
 remark #CADCOMM#
 permit ip any 117.55.248.0 0.0.7.255
 remark #CamboTech
 permit ip any 202.131.80.0 0.0.7.255
 remark #CAMINTEL#
 permit ip any 103.240.112.0 0.0.3.255
 permit ip any 120.136.24.0 0.0.7.255
 permit ip any 124.108.48.0 0.0.7.255
 permit ip any 183.81.184.0 0.0.7.255
 remark #CityLink#
 permit ip any 103.5.230.0 0.0.3.255
 permit ip any 103.28.242.0 0.0.1.255
 permit ip any 202.84.72.0 0.0.7.255
 permit ip any 202.93.8.0 0.0.7.255
 remark #DiGi#
 permit ip any 27.109.116.0 0.0.3.255
 permit ip any 103.23.132.0 0.0.3.255
 permit ip any 111.92.240.0 0.0.3.255
 permit ip any 114.134.184.0 0.0.7.255
 permit ip any 115.178.24.0 0.0.3.255
 remark #HTN#
 permit ip any 27.111.8.0 0.0.3.255
 permit ip any 218.100.71.0 0.0.0.255
 remark #Inet#
 permit ip any 27.116.60.0 0.0.0.255
 remark #NTC#
 permit ip any 103.244.248.0 0.0.3.255
 permit ip any 123.108.248.0 0.0.7.255
 permit ip any 146.196.88.0 0.0.3.255
 permit ip any 203.167.16.0 0.0.3.255
 remark #PPCTV#
 permit ip any 122.252.176.0 0.0.7.255
 remark #Sabay#
 permit ip any 118.67.200.0 0.0.0.255
 permit ip any 118.67.202.0 0.0.0.255
 remark #SeaTel#
 permit ip any 103.242.56.0 0.0.3.255
 permit ip any 202.53.144.0 0.0.3.255
 remark #Smart#
 permit ip any 117.20.112.0 0.0.7.255
 permit ip any 27.109.112.0 0.0.3.255
 permit ip any 202.93.153.0 0.0.0.255
 permit ip any 202.129.236.0 0.0.0.255
 permit ip any 203.118.242.0 0.0.0.255
 remark #TC#
 permit ip any 45.127.152.0 0.0.3.255
 permit ip any 103.6.8.0 0.0.3.255
 permit ip any 103.248.40.0 0.0.3.255
 permit ip any 202.150.8.0 0.0.3.255
 permit ip any 203.223.32.0 0.0.15.255
 remark #XinWei#
 permit ip any 43.255.112.0 0.0.3.255
 permit ip any 103.5.124.0 0.0.3.255
 permit ip any 146.88.200.0 0.0.7.255
 remark #SINET#
 permit ip any 43.245.202.0 0.0.0.255
 permit ip any 43.245.203.0 0.0.0.255
 permit ip any 96.9.64.0 0.0.31.255
 permit ip any 103.14.248.0 0.0.3.255
 permit ip any 180.178.124.0 0.0.3.255
 permit ip any 203.217.168.0 0.0.3.255

ip access-list extended acl-local-isp-out
 remark #ONLINE#
 permit ip 203.189.128.0 0.0.31.255 any
 permit ip 124.248.160.0 0.0.31.255 any
 permit ip 202.62.32.0 0.0.31.255 any
 permit ip 103.239.52.0 0.0.3.255 any
 permit ip 43.230.192.0 0.0.3.255 any
 remark #EZECOM#
 permit ip 110.74.192.0 0.0.31.255 any
 permit ip 113.130.124.0 0.0.3.255 any
 permit ip 119.82.248.0 0.0.7.255 any
 permit ip 103.9.188.0 0.0.3.255 any
 permit ip 163.47.172.0 0.0.3.255 any
 remark #MekongNet#
 permit ip 111.90.176.0 0.0.15.255 any
 permit ip 116.212.128.0 0.0.31.255 any
 permit ip 203.176.128.0 0.0.15.255 any
 remark #Metfone#
 permit ip 36.37.128.0 0.0.127.255 any
 permit ip 45.64.124.0 0.0.3.255 any
 permit ip 103.253.180.0 0.0.3.255 any
 permit ip 111.118.128.0 0.0.31.255 any
 permit ip 117.120.24.0 0.0.7.255 any
 permit ip 175.100.0.0 0.0.127.255 any
 permit ip 202.150.0.0 0.0.3.255 any
 remark #wicam#
 permit ip 43.245.216.0 0.0.3.255 any
 permit ip 49.156.32.0 0.0.31.255 any
 permit ip 103.17.212.0 0.0.3.255 any
 permit ip 119.15.80.0 0.0.15.255 any
 permit ip 202.79.24.0 0.0.7.255 any
 remark #chunwie#
 permit ip 103.246.228.0 0.0.3.255 any
 permit ip 111.67.96.0 0.0.15.255 any
 permit ip 124.108.4.0 0.0.3.255 any
 permit ip 150.129.20.0 0.0.3.255 any
 remark #AngkorNet#
 permit ip 202.178.112.0 0.0.15.255 any
 remark #CADCOMM#
 permit ip 117.55.248.0 0.0.7.255 any
 remark #CamboTech
 permit ip 202.131.80.0 0.0.7.255 any
 remark #CAMINTEL#
 permit ip 103.240.112.0 0.0.3.255 any
 permit ip 120.136.24.0 0.0.7.255 any
 permit ip 124.108.48.0 0.0.7.255 any
 permit ip 183.81.184.0 0.0.7.255 any
 remark #CityLink#
 permit ip 103.5.230.0 0.0.3.255 any
 permit ip 103.28.242.0 0.0.1.255 any
 permit ip 202.84.72.0 0.0.7.255 any
 permit ip 202.93.8.0 0.0.7.255 any
 remark #DiGi#
 permit ip 27.109.116.0 0.0.3.255 any
 permit ip 103.23.132.0 0.0.3.255 any
 permit ip 111.92.240.0 0.0.3.255 any
 permit ip 114.134.184.0 0.0.7.255 any
 permit ip 115.178.24.0 0.0.3.255 any
 remark #HTN#
 permit ip 27.111.8.0 0.0.3.255 any
 permit ip 218.100.71.0 0.0.0.255 any
 remark #Inet#
 permit ip 27.116.60.0 0.0.0.255 any
 remark #NTC#
 permit ip 103.244.248.0 0.0.3.255 any
 permit ip 123.108.248.0 0.0.7.255 any
 permit ip 146.196.88.0 0.0.3.255 any
 permit ip 203.167.16.0 0.0.3.255 any
 remark #PPCTV#
 permit ip 122.252.176.0 0.0.7.255 any
 remark #Sabay#
 permit ip 118.67.200.0 0.0.0.255 any
 permit ip 118.67.202.0 0.0.0.255 any
 remark #SeaTel#
 permit ip 103.242.56.0 0.0.3.255 any
 permit ip 202.53.144.0 0.0.3.255 any
 remark #Smart#
 permit ip 117.20.112.0 0.0.7.255 any
 permit ip 27.109.112.0 0.0.3.255 any
 permit ip 202.93.153.0 0.0.0.255 any
 permit ip 202.129.236.0 0.0.0.255 any
 permit ip 203.118.242.0 0.0.0.255 any
 remark #TC#
 permit ip 45.127.152.0 0.0.3.255 any
 permit ip 103.6.8.0 0.0.3.255 any
 permit ip 103.248.40.0 0.0.3.255 any
 permit ip 202.150.8.0 0.0.3.255 any
 permit ip 203.223.32.0 0.0.15.255 any
 remark #XinWei#
 permit ip 43.255.112.0 0.0.3.255 any
 permit ip 103.5.124.0 0.0.3.255 any
 permit ip 146.88.200.0 0.0.7.255 any
  remark #SINET#
 permit ip 43.245.202.0 0.0.0.255 any
 permit ip 43.245.203.0 0.0.0.255 any
 permit ip 96.9.64.0 0.0.31.255 any
 permit ip 103.14.248.0 0.0.3.255 any
 permit ip 180.178.124.0 0.0.3.255 any
 permit ip 203.217.168.0 0.0.3.255 any