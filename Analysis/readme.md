This [code](https://github.com/Lilli-K2/ActiveMouse/blob/main/Analysis/Analysis.py) can be used to analyse all of the tracked points just based on the original .csv file that is saved after the recording is stopped. In addition to the three figures already generated within using the dlc-live gui figures for all of the tracking points are made.

As of now these figures include:
- accuracy pie charts for all tracked points plus total Accuracy of tracking ability.
- line graphs of speed for all four points
- heatmaps for all four points plus heatsmaps with transparent backgrounds

To use this analysis read the correct .csv file into the <strong>df</strong>. Don't forget to change the <strong>base</strong> to your desired saving filename.

<strong>Please note</strong> that tail-tracking is usually sub-par and negatively affects the total Accuracy. As neck-tracking is usually the best it's what the ActiveMouse code is based on. Nose tracking is also usually satisfactory and butt tracking varies a bit more. It can still be useful to have these figures for all of your tracking points.
