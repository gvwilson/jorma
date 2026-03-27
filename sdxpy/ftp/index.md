# Variable Role Analysis: ftp

## client_all.py

| Scope  | Variable       | Role        | Location |
| :------| :--------------| :-----------| :--------|
| module | CHUNK_SIZE     | fixed value | line 3   |
| module | SERVER_ADDRESS | fixed value | line 4   |
| module | message        | fixed value | line 6   |
| module | sock           | fixed value | line 8   |
| module | received       | fixed value | line 13  |
| module | received_str   | fixed value | line 14  |

## client_chunk.py

| Scope              | Variable       | Role               | Location |
| :------------------| :--------------| :------------------| :--------|
| module             | CHUNK_SIZE     | fixed value        | line 4   |
| module             | SERVER_ADDRESS | fixed value        | line 5   |
| module             | filename       | fixed value        | line 47  |
| module             | host           | fixed value        | line 47  |
| module             | port           | fixed value        | line 47  |
| module.main        | filename       | fixed value        | line 37  |
| module.main        | host           | fixed value        | line 37  |
| module.main        | port           | fixed value        | line 37  |
| module.main        | conn           | fixed value        | line 38  |
| module.main        | bytes_sent     | fixed value        | line 39  |
| module.main        | bytes_received | fixed value        | line 41  |
| module.make_socket | host           | fixed value        | line 8   |
| module.make_socket | port           | fixed value        | line 8   |
| module.make_socket | conn           | fixed value        | line 9   |
| module.receive_ack | conn           | fixed value        | line 31  |
| module.receive_ack | received       | fixed value        | line 32  |
| module.send_file   | conn           | fixed value        | line 15  |
| module.send_file   | filename       | fixed value        | line 15  |
| module.send_file   | reader         | fixed value        | line 16  |
| module.send_file   | data           | fixed value        | line 17  |
| module.send_file   | total          | gatherer           | line 19  |
| module.send_file   | sent           | most-recent holder | line 21  |

## logging_handler.py

| Scope                        | Variable   | Role               | Location |
| :----------------------------| :----------| :------------------| :--------|
| module                       | BLOCK_SIZE | fixed value        | line 3   |
| module                       | host       | fixed value        | line 28  |
| module                       | port       | fixed value        | line 28  |
| module                       | server     | fixed value        | line 29  |
| module.LoggingHandler.debug  | args       | fixed value        | line 21  |
| module.LoggingHandler.debug  | self       | fixed value        | line 21  |
| module.LoggingHandler.handle | self       | fixed value        | line 7   |
| module.LoggingHandler.handle | data       | gatherer           | line 9   |
| module.LoggingHandler.handle | latest     | most-recent holder | line 11  |

## server_chunk.py

| Scope                     | Variable   | Role               | Location |
| :-------------------------| :----------| :------------------| :--------|
| module                    | CHUNK_SIZE | fixed value        | line 4   |
| module                    | host       | fixed value        | line 23  |
| module                    | port       | fixed value        | line 23  |
| module                    | server     | fixed value        | line 24  |
| module.FileHandler.handle | self       | fixed value        | line 8   |
| module.FileHandler.handle | data       | gatherer           | line 10  |
| module.FileHandler.handle | latest     | most-recent holder | line 12  |

## server_lib.py

| Scope                   | Variable       | Role        | Location |
| :-----------------------| :--------------| :-----------| :--------|
| module                  | CHUNK_SIZE     | fixed value | line 3   |
| module                  | SERVER_ADDRESS | fixed value | line 4   |
| module                  | server         | fixed value | line 15  |
| module.MyHandler.handle | self           | fixed value | line 7   |
| module.MyHandler.handle | data           | fixed value | line 8   |
| module.MyHandler.handle | cli            | fixed value | line 9   |
| module.MyHandler.handle | msg            | fixed value | line 10  |

## server_raw.py

| Scope          | Variable      | Role        | Location |
| :--------------| :-------------| :-----------| :--------|
| module         | CHUNK_SIZE    | fixed value | line 3   |
| module.handler | host          | fixed value | line 6   |
| module.handler | port          | fixed value | line 6   |
| module.handler | server_socket | fixed value | line 7   |
| module.handler | address       | fixed value | line 11  |
| module.handler | conn          | fixed value | line 11  |
| module.handler | data          | fixed value | line 14  |
| module.handler | msg           | fixed value | line 15  |

## test_server.py

| Scope                       | Variable  | Role        | Location |
| :---------------------------| :---------| :-----------| :--------|
| module.MockHandler.__init__ | message   | fixed value | line 23  |
| module.MockHandler.__init__ | self      | fixed value | line 23  |
| module.MockHandler.debug    | args      | fixed value | line 26  |
| module.MockHandler.debug    | self      | fixed value | line 26  |
| module.MockRequest.__init__ | message   | fixed value | line 5   |
| module.MockRequest.__init__ | self      | fixed value | line 5   |
| module.MockRequest.recv     | max_bytes | fixed value | line 10  |
| module.MockRequest.recv     | self      | fixed value | line 10  |
| module.MockRequest.recv     | top       | fixed value | line 12  |
| module.MockRequest.recv     | result    | fixed value | line 13  |
| module.MockRequest.sendall  | outgoing  | fixed value | line 17  |
| module.MockRequest.sendall  | self      | fixed value | line 17  |
| module.test_short           | msg       | fixed value | line 32  |
| module.test_short           | handler   | fixed value | line 33  |

