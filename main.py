import flet as ft
import flet_fastapi
from home import home_route
from store import store_route


async def main(page: ft.Page):
    page.route = home_route
    
    async def store(event):
        
        page.route = store_route
        
        if page.route == store_route:
            page.views.clear()
            page.views.append(
            ft.View(
                store_route,
                      [
                        ft.ElevatedButton('go to home', on_click=home)  
                      ])
            )
        
        await page.update_async()
 
    async def home(event):
        
        page.route = home_route
        
        if page.route == home_route:
            page.views.clear()
            page.views.append(
            ft.View(
            home_route,
                      [
                        ft.ElevatedButton('go to store', on_click=store)  
                      ]
            )
            )
        
        await page.update_async()
    
    
    page.views.clear()
    page.views.append(
            ft.View(
            home_route,
                      [
                        ft.ElevatedButton('go to store', on_click=store)  
                      ]
            )
        )

    await page.update_async()

app = flet_fastapi.app(main)