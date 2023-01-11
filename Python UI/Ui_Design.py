import flet as ft
from flet import (
    flet,
    Image,
    Page,
    transform,
    UserControl, Column, Row, Text,
    Container, padding, alignment, border, animation, border_radius,
)


class Doughnut(UserControl):
    def animate_content(self, e):
        if e.control.scale != 1.25:
            e.control.scale = 1.25
        else:
            e.control.scale = 1
        e.control.update()

    def Ingredient(self, macro, amount, color, percent):
        return Container(
            scale=transform.Scale(0.9),
            alignment=alignment.center,
            width=56,
            height=100,
            border=border.all(1, "black"),
            padding=5,
            border_radius=border_radius.all(30),
            content=Column(
                horizontal_alignment="center",
                alignment="center",
                spacing=5,
                controls=[
                    Text(value=macro, size=10, weight="bold", color="black"),
                    Text(value=amount, size=8, italic=True, color="black"),
                    Container(
                        width=35,
                        height=35,
                        bgcolor=color,
                        border_radius=35,
                        alignment=alignment.center,
                        scale=transform.Scale(1),
                        animate_scale=animation.Animation(
                            duration=900, curve="bounceOut"
                        ),
                        on_hover=lambda e: self.animate_content(e),
                        content=Text(
                            value=percent,
                            color="black",
                            size=11,
                            # width=60,
                            text_align="center",
                            weight="bold",
                        )
                    )

                ]
            )
        )

    def mainContainer(self):
        # Main Container
        self.__main = Container(
            width=280,
            height=600,
            bgcolor="#fffeff",
            border_radius=30,
            padding=10,


        )

        # IMAGE
        self.IMG = Image(
            src='./Assets/ice1.png',
            width=230,
            height=230,
            offset=transform.Offset(0, -0.1),
            animate_offset=animation.Animation(),
        )

        self.test = self.Ingredient("Suger", "25 grams", "blue500", "13%")
        self.fat = self.Ingredient("Fat", "250 grams", "pink300", "11%")
        self.salt = self.Ingredient("Salt", "6 grams", "pink400", "8%")
        self.energy = self.Ingredient("Energy", "25 grams", "pink300", "131%")

        # main Colunm
        self.__main__col = Column(
            controls=[
                Container(
                    width=self.__main.width,
                    height=self.__main.height * 0.45,
                    bgcolor="#fdf5f1",
                    content=Column(
                        spacing=0,
                        controls=[
                            # IMG Row
                            Row(
                                alignment="center",
                                controls=[
                                    self.IMG
                                ]
                            ),
                            # Second Segment
                            Container(
                                padding=10,
                                width=self.__main.width,
                                height=self.__main.height * 0.54,
                                bgcolor="#fffeff",
                                border_radius=border_radius.only(20),

                                offset=transform.Offset(0, -0.1),
                                animate_offset=animation.Animation(),

                                alignment=alignment.center,
                                content=Column(
                                    spacing=0,
                                    controls=[
                                        Container(
                                            padding=5
                                        ),
                                        Row(
                                            controls=[
                                                Text(
                                                    "Nutritional Value",
                                                    color="black",
                                                    weight="bold",
                                                )
                                            ]
                                        ),
                                        Container(
                                            content=Row(
                                                alignment='center',
                                                vertical_alignment='center',
                                                # specing = 0,
                                                controls=[
                                                    self.test,
                                                    self.fat,
                                                    self.salt,
                                                    self.energy,
                                                ]
                                            )
                                        ),
                                        Row(
                                            controls=[
                                                Text(
                                                    "Discription",
                                                    color="black",
                                                    weight="bold",
                                                )
                                            ]
                                        ),
                                        Row(
                                            controls=[
                                                Text(
                                                    """Ice cream is a frozen dairy dessert\nobtained by freezing the ice cream mix\nwith continuous agitation. It contains\nmilk products, sweetening materials,\nstabilizers, colors, flavors, and egg\nproducts. Ice cream had its origins in\nEurope and was introduced later in\nthe United States where itdeveloped\n""",
                                                    color="black",
                                                    # weight="w300",
                                                    size=13,
                                                ),
                                            ]
                                        ),
                                        Row(
                                            alignment="center",
                                            controls=[
                                                Container(
                                                    width=self.__main.width * 0.8,
                                                    height=45,
                                                    border_radius=9,
                                                    border=border.all(
                                                        2, "black"),
                                                    content=Row(
                                                        alignment="spaceAround",
                                                        controls=[
                                                            Column(
                                                                alignment="center",
                                                                spacing=1,
                                                                controls=[
                                                                    Text(
                                                                        "₹ 90.78",
                                                                        color="black",
                                                                        weight="bold",
                                                                        size=12,
                                                                    )
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                )
                                            ]
                                        )
                                    ]
                                )

                            )
                        ]
                    )
                )
            ]
        )
        self.__main.content = self.__main__col

        return self.__main

    def build(self):
        return Column(
            expand=True,
            alignment="center",
            controls=[
                self.mainContainer(),
            ]
        )


def start(page: Page):
    page.title = "My APP"
    page.theme_mode = "dark"
    app = Doughnut()
    page.add(app)

    page.update()


if __name__ == '__main__':
    flet.app(target=start, assets_dir='Assets')

# 30.46 Time Line
