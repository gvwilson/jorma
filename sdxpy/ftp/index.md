# Transferring Files

## client_all.py

| Variable | Scope | Role |
|---|---|---|
| CHUNK_SIZE | module | fixed value |
| SERVER_ADDRESS | module | fixed value |
| message | module | fixed value |
| sock | module | fixed value |
| received | module | fixed value |
| received_str | module | fixed value |

## server_raw.py

| Variable | Scope | Role |
|---|---|---|
| CHUNK_SIZE | module | fixed value |
| host | module.handler | fixed value |
| port | module.handler | fixed value |
| server_socket | module.handler | fixed value |
| address | module.handler | fixed value |
| conn | module.handler | fixed value |
| data | module.handler | fixed value |
| msg | module.handler | fixed value |

## server_lib.py

| Variable | Scope | Role |
|---|---|---|
| CHUNK_SIZE | module | fixed value |
| SERVER_ADDRESS | module | fixed value |
| server | module | fixed value |
| self | module.MyHandler.handle | fixed value |
| data | module.MyHandler.handle | fixed value |
| cli | module.MyHandler.handle | fixed value |
| msg | module.MyHandler.handle | fixed value |

## server_chunk.py

| Variable | Scope | Role |
|---|---|---|
| CHUNK_SIZE | module | fixed value |
| host | module | fixed value |
| port | module | fixed value |
| server | module | fixed value |
| self | module.FileHandler.handle | fixed value |
| data | module.FileHandler.handle | gatherer |
| latest | module.FileHandler.handle | most-recent holder |

## client_chunk.py

| Variable | Scope | Role |
|---|---|---|
| CHUNK_SIZE | module | fixed value |
| SERVER_ADDRESS | module | fixed value |
| filename | module | fixed value |
| host | module | fixed value |
| port | module | fixed value |
| filename | module.main | fixed value |
| host | module.main | fixed value |
| port | module.main | fixed value |
| conn | module.main | fixed value |
| bytes_sent | module.main | fixed value |
| bytes_received | module.main | fixed value |
| host | module.make_socket | fixed value |
| port | module.make_socket | fixed value |
| conn | module.make_socket | fixed value |
| conn | module.receive_ack | fixed value |
| received | module.receive_ack | fixed value |
| conn | module.send_file | fixed value |
| filename | module.send_file | fixed value |
| reader | module.send_file | fixed value |
| data | module.send_file | fixed value |
| total | module.send_file | gatherer |
| sent | module.send_file | most-recent holder |

## logging_handler.py

| Variable | Scope | Role |
|---|---|---|
| BLOCK_SIZE | module | fixed value |
| host | module | fixed value |
| port | module | fixed value |
| server | module | fixed value |
| args | module.LoggingHandler.debug | fixed value |
| self | module.LoggingHandler.debug | fixed value |
| self | module.LoggingHandler.handle | fixed value |
| data | module.LoggingHandler.handle | gatherer |
| latest | module.LoggingHandler.handle | most-recent holder |

## test_server.py

| Variable | Scope | Role |
|---|---|---|
| message | module.MockHandler.__init__ | fixed value |
| self | module.MockHandler.__init__ | fixed value |
| args | module.MockHandler.debug | fixed value |
| self | module.MockHandler.debug | fixed value |
| message | module.MockRequest.__init__ | fixed value |
| self | module.MockRequest.__init__ | fixed value |
| max_bytes | module.MockRequest.recv | fixed value |
| self | module.MockRequest.recv | fixed value |
| top | module.MockRequest.recv | fixed value |
| result | module.MockRequest.recv | fixed value |
| outgoing | module.MockRequest.sendall | fixed value |
| self | module.MockRequest.sendall | fixed value |
| msg | module.test_short | fixed value |
| handler | module.test_short | fixed value |

