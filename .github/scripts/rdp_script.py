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
    time.sleep(10)  # Wait for the RDP connection to establish

    # Perform other necessary interactions (username, password, etc.)
    # This part depends on your RDP setup
    # ...

    # Install RustDesk using PowerShell
    pyautogui.hotkey('win', 'r')
    time.sleep(2)
    pyautogui.write('powershell')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write('iex (iwr https://raw.githubusercontent.com/rustdesk/rustdesk/master/scripts/install.ps1 -UseBasicP  \owerShell)')
    pyautogui.press('enter')
    time.sleep(10)  # Wait for RustDesk installation to complete

if __name__ == "__main__":
    main()
