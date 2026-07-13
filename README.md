# CROMMS MultiSpectator in Virtual Research Building (VRB) - uses Binder Template

[![Binder](https://binder.intel4coro.de/badge_logo.svg)](https://binder.intel4coro.de/v2/gh/XPhantomad/VRB-CROMMS-Multispectator/main?urlpath=lab/tree/notebooks/instructions.ipynb)


## Quick Start: Start MultiSpectator

- click on the binder icon above and open the environment
- follow the instructions in the notebook

## MultiSpectator Simulation

The Simulation consists of 4 SUTs (Systems Under Test) and 4 Footbots ("fb_0"-"fb_3"). Only the Footbots are controlled by the MultiSpectator via the Dashboard. Initially, SUT3 and SUT1 are marked as interesting targets because they have all its LEDs turned on. For this reason, they will be inspected by the first robot which detects them. For the inspection the Footbots surround the SUTs in a hexagon shape. The other 2 Footbots perform exploration to search for other SUTs in the area. All detected SUTs appear in the "Discovered Robots" list in the Dashboard. Each of them can get a specified number of observers applied via the action column. All existing monitoring teams are displayed in the "Monitoring" table of the dashboard. This table additionally offers the possibility to stop and cancel an ongoing inspection task. The dashboard updates every second, that is why applying an observer count has to be done quickly.
For use case 5 (fixed-position inspection), the dashboard has 3 input fields below, where the user can specify a target position and the number of observers for that task. After pressing "Apply", the automatically assigned robots drive to the target position and inspect it like a SUT. If all robots are busy in monitoring teams, no new task can be applied.
