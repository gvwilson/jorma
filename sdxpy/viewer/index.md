# A File Viewer

## first_curses.py

| Variable | Scope | Role |
|---|---|---|
| stdscr | module.main | fixed value |

## util.py

| Variable | Scope | Role |
|---|---|---|
| LOG | module | fixed value |
| ROW | module | fixed value |
| COL | module | fixed value |
| args | module.log | fixed value |
| num_lines | module.make_lines | fixed value |
| result | module.make_lines | log |
| i | module.make_lines | stepper |
| ch | module.make_lines | most-recent holder |
| filename | module.open_log | fixed value |
| LOG | module.open_log | fixed value |
| logfile | module.start | fixed value |
| num_lines | module.start | fixed value |
| size | module.start | lazy value |
| lines | module.start | fixed value |

## logging_curses.py

| Variable | Scope | Role |
|---|---|---|
| stdscr | module.main | fixed value |
| key | module.main | most-recent holder |

## show_lines.py

| Variable | Scope | Role |
|---|---|---|
| logfile | module | fixed value |
| num_lines | module | fixed value |
| lines | module | fixed value |
| lines | module.main | fixed value |
| stdscr | module.main | fixed value |
| line | module.main | stepper |
| y | module.main | stepper |
| key | module.main | most-recent holder |

## use_window.py

| Variable | Scope | Role |
|---|---|---|
| logfile | module | fixed value |
| num_lines | module | fixed value |
| lines | module | fixed value |
| screen | module.Window.__init__ | fixed value |
| self | module.Window.__init__ | fixed value |
| lines | module.Window.draw | fixed value |
| self | module.Window.draw | fixed value |
| line | module.Window.draw | stepper |
| y | module.Window.draw | stepper |
| lines | module.main | fixed value |
| stdscr | module.main | fixed value |
| window | module.main | fixed value |
| key | module.main | most-recent holder |

## size_window.py

| Variable | Scope | Role |
|---|---|---|
| lines | module | fixed value |
| size | module | fixed value |
| screen | module.Window.__init__ | fixed value |
| self | module.Window.__init__ | fixed value |
| size | module.Window.__init__ | fixed value |
| lines | module.Window.draw | fixed value |
| self | module.Window.draw | fixed value |
| line | module.Window.draw | stepper |
| y | module.Window.draw | stepper |
| lines | module.main | fixed value |
| size | module.main | fixed value |
| stdscr | module.main | fixed value |
| window | module.main | fixed value |
| key | module.main | most-recent holder |

## cursor_const.py

| Variable | Scope | Role |
|---|---|---|
| lines | module | fixed value |
| size | module | fixed value |
| screen | module.Window.__init__ | fixed value |
| self | module.Window.__init__ | fixed value |
| size | module.Window.__init__ | fixed value |
| lines | module.Window.draw | fixed value |
| self | module.Window.draw | fixed value |
| line | module.Window.draw | stepper |
| y | module.Window.draw | stepper |
| self | module.Window.size | fixed value |
| lines | module.main | fixed value |
| size | module.main | fixed value |
| stdscr | module.main | fixed value |
| window | module.main | fixed value |
| key | module.main | most-recent holder |

## move_cursor.py

| Variable | Scope | Role |
|---|---|---|
| lines | module | fixed value |
| size | module | fixed value |
| self | module.Cursor.__init__ | fixed value |
| self | module.Cursor.down | fixed value |
| self | module.Cursor.left | fixed value |
| self | module.Cursor.pos | fixed value |
| self | module.Cursor.right | fixed value |
| self | module.Cursor.up | fixed value |
| lines | module.main | fixed value |
| size | module.main | fixed value |
| stdscr | module.main | fixed value |
| window | module.main | fixed value |
| cursor | module.main | fixed value |
| key | module.main | most-recent holder |

## call_example.py

| Variable | Scope | Role |
|---|---|---|
| p | module | fixed value |
| result | module | fixed value |
| self | module.Pretend.__call__ | fixed value |
| value | module.Pretend.__call__ | fixed value |
| increment | module.Pretend.__init__ | fixed value |
| self | module.Pretend.__init__ | fixed value |

## main_app.py

| Variable | Scope | Role |
|---|---|---|
| lines | module | fixed value |
| size | module | fixed value |
| app | module | fixed value |
| screen | module.MainApp.__call__ | fixed value |
| self | module.MainApp.__call__ | fixed value |
| lines | module.MainApp.__init__ | fixed value |
| self | module.MainApp.__init__ | fixed value |
| size | module.MainApp.__init__ | fixed value |
| self | module.MainApp._run | fixed value |
| key | module.MainApp._run | most-recent holder |
| screen | module.MainApp._setup | fixed value |
| self | module.MainApp._setup | fixed value |

## dispatch_keys.py

| Variable | Scope | Role |
|---|---|---|
| lines | module | fixed value |
| size | module | fixed value |
| app | module | fixed value |
| TRANSLATE | module.DispatchApp | fixed value |
| lines | module.DispatchApp.__init__ | fixed value |
| self | module.DispatchApp.__init__ | fixed value |
| size | module.DispatchApp.__init__ | fixed value |
| self | module.DispatchApp._do_CONTROL_X | fixed value |
| self | module.DispatchApp._do_KEY_DOWN | fixed value |
| self | module.DispatchApp._do_KEY_LEFT | fixed value |
| self | module.DispatchApp._do_KEY_RIGHT | fixed value |
| self | module.DispatchApp._do_KEY_UP | fixed value |
| self | module.DispatchApp._interact | fixed value |
| key | module.DispatchApp._interact | unknown |
| name | module.DispatchApp._interact | fixed value |
| self | module.DispatchApp._run | fixed value |

## buffer_class.py

| Variable | Scope | Role |
|---|---|---|
| lines | module | fixed value |
| size | module | fixed value |
| app | module | fixed value |
| lines | module.Buffer.__init__ | fixed value |
| self | module.Buffer.__init__ | fixed value |
| self | module.Buffer.lines | fixed value |
| lines | module.BufferApp.__init__ | fixed value |
| self | module.BufferApp.__init__ | fixed value |
| size | module.BufferApp.__init__ | fixed value |
| self | module.BufferApp._make_buffer | fixed value |
| self | module.BufferApp._make_cursor | fixed value |
| self | module.BufferApp._make_window | fixed value |
| self | module.BufferApp._run | fixed value |
| screen | module.BufferApp._setup | fixed value |
| self | module.BufferApp._setup | fixed value |

## clip_cursor.py

| Variable | Scope | Role |
|---|---|---|
| lines | module | fixed value |
| size | module | fixed value |
| app | module | fixed value |
| self | module.ClipApp._make_buffer | fixed value |
| self | module.ClipApp._make_cursor | fixed value |
| row | module.ClipBuffer.ncol | fixed value |
| self | module.ClipBuffer.ncol | fixed value |
| self | module.ClipBuffer.nrow | fixed value |
| buffer | module.ClipCursor.__init__ | fixed value |
| self | module.ClipCursor.__init__ | fixed value |
| self | module.ClipCursor.down | fixed value |
| self | module.ClipCursor.left | fixed value |
| self | module.ClipCursor.right | fixed value |
| self | module.ClipCursor.up | fixed value |

## clip_fixed.py

| Variable | Scope | Role |
|---|---|---|
| lines | module | fixed value |
| size | module | fixed value |
| app | module | fixed value |
| self | module.ClipAppFixed._make_cursor | fixed value |
| self | module.ClipCursorFixed._fix | fixed value |
| self | module.ClipCursorFixed.down | fixed value |
| self | module.ClipCursorFixed.up | fixed value |

## viewport.py

| Variable | Scope | Role |
|---|---|---|
| lines | module | fixed value |
| size | module | fixed value |
| app | module | fixed value |
| self | module.ViewportApp._make_buffer | fixed value |
| self | module.ViewportApp._make_cursor | fixed value |
| self | module.ViewportApp._run | fixed value |
| screen_pos | module.ViewportApp._run | most-recent holder |
| lines | module.ViewportBuffer.__init__ | fixed value |
| self | module.ViewportBuffer.__init__ | fixed value |
| self | module.ViewportBuffer._bottom | fixed value |
| self | module.ViewportBuffer.lines | fixed value |
| col | module.ViewportBuffer.scroll | fixed value |
| row | module.ViewportBuffer.scroll | fixed value |
| self | module.ViewportBuffer.scroll | fixed value |
| height | module.ViewportBuffer.set_height | fixed value |
| self | module.ViewportBuffer.set_height | fixed value |
| pos | module.ViewportBuffer.transform | fixed value |
| self | module.ViewportBuffer.transform | fixed value |
| result | module.ViewportBuffer.transform | fixed value |
| buffer | module.ViewportCursor.__init__ | fixed value |
| self | module.ViewportCursor.__init__ | fixed value |
| window | module.ViewportCursor.__init__ | fixed value |
| self | module.ViewportCursor._fix | fixed value |
| self | module.ViewportCursor.left | fixed value |
| self | module.ViewportCursor.right | fixed value |

