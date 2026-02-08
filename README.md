# LEO-satellite-power-optimization

This is a small tool built to figure out how much battery capacity a satellite needs in Low Earth Orbit (LEO). Since satellites spend part of their orbit in the Earth's shadow (eclipse), they need enough storage to keep the payload running until they hit sunlight again.

How I approached the problem
I wanted to see how the altitude (from 400km to 800km) changes the "battery stress."

NASA reports to keep the simulation realistic:
The Cycle Life Problem: I found that in LEO, a satellite cycles about 15 times a day. If I used a standard 80% Depth of Discharge (like in a car), the battery would die way too fast. Based on Cunningham et al. (NASA), I capped the DoD at 30% to make sure the battery lasts for years.

System Efficiency: I factored in a 92% efficiency for the power electronics (PCDU) to account for heat and conversion losses.


Why I used Python/NumPy?

I wanted to be able to calculate this for a whole constellation of satellites at once. Using NumPy lets me calculate 1,000 different orbits in one go without the computer slowing down.

The Modular Setup: I split the code into physics.py and power.py. This makes it much easier to upgrade—for example, if I wanted to add a more complex thermal model later, I only have to change one file without breaking the whole thing.
