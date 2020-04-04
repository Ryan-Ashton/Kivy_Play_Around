from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase

from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.icon_definitions import md_icons


class ContentNavigationDrawer(BoxLayout):
    pass

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''

    icon = StringProperty("android")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color



class TestNavigationDrawer(MDApp):


    def on_tab_switch(self, *args):
        """Called when switching tabs."""

    def build(self):
        return Builder.load_file("main.kv")


    def on_start(self):
        icons_item = {
            "download": "Download Data",
            "upload": "Upload Data",
            "trending-up": "What is trending up?",
            "trending-down": "What is trending down?",
            "share": "Share insights"
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

        icons = {
            "compare": "Compare against competitors",
            "eye": "Keep an eye on the competitors",
            "globe": "New competitors around the globe",
        }

        for i in icons.keys():
            self.root.ids.scroll.add_widget(
                ListItemWithCheckbox(text=icons[i], icon=i)
            )


class Tab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab'''


Product_Crawler = TestNavigationDrawer()

Product_Crawler.run()