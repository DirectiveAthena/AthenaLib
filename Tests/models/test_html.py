# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaLib.HTML.models.html import HTMLElement
import AthenaLib.HTML.models.html_library as HTMLElementLib

# Custom Packages
from Tests.test_structure import TestStructure

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestHTML(TestStructure):
    def test_SingleElement(self):
        self.subtest_multiple_cases(
            # result    object_factory
            ("<span>",              lambda: HTMLElement(name="span").to_tag()),
            ("""<span class="test">""", lambda: HTMLElement(name="span", classes=["test"]).to_tag()),
            ("""<span class="test test2">""", lambda: HTMLElement(name="span", classes=["test", "test2"]).to_tag()),
            ("""<span id="test">""", lambda: HTMLElement(name="span", id_str="test").to_tag()),
            ("""<span class="test test2" id="test">""", lambda: HTMLElement(name="span", classes=["test", "test2"],
                                                                            id_str="test").to_tag()),
        )

    def test_NestedElement(self):
        self.assertEqual(
            "<span><p>Hello</p></span>",
            str(HTMLElementLib.Span(HTMLElementLib.P("Hello")))
        )
        self.assertEqual(
            '<span class="test"><p>Hello</p></span>',
            str(HTMLElementLib.Span(
                HTMLElementLib.P("Hello"),
                classes=["test"]
            ))
        )
        self.assertEqual(
            '<span class="test"><p class="test2">Hello</p></span>',
            str(HTMLElementLib.Span(
                HTMLElementLib.P(
                    "Hello",
                    classes=["test2"]
                ),
                classes=["test"]
            ))
        )
        element = HTMLElementLib.Span(classes=["test"])
        element.wraps = [HTMLElementLib.P("Hello")]

        self.assertEqual(
            '<span class="test"><p>Hello</p></span>',
            str(element)
        )

    def test_to_dict(self):
        self.assertEqual(
            {
                'accesskey': False,
                'classes': ['test', 'test2'],
                'contenteditable': False,
                'dir': False,
                'draggable': False,
                'hidden': False,
                'id': 'test',
                'lang': False,
                'name': 'span',
                'spellcheck': False,
                'style': 'color:red;',
                'tabindex': False,
                'title': False,
                'translate': False,
                'wraps': []
            },
            HTMLElement(name="span", classes=["test", "test2"], id_str="test", style="color:red;").to_dict()
        )
