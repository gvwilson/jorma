# Serving Web Pages

## requests_example.py

| Variable | Scope | Role |
|---|---|---|
| response | module | fixed value |

## basic_server.py

| Variable | Scope | Role |
|---|---|---|
| PAGE | module | fixed value |
| server_address | module | fixed value |
| server | module | fixed value |
| self | module.RequestHandler.do_GET | fixed value |
| content | module.RequestHandler.do_GET | fixed value |

## file_server.py

| Variable | Scope | Role |
|---|---|---|
| ERROR_PAGE | module | fixed value |
| serverAddress | module | fixed value |
| server | module | fixed value |
| self | module.RequestHandler.do_GET | fixed value |
| url_path | module.RequestHandler.do_GET | fixed value |
| full_path | module.RequestHandler.do_GET | fixed value |
| msg | module.RequestHandler.do_GET | fixed value |
| msg | module.RequestHandler.handle_error | fixed value |
| self | module.RequestHandler.handle_error | fixed value |
| content | module.RequestHandler.handle_error | unknown |
| full_path | module.RequestHandler.handle_file | fixed value |
| given_path | module.RequestHandler.handle_file | fixed value |
| self | module.RequestHandler.handle_file | fixed value |
| reader | module.RequestHandler.handle_file | fixed value |
| content | module.RequestHandler.handle_file | fixed value |
| content | module.RequestHandler.send_content | fixed value |
| self | module.RequestHandler.send_content | fixed value |
| status | module.RequestHandler.send_content | fixed value |

## mock_handler.py

| Variable | Scope | Role |
|---|---|---|
| path | module.MockRequestHandler.__init__ | fixed value |
| self | module.MockRequestHandler.__init__ | fixed value |
| self | module.MockRequestHandler.end_headers | fixed value |
| key | module.MockRequestHandler.send_header | fixed value |
| self | module.MockRequestHandler.send_header | fixed value |
| value | module.MockRequestHandler.send_header | fixed value |
| self | module.MockRequestHandler.send_response | fixed value |
| status | module.MockRequestHandler.send_response | fixed value |

## testable_server.py

| Variable | Scope | Role |
|---|---|---|
| ERROR_PAGE | module | fixed value |
| serverAddress | module | fixed value |
| server | module | fixed value |
| self | module.ApplicationRequestHandler.do_GET | fixed value |
| url_path | module.ApplicationRequestHandler.do_GET | fixed value |
| full_path | module.ApplicationRequestHandler.do_GET | fixed value |
| msg | module.ApplicationRequestHandler.do_GET | fixed value |
| msg | module.ApplicationRequestHandler.handle_error | fixed value |
| self | module.ApplicationRequestHandler.handle_error | fixed value |
| content | module.ApplicationRequestHandler.handle_error | unknown |
| full_path | module.ApplicationRequestHandler.handle_file | fixed value |
| given_path | module.ApplicationRequestHandler.handle_file | fixed value |
| self | module.ApplicationRequestHandler.handle_file | fixed value |
| reader | module.ApplicationRequestHandler.handle_file | fixed value |
| content | module.ApplicationRequestHandler.handle_file | fixed value |
| content | module.ApplicationRequestHandler.send_content | fixed value |
| self | module.ApplicationRequestHandler.send_content | fixed value |
| status | module.ApplicationRequestHandler.send_content | fixed value |

## test_testable_server.py

| Variable | Scope | Role |
|---|---|---|
| fs | module.test_existing_path | fixed value |
| content_str | module.test_existing_path | fixed value |
| content_bytes | module.test_existing_path | fixed value |
| handler | module.test_existing_path | fixed value |
| handler | module.test_nonexistent_path | fixed value |

