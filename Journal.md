---
title: "WayBoard"
author: "mihranrazaa"
description: "A personalised 60% minimal keyboard "
created_at: "2025-06-13"
---

**June13**

- finalized that i will be using RP2040 for this project and decided that i won't add any knob or display, i will use cherry mx brown switches for this keyboard.
- I want to keep it a simple keyboard which does it's job.

---

**June14**

- Created the repository
- I will start by creating the layout of the keyboard on the website.
- Completed the layout :

![Screenshot](Assets/layout.png)

- I rechanged the layout to the default us based qwerty type, because i personally didn.t liked the previous one that much.

![Screenshot](Assets/newla.png)

- I also found the symbols and footprint for my MCU that will RP2040 plus and Cherry MX brown Switches, i started working on the schematics only connected the switches and diodes till now 

![Screenshot](Assets/raw_schematic.png)

- My goal is atleast completing the pcb in this night and start working on the CAD from that point or after a sleep.

At the end: **4-5hrs of total work**

---

**June 15**

- So i wasn't able to complete the PCB in the night and i did it right now, i will add the imges below, my next plan is building the case for it like i did thought of a design because i put the MCU on the side there is a vacant space below it and remove that space from the pcb because i'm thinking that i can make a handle type thing their which will improve it's looks too i also have to focus on proper screw placements i will propabably add only 4 screws to join the main and top body...
- I also added Text in the pcb which i forgot in the first iteration but even this is just all right, imo it looks better without any text, i mean i can add text on the case yeah just remembered i also thinking of adding PCB holders in the case like yeah i'll add image if that works.
Anyways here's the image for this projects final pcb and schematics :

![Screenshot](Assets/pcd.png)
![Screenshot](Assets/pcb3d.png)
![Screenshot](Assets/f_schem.jpg)

- Btw i found a great plugin in Kicad which automatically arranges the Switches according the keyboard layout design just upload the json file to it, but it kinda also wires up them which i had clean because it was really messy and i let's just say it is best for arranging keys...
- ANyways Started working on the 3D case for the keyboard my plan is to keep the keyboard a bit rounded and the plate too ofc, i will also remove the bottom right part just like the pcb i'm thinking of giving it a Handle like look  from which you can grab it...
- here are is a picture of the body which i created:

![Screenshot](Assets/raw_body.png)

- This is the not the perfect body right now i will add fillet to round the edges which will make it look good i also have to add area for connecting usb type c, need some dimensions before i do that, it should fit the pcb properly....  also  I can't see the extruded lines in the assemble page on onshape dunno why.
- My body is now finalized i added fillet almost everywhere (like in edges )which made the top case and the body look shit,  i didn't take any photos of it tho, then i removed it and added fillet on only exterior side of the body, which is now looking good, i still don't know why the i can't see the extruded line in the asseble page it is quite important part of the keyboard as it will hide the pcb from the gap...

![Screenshot](Assets/fbody.png)

- I have started working on the Top panel now this should be easy as we already have the dxf file for my layout, just need proper positioning and have to add screw holes...
- So a very dumb thing happend with me lol, i added the Gap just near the lines of the top panel rectangle(in sketch) i forgot that the dimensions of the top panel are of the outer base rectangle and i started thinking that i have ruined the design but i understood it later and fixed and the dimensions are now correct and fitting properly

![Screenshot](Assets/fk3.png)

- With that my project is almost finished now just need to make firmware which is very easy actually i never knew keyboard firware are coded on python, anyways i wasted way too much time in assembly page trying to join them together and taking photos i'm not the best in the CAD work...

![Screenshot](Assets/fk1.png)

- I will try complete the firmware tonight only i mean in 3 hrs it will be morning it is already 16 but not for me.. I haven't added the repo to the highway submission so i will do that right now and hopefully submit it tomorrow :).

At the end: **8+ hrs**

---

**JUlY 16**

- In night i almost completed the firmware but now in the morning i have created it all of the files are ready now i just have to find the BOM like component prices in my area create a good README and fix journal i think this should do it
- The pull request is still not accepted i think i have to wait till it gets accepted.
- Finally README done added BOM and details on it, still not accepted this is my second project but my first one didn't got approved yet, i hope this one happens a bit quicker because i have added all the things required...
- ALright everything is done ig it is ready for submission ones my pull request gets accepted i will submit it right away or i will ask in the slack for it, anyways let's hope for the best and I hope I go to undercity!!.

- Completed V1

- Ay Pull request got accepted! Time to submit I will do it after I get home... 
- Alright time to submit filling the form and submitting on slack too...
At the end:**3hrs**

- Improved the design of the port:

![Screenshot](Assets/nport.png)

---

**JULY 17**

- submitted the project yesterday, fixed two pcb issues also added a image of pcb with 3d model components i had to add all the 3d components in the footprint quite time consuming but makes the pcb look good, also i didn't find the 3d model for rp2040 plus but added pico there because they both have same pinout...
- Also i can't add a combined images with the 3d component my laptop can't handle that much and is working like a picture animation basically lot of lagging so yeah i just added the pcb image in the readme file, should i add this info in the readme too?
- anyways that's all i did right now took somewhere around 40-50 mins ....

---

**JUNE23**

- so my project got rejected yeah and got a reply the cad is too basic which is the idea of the minimal keyboard i think, well still i did some more touch up, added a wedge structure for more comfortable usage added a big wayboard name to improve asthetics..

![Screenshot](Assets/ncad.png)

![Screenshot](Assets/ncad2.png)

---

**JULY 9-10**

- SO i Improved the CAD, firstly i completely created a new base, added grooved lines in sides and front, i also added the name, grooved lines looks goood ngl, i was thinking of adding the grooved lines in the front side too but i will not look that good so i scrapped that plan, also forgot to mention the base is wedged, for comfortable typing, then i was thinking of again making that hole for handle but it wasn't looking that good with this base so i removed it and added verison and name, so i kept the top almost same but then i thought of adding the logo of open source hardware so i did that, i revamped the usb c port too previously it was just a big gap now i have added a proper design and hole for it, i think it looks good, now it's upto reviewers, tho i will update it whenever i get other idea and time my exams are almost here ahhh, anyways i will be adding it for re-review now... and yeah here are some images :

![Screenshot](Assets/rcad.png)

![Screenshot](Assets/rcad3.png)

![Screenshot](Assets/rcad5.png)

![Screenshot](Assets/rcad2.png)

- BYEEEE :)

----

**JULY 13**

- Added round extrusions because I think there are looking good there 

![Screenshot](Assets/uhole.png)

