# Macro-Bot
A python Macro Bot

This script reads commands from a text file and performs corresponding mouse movements
and keyboard actions.

Commands Format:
- For mouse movements: MOUSE.UP(n), MOUSE.DOWN(n), MOUSE.LEFT(n), MOUSE.RIGHT(n)
  (n is optional, defaults to 1 if not provided)
- For keyboard actions: KEYBOARD(letter)

Example Usage in commands.txt:
MOUSE.UP(50)
KEYBOARD(A)
MOUSE.RIGHT(30)

Author: CURSEDVR
