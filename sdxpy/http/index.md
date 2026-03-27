# Variable Role Analysis: http

## basic_server.py

| Scope                        | Variable       | Role        | Location |
| :----------------------------| :--------------| :-----------| :--------|
| module                       | PAGE           | fixed value | line 3   |
| module                       | server_address | fixed value | line 17  |
| module                       | server         | fixed value | line 18  |
| module.RequestHandler.do_GET | self           | fixed value | line 6   |
| module.RequestHandler.do_GET | content        | fixed value | line 7   |

## file_server.py

| Scope                              | Variable      | Role        | Location |
| :----------------------------------| :-------------| :-----------| :--------|
| module                             | ERROR_PAGE    | fixed value | line 6   |
| module                             | serverAddress | fixed value | line 64  |
| module                             | server        | fixed value | line 65  |
| module.RequestHandler.do_GET       | self          | fixed value | line 23  |
| module.RequestHandler.do_GET       | url_path      | fixed value | line 25  |
| module.RequestHandler.do_GET       | full_path     | fixed value | line 26  |
| module.RequestHandler.do_GET       | msg           | fixed value | line 33  |
| module.RequestHandler.handle_error | msg           | fixed value | line 48  |
| module.RequestHandler.handle_error | self          | fixed value | line 48  |
| module.RequestHandler.handle_error | content       | unknown     | line 49  |
| module.RequestHandler.handle_file  | full_path     | fixed value | line 38  |
| module.RequestHandler.handle_file  | given_path    | fixed value | line 38  |
| module.RequestHandler.handle_file  | self          | fixed value | line 38  |
| module.RequestHandler.handle_file  | reader        | fixed value | line 40  |
| module.RequestHandler.handle_file  | content       | fixed value | line 41  |
| module.RequestHandler.send_content | content       | fixed value | line 55  |
| module.RequestHandler.send_content | self          | fixed value | line 55  |
| module.RequestHandler.send_content | status        | fixed value | line 55  |

## mock_handler.py

| Scope                                   | Variable | Role        | Location |
| :---------------------------------------| :--------| :-----------| :--------|
| module.MockRequestHandler.__init__      | path     | fixed value | line 4   |
| module.MockRequestHandler.__init__      | self     | fixed value | line 4   |
| module.MockRequestHandler.end_headers   | self     | fixed value | line 18  |
| module.MockRequestHandler.send_header   | key      | fixed value | line 13  |
| module.MockRequestHandler.send_header   | self     | fixed value | line 13  |
| module.MockRequestHandler.send_header   | value    | fixed value | line 13  |
| module.MockRequestHandler.send_response | self     | fixed value | line 10  |
| module.MockRequestHandler.send_response | status   | fixed value | line 10  |

## requests_example.py

| Scope  | Variable | Role        | Location |
| :------| :--------| :-----------| :--------|
| module | response | fixed value | line 3   |

## test_testable_server.py

| Scope                        | Variable      | Role        | Location |
| :----------------------------| :-------------| :-----------| :--------|
| module.test_existing_path    | fs            | fixed value | line 22  |
| module.test_existing_path    | content_str   | fixed value | line 23  |
| module.test_existing_path    | content_bytes | fixed value | line 24  |
| module.test_existing_path    | handler       | fixed value | line 26  |
| module.test_nonexistent_path | handler       | fixed value | line 15  |

## testable_server.py

| Scope                                         | Variable      | Role        | Location |
| :---------------------------------------------| :-------------| :-----------| :--------|
| module                                        | ERROR_PAGE    | fixed value | line 5   |
| module                                        | serverAddress | fixed value | line 67  |
| module                                        | server        | fixed value | line 68  |
| module.ApplicationRequestHandler.do_GET       | self          | fixed value | line 22  |
| module.ApplicationRequestHandler.do_GET       | url_path      | fixed value | line 24  |
| module.ApplicationRequestHandler.do_GET       | full_path     | fixed value | line 25  |
| module.ApplicationRequestHandler.do_GET       | msg           | fixed value | line 32  |
| module.ApplicationRequestHandler.handle_error | msg           | fixed value | line 45  |
| module.ApplicationRequestHandler.handle_error | self          | fixed value | line 45  |
| module.ApplicationRequestHandler.handle_error | content       | unknown     | line 46  |
| module.ApplicationRequestHandler.handle_file  | full_path     | fixed value | line 37  |
| module.ApplicationRequestHandler.handle_file  | given_path    | fixed value | line 37  |
| module.ApplicationRequestHandler.handle_file  | self          | fixed value | line 37  |
| module.ApplicationRequestHandler.handle_file  | reader        | fixed value | line 39  |
| module.ApplicationRequestHandler.handle_file  | content       | fixed value | line 40  |
| module.ApplicationRequestHandler.send_content | content       | fixed value | line 50  |
| module.ApplicationRequestHandler.send_content | self          | fixed value | line 50  |
| module.ApplicationRequestHandler.send_content | status        | fixed value | line 50  |

