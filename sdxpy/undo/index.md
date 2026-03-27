# Undo and Redo

## headless.py

| Variable | Scope | Role |
|---|---|---|
| lines | module.HeadlessApp.__init__ | fixed value |
| self | module.HeadlessApp.__init__ | fixed value |
| size | module.HeadlessApp.__init__ | fixed value |
| key | module.HeadlessApp._add_log | fixed value |
| self | module.HeadlessApp._add_log | fixed value |
| self | module.HeadlessApp._make_window | fixed value |
| self | module.HeadlessApp.get_log | fixed value |
| keystrokes | module.HeadlessScreen.__init__ | fixed value |
| self | module.HeadlessScreen.__init__ | fixed value |
| size | module.HeadlessScreen.__init__ | fixed value |
| self | module.HeadlessScreen.__str__ | fixed value |
| col | module.HeadlessScreen.addstr | fixed value |
| row | module.HeadlessScreen.addstr | fixed value |
| self | module.HeadlessScreen.addstr | fixed value |
| text | module.HeadlessScreen.addstr | fixed value |
| self | module.HeadlessScreen.display | fixed value |
| self | module.HeadlessScreen.erase | fixed value |
| self | module.HeadlessScreen.getkey | fixed value |
| key | module.HeadlessScreen.getkey | fixed value |
| col | module.HeadlessScreen.move | fixed value |
| row | module.HeadlessScreen.move | fixed value |
| self | module.HeadlessScreen.move | fixed value |
| screen | module.HeadlessWindow.__init__ | fixed value |
| self | module.HeadlessWindow.__init__ | fixed value |
| size | module.HeadlessWindow.__init__ | fixed value |

## test_headless.py

| Variable | Scope | Role |
|---|---|---|
| size | module.test_move_right | fixed value |
| lines | module.test_move_right | fixed value |
| keys | module.test_move_right | fixed value |
| screen | module.test_move_right | fixed value |
| app | module.test_move_right | fixed value |
| size | module.test_no_keystrokes | fixed value |
| lines | module.test_no_keystrokes | fixed value |
| keys | module.test_no_keystrokes | fixed value |
| screen | module.test_no_keystrokes | fixed value |
| app | module.test_no_keystrokes | fixed value |
| size | module.test_scroll_down | fixed value |
| lines | module.test_scroll_down | fixed value |
| keys | module.test_scroll_down | fixed value |
| screen | module.test_scroll_down | fixed value |
| app | module.test_scroll_down | fixed value |

## insert_delete.py

| Variable | Scope | Role |
|---|---|---|
| INSERTABLE | module.InsertDeleteApp | fixed value |
| self | module.InsertDeleteApp._do_DELETE | fixed value |
| key | module.InsertDeleteApp._do_INSERT | fixed value |
| self | module.InsertDeleteApp._do_INSERT | fixed value |
| self | module.InsertDeleteApp._get_key | fixed value |
| key | module.InsertDeleteApp._get_key | fixed value |
| self | module.InsertDeleteApp._interact | fixed value |
| family | module.InsertDeleteApp._interact | fixed value |
| key | module.InsertDeleteApp._interact | fixed value |
| name | module.InsertDeleteApp._interact | fixed value |
| self | module.InsertDeleteApp._make_buffer | fixed value |
| pos | module.InsertDeleteBuffer.delete | fixed value |
| self | module.InsertDeleteBuffer.delete | fixed value |
| line | module.InsertDeleteBuffer.delete | unknown |
| char | module.InsertDeleteBuffer.insert | fixed value |
| pos | module.InsertDeleteBuffer.insert | fixed value |
| self | module.InsertDeleteBuffer.insert | fixed value |
| line | module.InsertDeleteBuffer.insert | unknown |

## test_insert_delete.py

| Variable | Scope | Role |
|---|---|---|
| keys | module.make_fixture | fixed value |
| lines | module.make_fixture | fixed value |
| size | module.make_fixture | fixed value |
| screen | module.make_fixture | fixed value |
| app | module.make_fixture | fixed value |
| app | module.test_delete_empty_line | fixed value |
| app | module.test_delete_left_edge | fixed value |
| app | module.test_delete_middle | fixed value |
| app | module.test_delete_right | fixed value |
| app | module.test_insert_upper_left | fixed value |

## history.py

| Variable | Scope | Role |
|---|---|---|
| keystrokes | module.HistoryApp.__init__ | fixed value |
| self | module.HistoryApp.__init__ | fixed value |
| size | module.HistoryApp.__init__ | fixed value |
| self | module.HistoryApp._do_DELETE | fixed value |
| col | module.HistoryApp._do_DELETE | fixed value |
| row | module.HistoryApp._do_DELETE | fixed value |
| char | module.HistoryApp._do_DELETE | fixed value |
| key | module.HistoryApp._do_INSERT | fixed value |
| self | module.HistoryApp._do_INSERT | fixed value |
| pos | module.HistoryApp._do_INSERT | fixed value |
| self | module.HistoryApp.get_history | fixed value |

## action.py

| Variable | Scope | Role |
|---|---|---|
| app | module.Action.__init__ | fixed value |
| self | module.Action.__init__ | fixed value |
| self | module.Action.do | fixed value |
| self | module.Action.save | fixed value |
| self | module.Action.undo | fixed value |
| INSERTABLE | module.ActionApp | fixed value |
| keystrokes | module.ActionApp.__init__ | fixed value |
| self | module.ActionApp.__init__ | fixed value |
| size | module.ActionApp.__init__ | fixed value |
| key | module.ActionApp._add_log | fixed value |
| self | module.ActionApp._add_log | fixed value |
| key | module.ActionApp._do_CONTROL_X | fixed value |
| self | module.ActionApp._do_CONTROL_X | fixed value |
| key | module.ActionApp._do_DELETE | fixed value |
| self | module.ActionApp._do_DELETE | fixed value |
| key | module.ActionApp._do_INSERT | fixed value |
| self | module.ActionApp._do_INSERT | fixed value |
| key | module.ActionApp._do_KEY_DOWN | fixed value |
| self | module.ActionApp._do_KEY_DOWN | fixed value |
| key | module.ActionApp._do_KEY_LEFT | fixed value |
| self | module.ActionApp._do_KEY_LEFT | fixed value |
| key | module.ActionApp._do_KEY_RIGHT | fixed value |
| self | module.ActionApp._do_KEY_RIGHT | fixed value |
| key | module.ActionApp._do_KEY_UP | fixed value |
| self | module.ActionApp._do_KEY_UP | fixed value |
| self | module.ActionApp._get_key | fixed value |
| key | module.ActionApp._get_key | fixed value |
| self | module.ActionApp._interact | fixed value |
| family | module.ActionApp._interact | fixed value |
| key | module.ActionApp._interact | fixed value |
| name | module.ActionApp._interact | fixed value |
| action | module.ActionApp._interact | fixed value |
| self | module.ActionApp.get_history | fixed value |
| app | module.Delete.__init__ | fixed value |
| pos | module.Delete.__init__ | fixed value |
| self | module.Delete.__init__ | fixed value |
| self | module.Delete.__str__ | fixed value |
| self | module.Delete.do | fixed value |
| self | module.Delete.undo | fixed value |
| self | module.Exit.__str__ | fixed value |
| self | module.Exit.do | fixed value |
| app | module.Insert.__init__ | fixed value |
| char | module.Insert.__init__ | fixed value |
| pos | module.Insert.__init__ | fixed value |
| self | module.Insert.__init__ | fixed value |
| self | module.Insert.__str__ | fixed value |
| self | module.Insert.do | fixed value |
| self | module.Insert.undo | fixed value |
| app | module.Move.__init__ | fixed value |
| direction | module.Move.__init__ | fixed value |
| self | module.Move.__init__ | fixed value |
| self | module.Move.__str__ | fixed value |
| self | module.Move.do | fixed value |
| self | module.Move.undo | fixed value |

## cursor.py

| Variable | Scope | Role |
|---|---|---|
| buffer | module.Cursor.__init__ | fixed value |
| self | module.Cursor.__init__ | fixed value |
| window | module.Cursor.__init__ | fixed value |
| self | module.Cursor._fix | fixed value |
| direction | module.Cursor.act | fixed value |
| self | module.Cursor.act | fixed value |
| self | module.Cursor.down | fixed value |
| self | module.Cursor.left | fixed value |
| pos | module.Cursor.move_to | fixed value |
| self | module.Cursor.move_to | fixed value |
| self | module.Cursor.pos | fixed value |
| self | module.Cursor.right | fixed value |
| self | module.Cursor.up | fixed value |

## undoable.py

| Variable | Scope | Role |
|---|---|---|
| self | module.Undo.__str__ | fixed value |
| self | module.Undo.do | fixed value |
| action | module.Undo.do | fixed value |
| self | module.Undo.save | fixed value |
| key | module.UndoableApp._do_UNDO | fixed value |
| self | module.UndoableApp._do_UNDO | fixed value |
| self | module.UndoableApp._interact | fixed value |
| family | module.UndoableApp._interact | fixed value |
| key | module.UndoableApp._interact | fixed value |
| name | module.UndoableApp._interact | fixed value |
| action | module.UndoableApp._interact | fixed value |

## test_undoable.py

| Variable | Scope | Role |
|---|---|---|
| LINES | module | fixed value |
| app | module.get_screen | fixed value |
| keys | module.make_fixture | fixed value |
| lines | module.make_fixture | fixed value |
| size | module.make_fixture | fixed value |
| screen | module.make_fixture | fixed value |
| app | module.make_fixture | fixed value |
| app | module.test_insert_undo | fixed value |

