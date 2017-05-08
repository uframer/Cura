import json

with open("theme.json") as f:
	theme = json.load(f)
for colour_name in theme["colors"]:
	colour = theme["colors"][colour_name]
	for i in range(3):
		colour[i] = 255 - colour[i]
	theme["colors"][colour_name] = colour
with open("theme.json", "w") as f:
	json.dump(theme, f)

