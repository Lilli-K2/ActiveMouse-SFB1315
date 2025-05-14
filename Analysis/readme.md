This [code](https://github.com/Lilli-K2/ActiveMouse/blob/main/Analysis/Analysis.py) can be used to analyse all of the tracked points just based on the original .csv file that is saved after the recording is stopped. In addition to the three figures already generated within using the dlc-live gui, figures for all of the tracking points are made.

As of now these figures include:
- <strong>accuracy pie charts</strong> for all tracked points plus total accuracy of tracking ability
- <strong>line graphs</strong> of speed for all four points
- <strong>heatmaps</strong> for all four points plus heatsmaps with transparent backgrounds

To use this analysis read the correct .csv file into the <strong>df</strong>. Don't forget to change the <strong>base</strong> to your desired saving filename.

<strong>Please note</strong> that tail-tracking is usually sub-par and negatively affects the total accuracy. As neck-tracking is usually the best it's what the ActiveMouse code is based on. Butt tracking is also usually satisfactory and nose tracking varies a bit more. It can still be useful to have these figures for all of your tracking points.
