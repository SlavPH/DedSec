#!/usr/bin/env python3

## DedSec app without functions
## You can add your functions
## github.com/SlavPH

import sys
from kivymd.app import MDApp
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.fitimage.fitimage import FitImage
from kivymd.uix.navigationdrawer import (
    MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerHeader,
    MDNavigationDrawerLabel,
    MDNavigationDrawerDivider,
    MDNavigationDrawerItem
)
from kivymd.uix.list import (
    IRightBodyTouch, 
    OneLineAvatarIconListItem, 
    OneLineAvatarListItem , 
    ImageLeftWidget
)


class BaseNavigationDrawerItem(MDNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.radius = 24
        self.text_color = "#4a4939"
        self.icon_color = "#4a4939"
        self.focus_color = "#e7e4c0"


class DrawerLabelItem(BaseNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.focus_behavior = False
        self._no_ripple_effect = True
        self.selected_color = "#546d7a"


class DrawerClickableItem(BaseNavigationDrawerItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._no_ripple_effect = True
        self.ripple_color = "#FFFFFF"
        self.selected_color = "#FF000"


class DedSecApp(MDApp):
 
    def nav_drawer_open(self, *args):
        nav_drawer = self.root.children[0].ids.nav_drawer
        nav_drawer.set_state("open")

    # Build method
    def build(self):
        # Theme
        self.theme_cls.primary_palette = "BlueGray"
        self.theme_cls.theme_style = "Dark"
 
        # Home screen
        Home = MDScreen()

        # Top toolbar
        self.TopToolbar = MDTopAppBar(
            pos_hint = {"top":1},
            use_overflow = True,
            opposite_colors = True,
            left_action_items = [
                ["skull-scan", lambda x: self.nav_drawer_open(), "Menu", "Menu"]
            ],
            right_action_items = [
                ["location-exit", lambda _:sys.exit(), "Exit", "Exit"],
            ]
        )

        # Navigation layout
        self.NavigationLayout = MDNavigationLayout(
            MDNavigationDrawer(
                MDNavigationDrawerMenu(
                    MDNavigationDrawerHeader(
                        title="DedSec App",
                        title_color="#546d7a",
                        text="Made by GothPH",
                        text_font_style = "Overline",
                        text_font_size = "15sp",
                        spacing = "2dp",
                        padding = ("12dp", "0dp", "10dp", "26dp")
                    ),
                    MDBoxLayout(
                        FitImage(
                            size_hint_y=.3,
                            source='icon.png',
                        ),
                        size_hint_y=None,
                        height="200dp",
                        orientation='vertical',
                    ),
                    MDNavigationDrawerLabel(
                        text="Status",
                    ),
                    DrawerClickableItem(
                        icon="account-group",
                        right_text="935",
                        text_right_color="#4a4939",
                        text="Followers",
                    ),
                    DrawerClickableItem(
                        icon="meter-electric",
                        right_text="182",
                        text_right_color="#4a4939",
                        text="BotNets",
                    ),
                    MDNavigationDrawerDivider(),
                    MDNavigationDrawerLabel(
                        text="About",
                    ),
                    DrawerLabelItem(
                        icon="github",
                        text="Github.com/SlavPH",
                    ),
                    DrawerLabelItem(
                        icon="information-outline",
                        text="Version 1.0",
                    ),
                ),
                id="nav_drawer",
                radius=(0, 0, 0, 0),
            ),
        )

        self.option1 = MDCard(
            MDIconButton(
                icon="skull",
                pos_hint={"top": 1, "right": 1}
            ),
            MDLabel(
                text="Bomber",
                adaptive_size=True,
                color="white",
                pos=("12dp", "12dp"),
            ),
            style = "elevated",
            focus_behavior = True,
            ripple_behavior = True,
            size_hint=(0.2, 0.2),
            pos_hint = {"center_x": 0.2, "center_y": 0.7} ,
            elevation=6,
            unfocus_color="darkgrey",
            md_bg_color="darkgrey",
            focus_color="#546d7a",
            on_release = lambda _: print("card1")
        )

        self.option2 = MDCard(
            MDIconButton(
                icon="skull",
                pos_hint={"top": 1, "right": 1}
            ),
            MDLabel(
                text="DDos",
                adaptive_size=True,
                color="white",
                pos=("12dp", "12dp"),
            ),
            focus_behavior = True,
            ripple_behavior = True,
            size_hint = (0.2, 0.2),
            pos_hint = {"center_x": 0.5, "center_y": 0.7} ,
            elevation=6,
            unfocus_color="darkgrey",
            md_bg_color="darkgrey",
            focus_color="#546d7a",
            on_release = lambda _: print("card2")
        )

        self.option3 = MDCard(
            MDIconButton(
                icon="skull",
                pos_hint={"top": 1, "right": 1}
            ),
            MDLabel(
                text="Profiler",
                adaptive_size=True,
                color="white",
                pos=("12dp", "12dp"),
            ),
            focus_behavior = True,
            ripple_behavior = True,
            size_hint = (0.2, 0.2),
            pos_hint = {"center_x": 0.8, "center_y": 0.7} ,
            elevation=6,
            unfocus_color="darkgrey",
            md_bg_color="darkgrey",
            focus_color="#546d7a",
            on_release = lambda _: print("card3")
        )

        # Add widgets
        Home.add_widget(self.TopToolbar)
        Home.add_widget(self.option1)
        Home.add_widget(self.option2)
        Home.add_widget(self.option3)
        Home.add_widget(self.NavigationLayout)
        
        return Home

DedSecApp().run()
