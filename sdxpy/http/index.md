# Variable Role Analysis: http

## basic_server.py

```

[module]
  PAGE                     fixed value             (line 3)
  server_address           fixed value             (line 17)
  server                   fixed value             (line 18)

[module.RequestHandler.do_GET]
  self                     fixed value             (line 6)
  content                  fixed value             (line 7)
```

## file_server.py

```

[module]
  ERROR_PAGE               fixed value             (line 6)
  serverAddress            fixed value             (line 64)
  server                   fixed value             (line 65)

[module.RequestHandler.do_GET]
  self                     fixed value             (line 23)
  url_path                 fixed value             (line 25)
  full_path                fixed value             (line 26)
  msg                      fixed value             (line 33)

[module.RequestHandler.handle_error]
  msg                      fixed value             (line 48)
  self                     fixed value             (line 48)
  content                  unknown                 (line 49)

[module.RequestHandler.handle_file]
  full_path                fixed value             (line 38)
  given_path               fixed value             (line 38)
  self                     fixed value             (line 38)
  reader                   fixed value             (line 40)
  content                  fixed value             (line 41)

[module.RequestHandler.send_content]
  content                  fixed value             (line 55)
  self                     fixed value             (line 55)
  status                   fixed value             (line 55)
```

## mock_handler.py

```

[module.MockRequestHandler.__init__]
  path                     fixed value             (line 4)
  self                     fixed value             (line 4)

[module.MockRequestHandler.end_headers]
  self                     fixed value             (line 18)

[module.MockRequestHandler.send_header]
  key                      fixed value             (line 13)
  self                     fixed value             (line 13)
  value                    fixed value             (line 13)

[module.MockRequestHandler.send_response]
  self                     fixed value             (line 10)
  status                   fixed value             (line 10)
```

## requests_example.py

```

[module]
  response                 fixed value             (line 3)
```

## test_testable_server.py

```

[module.test_existing_path]
  fs                       fixed value             (line 22)
  content_str              fixed value             (line 23)
  content_bytes            fixed value             (line 24)
  handler                  fixed value             (line 26)

[module.test_nonexistent_path]
  handler                  fixed value             (line 15)
```

## testable_server.py

```

[module]
  ERROR_PAGE               fixed value             (line 5)
  serverAddress            fixed value             (line 67)
  server                   fixed value             (line 68)

[module.ApplicationRequestHandler.do_GET]
  self                     fixed value             (line 22)
  url_path                 fixed value             (line 24)
  full_path                fixed value             (line 25)
  msg                      fixed value             (line 32)

[module.ApplicationRequestHandler.handle_error]
  msg                      fixed value             (line 45)
  self                     fixed value             (line 45)
  content                  unknown                 (line 46)

[module.ApplicationRequestHandler.handle_file]
  full_path                fixed value             (line 37)
  given_path               fixed value             (line 37)
  self                     fixed value             (line 37)
  reader                   fixed value             (line 39)
  content                  fixed value             (line 40)

[module.ApplicationRequestHandler.send_content]
  content                  fixed value             (line 50)
  self                     fixed value             (line 50)
  status                   fixed value             (line 50)
```

