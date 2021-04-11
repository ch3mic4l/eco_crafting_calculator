# Description
A tool to calculate how many and which materials you need to craft an item in Eco
</br>
</br>This tool will dynamically download the crafting receipes from the Eco website, so if any updates are made to Eco the script will still work.
</br>
</br>Written on Python 3.9.4

# Usage
```
python eco_crafting_calculator.py --list-crafting-material -i "Steam Truck" -q 1

Downloading HTML from https://wiki.play.eco/en/Crafting
Parsing information from Crafting Page

Searching for Steam Truck
Found Steam Truck
Showing materials required to craft 1 Steam Truck with upgrade module 1's
	Crafted at Assembly Line
	Quantity Produced 1
	Crafting Time (Mins): 9.0
	Labor Cost: 1000
	XP Gained
	Required Skill: Mechanics Level 2
	Materials Used:
		10.8 x Iron Plate
			10.8 x Iron Bar
					7.2 x Iron Concentrate
		7.2 x Iron Pipe
			14.4 x Iron Bar
					9.6 x Iron Concentrate
		21.6 x Screws
			5.4 x Iron Bar
					3.6 x Iron Concentrate
		18.0 x Leather Hide
			18.0 x TinyLeatherCarcass Tag
		27.0 x Lumber Tag
		0.9 x Portable Steam Engine
			7.2 x IronPiston
					14.4 x Iron Pipe
							28.8 x Iron Bar
									19.2 x Iron Concentrate
					14.4 x Iron Bar
							9.6 x Iron Concentrate
			16.2 x Screws
					4.05 x Iron Bar
							2.6999999999999997 x Iron Concentrate
			10.8 x Iron Plate
					10.8 x Iron Bar
							7.2 x Iron Concentrate
			2.7 x Boiler
					40.5 x Iron Plate
							40.5 x Iron Bar
									27.0 x Iron Concentrate
					27.0 x Screws
							6.75 x Iron Bar
									4.5 x Iron Concentrate
			10.8 x Iron Gear
					10.8 x Iron Bar
							7.2 x Iron Concentrate
		3.6 x Iron Wheel
			21.6 x Iron Bar
					14.4 x Iron Concentrate
		0.9 x Iron Axle
			1.8 x Iron Bar
					1.2 x Iron Concentrate
```