import csv

data = [
    ["Event", "Variables", "Action", "Image Assets", "Audio Assets", "MP3 Placement", "Plugin Settings", "Banner Ad Placement", "Interstitial Ad Placement", "AdMob ID", "Action Timing"],
    ["At the beginning of the game", "- None", "Initialize game board", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["When player moves a piece", "Current player", "Validate and execute piece movement", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["When player captures a piece", "Current player", "Remove captured piece from the board", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["When a check occurs", "Current player", "Check if the king is in check", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["When a checkmate occurs", "Current player", "Declare the game as checkmate", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["When a stalemate occurs", "-", "Declare the game as stalemate", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["When player requests a draw", "-", "Evaluate the draw request", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["During gameplay", "Current player, game state", "Update game state and player turn", "-", "-", "-", "-", "-", "-", "-", "-"],
    ["When player resigns", "Current player", "Declare the opponent as the winner", "-", "-", "-", "-", "-", "-", "-", "-"],
]

filename = "chess_game_table.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Table successfully generated and saved as {filename}.")

