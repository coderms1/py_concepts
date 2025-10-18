# The built-in zip() function pairs elements from both lists,
# truncates to the length of the shorter one, and is useful
# for parallel iteration like this.

doggos = ["Apollo", "Luna", "Moose", "Bentley"]
energy_lvls = [77, 56, 69, 63, 88]

for doggo, energy in zip(doggos, energy_lvls):
  print(f"{doggo}'s energy: {energy}")