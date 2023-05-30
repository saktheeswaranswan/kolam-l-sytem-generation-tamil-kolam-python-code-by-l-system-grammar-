import csv

data = [
    ["Event", "Variables", "Action", "Image Assets", "Audio Assets", "MP3 Placement", "Plugin Settings", "Banner Ad Placement", "Interstitial Ad Placement", "AdMob ID", "Action Timing"],
    ["At the beginning of the scene", "- None", "Create player character", "Player sprite", "-", "-", "-", "-", "-", "-", "-"],
    ["When player collides with an obstacle", "Player lives", "Decrease player lives", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["When player collects a power-up", "Player power-up count", "Increase player power-up count", "Power-up sprite", "Power-up sound effect", "-", "-", "-", "-", "-", "-"],
    ["Timer event", "- None", "Spawn new obstacles", "Obstacle sprites", "-", "-", "-", "-", "-", "-", "Set timer interval for obstacle spawn"],
    ["When player completes a level", "Level progress", "Increase level progress", "-", "Level completion sound effect", "-", "-", "-", "-", "-", "-"],
    ["When player reaches a high score", "High score", "Update high score if current score is higher than previous high score", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["When player triggers an in-game event", "- None", "Trigger specific in-game event", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["During gameplay", "Score, time", "Update score and time", "-", "Score counting sound effect", "-", "-", "-", "-", "-", "-"],
    ["When player pauses the game", "- None", "Pause the game", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["When player resumes the game", "- None", "Resume the game", "-", "-", "-", "-", "-", "-", "-", "-"]
]

filename = "game_table.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Table successfully generated and saved as {filename}.")

