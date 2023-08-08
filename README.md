# ipchecker
アクセス元とアクセス先を表示するコンテナ（LBの挙動確認用）

# how to use
```
k run --image imuratavmware/ipchecker ipchecker
```

```
$ k run centos --image centos -- sleep 1d
$ k exec -it centos -- curl ipchecker
Client IP: 127.0.0.6
Server IP: 100.96.3.191
```
