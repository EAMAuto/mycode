import shutil # For moving and renaming files
import os # For directory operations

def main():
    """Main logic"""
    os.chdir("/home/student/mycode/")

    shutil.move("raynor.obj", "battlecruiser/")

    xname = input("What is the new name for kerrigan.obj? ")
    shutil.move("battlecruiser/kerrigan.obj", f"battlecruiser/{xname}")

main()
