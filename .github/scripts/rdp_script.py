import pyautogui
import time
import os

def main():
    # Open the Start menu
    pyautogui.press('win')
    time.sleep(2)

    # Search for Remote Desktop
    pyautogui.write('remote desktop')
    pyautogui.press('enter')
    time.sleep(2)

    # Click on Remote Desktop Connection
    pyautogui.click(50, 190)
    time.sleep(2)

    # Click on Computer field
    pyautogui.click(760, 460)
    time.sleep(2)

    # Type the IP address of the RDP server
    pyautogui.write('YOUR_RDP_SERVER_IP')
    pyautogui.press('enter')
    time.sleep(2)

    # Perform other necessary interactions (username, password, etc.)
    # This part depends on your RDP setup

if __name__ == "__main__":
    main()

