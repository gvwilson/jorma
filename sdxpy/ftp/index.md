# Variable Role Analysis: ftp

## client_all.py

```

[module]
  CHUNK_SIZE               fixed value             (line 3)
  SERVER_ADDRESS           fixed value             (line 4)
  message                  fixed value             (line 6)
  sock                     fixed value             (line 8)
  received                 fixed value             (line 13)
  received_str             fixed value             (line 14)
```

## client_chunk.py

```

[module]
  CHUNK_SIZE               fixed value             (line 4)
  SERVER_ADDRESS           fixed value             (line 5)
  filename                 fixed value             (line 47)
  host                     fixed value             (line 47)
  port                     fixed value             (line 47)

[module.main]
  filename                 fixed value             (line 37)
  host                     fixed value             (line 37)
  port                     fixed value             (line 37)
  conn                     fixed value             (line 38)
  bytes_sent               fixed value             (line 39)
  bytes_received           fixed value             (line 41)

[module.make_socket]
  host                     fixed value             (line 8)
  port                     fixed value             (line 8)
  conn                     fixed value             (line 9)

[module.receive_ack]
  conn                     fixed value             (line 31)
  received                 fixed value             (line 32)

[module.send_file]
  conn                     fixed value             (line 15)
  filename                 fixed value             (line 15)
  reader                   fixed value             (line 16)
  data                     fixed value             (line 17)
  total                    gatherer                (line 19)
  sent                     most-recent holder      (line 21)
```

## logging_handler.py

```

[module]
  BLOCK_SIZE               fixed value             (line 3)
  host                     fixed value             (line 28)
  port                     fixed value             (line 28)
  server                   fixed value             (line 29)

[module.LoggingHandler.debug]
  args                     fixed value             (line 21)
  self                     fixed value             (line 21)

[module.LoggingHandler.handle]
  self                     fixed value             (line 7)
  data                     gatherer                (line 9)
  latest                   most-recent holder      (line 11)
```

## server_chunk.py

```

[module]
  CHUNK_SIZE               fixed value             (line 4)
  host                     fixed value             (line 23)
  port                     fixed value             (line 23)
  server                   fixed value             (line 24)

[module.FileHandler.handle]
  self                     fixed value             (line 8)
  data                     gatherer                (line 10)
  latest                   most-recent holder      (line 12)
```

## server_lib.py

```

[module]
  CHUNK_SIZE               fixed value             (line 3)
  SERVER_ADDRESS           fixed value             (line 4)
  server                   fixed value             (line 15)

[module.MyHandler.handle]
  self                     fixed value             (line 7)
  data                     fixed value             (line 8)
  cli                      fixed value             (line 9)
  msg                      fixed value             (line 10)
```

## server_raw.py

```

[module]
  CHUNK_SIZE               fixed value             (line 3)

[module.handler]
  host                     fixed value             (line 6)
  port                     fixed value             (line 6)
  server_socket            fixed value             (line 7)
  address                  fixed value             (line 11)
  conn                     fixed value             (line 11)
  data                     fixed value             (line 14)
  msg                      fixed value             (line 15)
```

## test_server.py

```

[module.MockHandler.__init__]
  message                  fixed value             (line 23)
  self                     fixed value             (line 23)

[module.MockHandler.debug]
  args                     fixed value             (line 26)
  self                     fixed value             (line 26)

[module.MockRequest.__init__]
  message                  fixed value             (line 5)
  self                     fixed value             (line 5)

[module.MockRequest.recv]
  max_bytes                fixed value             (line 10)
  self                     fixed value             (line 10)
  top                      fixed value             (line 12)
  result                   fixed value             (line 13)

[module.MockRequest.sendall]
  outgoing                 fixed value             (line 17)
  self                     fixed value             (line 17)

[module.test_short]
  msg                      fixed value             (line 32)
  handler                  fixed value             (line 33)
```

