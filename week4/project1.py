# Goal:
#   Build a text-based adventure game that feels like a real game:
#     - The player explores an island
#     - Choices affect health + score
#     - There is randomness (unpredictable events)
#     - The game uses loops + conditionals + input + int()
#
# You MUST use:
#   - variables
#   - input()
#   - int() type conversion at least once
#   - if / elif / else
#   - comparison operators (==, >, <, <=, >=)
#   - boolean logic (and/or) at least once
#   - a while loop
#   - break
#   - continue (at least once)
#   - random choice (you will import random)
#
# ------------------------------------------------------------
# GAME STORY
# ------------------------------------------------------------
# You are stranded on a mystery island.
# You must survive, explore, and collect points.
# Random events make the island unpredictable.
#
# ------------------------------------------------------------
# SETUP REQUIREMENTS
# ------------------------------------------------------------
#
# 1) Import random
#    - You will use it to pick random events / directions
#
# 2) Ask the player for their name using input()
#
# 3) Create these variables:
#       health = 100
#       score = 0
#       turns = 0
#
# 4) Print a welcome message using the player's name
#
# ------------------------------------------------------------
# MAIN LOOP REQUIREMENTS
# ------------------------------------------------------------
#
# Use:
#   while health > 0:
#
# Inside the loop:
#
#   A) Increase turns by 1 each loop
#
#   B) Print a status line every turn showing:
#        - turns
#        - health
#        - score
#
#   C) Ask the player for an action:
#        "Choose: jungle / beach / camp / quit"
#
#   D) If action is not one of those options:
#        - Print "Invalid choice"
#        - continue  (DO NOT lose health, DO NOT gain score)
#
# ------------------------------------------------------------
# ACTION 1: JUNGLE (DIRECTION + RANDOM EVENT)
# ------------------------------------------------------------
#
# If action == "jungle":
#
#   1) Ask the player to choose a direction:
#        "Pick a direction: north / south / east / west"
#
#   2) If direction is invalid:
#        - Print "Invalid direction"
#        - continue
#
#   3) Generate a random "safe" direction:
#        - Example: safe_dir = random.choice(["north","south","east","west"])
#
#   4) Compare player direction to safe_dir:
#
#      If they match:
#         - Print something like "You found berries and water!"
#         - Increase health (example: +10)
#         - Increase score (example: +15)
#
#      Else:
#         - Print something like "A wild boar chased you!"
#         - Decrease health (example: -15)
#
#   5) Add an extra twist using boolean logic:
#      Example rule:
#        - If (health < 40 and direction != safe_dir) then extra damage
#          (This forces and/or usage)
#
# ------------------------------------------------------------
# ACTION 2: BEACH (TREASURE CHEST WITH CODE LOCK)
# ------------------------------------------------------------
#
# elif action == "beach":
#
#   Beach has a treasure chest with a code lock.
#
#   1) Randomly generate a secret code number between 1 and 5
#      (example: code = random.randint(1, 5))
#
#   2) Tell the player:
#        "A chest appears! Guess the code (1 to 5). You get 2 tries."
#
#   3) Use a small while loop inside this section:
#        tries = 2
#        while tries > 0:
#            - Ask for guess
#            - Convert to int using int()
#            - Validate: if guess < 1 or guess > 5 -> print "Invalid" and continue
#            - Decrease tries ONLY when valid
#            - If guess == code:
#                 - Print "Chest opened!"
#                 - Increase score a lot (example: +25)
#                 - break
#            - Else:
#                 - Print "Wrong code!"
#
#   4) If they fail both tries:
#        - Print "The chest vanishes!"
#        - Decrease health slightly (example: -5)
#
# ------------------------------------------------------------
# ACTION 3: CAMP (REST OR RISK)
# ------------------------------------------------------------
#
# elif action == "camp":
#
#   Camping can restore health, but it might attract danger.
#
#   1) Ask:
#        "Do you want to rest or set traps? (rest/traps)"
#
#   2) If invalid:
#        - Print "Invalid choice"
#        - continue
#
#   3) If rest:
#        - Random chance:
#            - 50% chance you heal (example +20 health)
#            - 50% chance you get robbed by monkeys (example -10 score)
#        - Use random to decide
#
#   4) If traps:
#        - Random chance:
#            - You catch food (score +10, health +5)
#            - OR you hurt yourself (health -10)
#
# ------------------------------------------------------------
# QUIT
# ------------------------------------------------------------
#
# elif action == "quit":
#     - Print goodbye message
#     - break
#
# ------------------------------------------------------------
# LOOP SAFETY / ENDING RULES
# ------------------------------------------------------------
#
# Safety rules:
#   - turns MUST increase each loop
#   - OR health/score MUST change sometimes
#   - Player MUST always have a way to quit
#
# Ending rules:
#
# After the loop ends:
#
#   If health <= 0:
#       Print "Game Over"
#
#   Always print a final summary:
#       - Player name
#       - Turns survived
#       - Final health
#       - Final score
#
# Bonus ending:
#   If score >= 60:
#       Print "You escaped the island as a legend!"
#   elif score >= 30:
#       Print "You survived, barely!"
#   else:
#       Print "You escaped... but with nothing to brag about."
#
# ------------------------------------------------------------
# OPTIONAL CHALLENGES (Pick 1+)
# ------------------------------------------------------------
#
# 1) Add an inventory system:
#      inventory = 0
#      Gain items from events, spend items to heal or boost score
#
# 2) Add a boss event after turns >= 8:
#      Example: force the player into a final jungle direction challenge
#
# 3) Add "difficulty":
#      Ask user for difficulty (1/2/3) using int()
#      Difficulty changes damage and rewards
#
# 4) Add input normalization:
#      Convert inputs to lowercase to handle "Jungle", "JUNGLE", etc.
