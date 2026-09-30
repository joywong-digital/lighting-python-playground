"""
CS50P Week 6 - Lighting Playbook

Inspired by CS50P Lecture 6: File I/O  https://cdn.cs50.net/python/2022/x/lectures/6/src6.pdf

Example: Gif creation with light bulb on/off

"""
from PIL import Image

off = Image.open("bulb_off.png")
on = Image.open("bulb_on.png")

off.save(
    "minecraft_bulb.gif",
    save_all=True,
    append_images=[on],
    duration=500,
    loop=0
)