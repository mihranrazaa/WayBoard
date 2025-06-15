---
title: "WayBoard"
author: "mihranrazaa"
description: "A personalised 60% minimal keyboard "
created_at: "2025-06-13"
---

**June13**

- finalized that i will be using RP2040 for this project and decided that i won't add any knob or display, i will use cherry mx brown switches for this keyboard.
- I want to keep it a simple keyboard which does it's job.

**June14**

- Created the repository
- I will start by creating the layout of the keyboard on the website.
- Completed the layout :

![Screenshot](Assets/layout.png)

- I rechanged the layout to the default us based qwerty type, because i personally didn.t liked the previous one that much.

![Screenshot](newla/layout.png)

- I also found the symbols and footprint for my MCU that will RP2040 plus and Cherry MX brown Switches, i started working on the schematics only connected the switches and diodes till now 

![Screenshot](Assets/raw_schematic.png)

- My goal is atleast completing the pcb in this night and start working on the CAD from that point or after a sleep.

**June 15**
- So i wasn't able to complete the PCB in the night and i did it right now, i will add the imges below, my next plan is building the case for it like i did thought of a design because i put the MCU on the side there is a vacant space below it and remove that space from the pcb because i'm thinking that i can make a handle type thing their which will improve it's looks too i also have to focus on proper screw placements i will propabably add only 4 screws to join the main and top body...
- I also added Text in the pcb which i forgot in the first iteration but even this is just all right, imo it looks better without any text, i mean i can add text on the case yeah just remembered i also thinking of adding PCB holders in the case like yeah i'll add image if that works.
Anyways here's the image for this projects final pcb and schematics :

![Screenshot](Assets/pcd.png)
![Screenshot](Assets/pcb3d.png)
![Screenshot](Assets/f_schem.jpg)

- Btw i found a great plugin in Kicad which automatically arranges the Switches according the keyboard layout design just upload the json file to it, but it kinda also wires up them which i had clean because it was really messy and i let's just say it is best for arranging keys...

