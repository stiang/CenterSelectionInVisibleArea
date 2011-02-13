#!/usr/bin/python
# -*- coding: utf-8 -*-
import sublime_plugin


class CenterSelectionInVisibleAreaCommand(sublime_plugin.TextCommand):

    def isEnabled(self, edit, args):
        return self.view.sel()

    def run(self, edit, args=None):
        view = self.view
        view.show(view.sel()[0])

        (selection_on, _) = view.rowcol(view.sel()[0].begin())

        visible = view.visible_region()

        (first_visible, _) = view.rowcol(visible.begin())
        (last_visible, _) = view.rowcol(visible.end())

        centered = first_visible + (last_visible - first_visible) / 2

        diff = centered - selection_on

        sel = view.sel()[0]

        for i in range(abs(diff)):
            if sel.begin() \
                <= view.line(view.visible_region().begin()).begin() \
                or sel.begin() \
                >= view.line(view.visible_region().begin()).end():
                view.run_command('scroll_lines', {'amount': (1 if diff
                                 >= 0 else -1)})
                sel = view.sel()[0]
            else:
                break


