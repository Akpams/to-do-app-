import flet as ft
from flet import *
from custom_checkbox import CustomCheckBox


def main(page: ft.Page):
    BG="#041955"
    FWG="#97b4ff"
    FG='#3450a1'
    PINK="#eb06ff"
    tasks=ft.Column(
        height =300,
        scroll="auto",
    
        # controls=[ft.Container(height=60, width=400, bgcolor="blue")],
    )
    def restore(e):
        page_2.controls[0].width =400
        page_2.controls[0].scale=ft.transform.Scale(1, alignment=ft.alignment.center_right)
        page_2.update()
    def shrink(e):
        page_2.controls[0].width =120
        page_2.controls[0].scale=ft.transform.Scale(0.8, alignment=ft.alignment.center_right)
        page_2.controls[0].border_radius=ft.border_radius.only(35,0,35,0)
        page_2.update()
    for i in range(10):
        tasks.controls.append(
            ft.Container(border_radius=10,
                         height=60, 
                         width=380, 
                         bgcolor=BG,
                         padding =ft.padding.only(left=10, top=20),
                        content=CustomCheckBox(
                            color=PINK,
                            label="my daily tasks",
                        )
                         ),
            )
        


    category_card=ft.Row(
        scroll="auto"

    )
    
    create_task_view=ft.Container(
        content=ft.Container(
            ft.Container(
                on_click=lambda _:page.go('/'),
                height=50, width=50,
                content=ft.Text("x", color="blue"),
            )
        )
    )
    categories=["Business", 'Family', "Work", "Church"]
    for i,category in enumerate(categories):
        category_card.controls.append(
            ft.Container(
                bgcolor=BG,
                width=180,
                height=110,
                padding=8,
                border_radius=20,
                content=ft.Column(
                    controls=[
                        ft.Text("40 Tasks",color="white" ),
                        ft.Text(category, color="white"),
                        ft.Container(
                            bgcolor="white12",
                            width=150,
                            height=7,
                            border_radius=10,
                            padding=ft.padding.only(right=i*20),
                            content=ft.Container(
                                bgcolor=PINK,
                            ),
                        )
                    ]
                )
                
            )
        )
    first_page_content=ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(alignment="spaceBetween",
                    controls=[
                        ft.Container(on_click=lambda e: shrink(e),
                            content=ft.Icon( ft.icons.MENU, color=ft.colors.WHITE)
                        ),
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.SEARCH, color=ft.colors.WHITE),
                                ft.Icon(ft.icons.NOTIFICATIONS, color=ft.colors.WHITE)
                            ]
                        )

                    ]
                ),
                ft.Container(height=20),
                ft.Text(value="What\'s up, Dear!!!", color="white"),
                ft.Text(value="CATEGORIES",color="white"), 
                ft.Container(
                    padding =ft.padding.only(top=10, bottom=20,),
                    content=category_card
                ),
                ft.Container(height=20),
                ft.Text("TODAY'S TASKS", color="white"),
                ft.Stack(
                    controls=[
                        tasks,
                        ft.FloatingActionButton(bgcolor=FWG,
                            bottom=20,right=20,
                            icon=ft.icons.ADD, on_click=lambda _: page.go("/create_task"),
                        )
                    ]
                )

            ],
        ),
    )
    page_1=ft.Container(
        width=400,
        height=680,
        bgcolor=BG,
        border_radius=35,
        padding =ft.padding.only(left=50,top=60, right=200),
        content=ft.Column(
            controls=[
                Row(alignment ="end",
                    controls=[
                        ft.Container(border_radius=20,padding=ft.padding.only(top=1, left=1),
                    height=30,width =30,border=ft.border.all(color="white", width=1),
                    content=ft.Text(" <", color="white"),
                    on_click=lambda e: restore(e),
                )
                    ]
                ), 
                Container(height=20),
                Text('James\nTech', size=15, weight="bold", color="white"),
            ]
        )
    )
    page_2=ft.Row(alignment='end',
        controls=[
            ft.Container(
                width=300,
                height=680,
                bgcolor=FG,
                animate =ft.animation.Animation(600,ft.AnimationCurve.DECELERATE),
                animate_scale=ft.animation.Animation(400, curve="decelerate"),
                border_radius=25,
                padding=ft.padding.only(
                    top=50, left=20,
                    right=20, bottom=5
                ),
                content=ft.Column(
                    controls=[
                        first_page_content
                    ]
                ),

            )
        ]
    )


    container=ft.Container(
        width=300,
        height=670,
        bgcolor=BG,
        border_radius=25,
        content=ft.Stack(
            controls=[
                page_1,
                page_2,
            ]
        )

        )
    pages={
        '/':ft.View(
            '/', 
            [
                container
            ]
        ),
        "/create_task":ft.View(
            "/create_task",
            [
                create_task_view
            ]
        )
    }
    def route_change(route):
        page.views.clear()
        page.views.append(
        pages[page.route]

        )
    page.add(container)
    page.on_route_change=route_change
    page.go(page.route)

ft.app(target=main)