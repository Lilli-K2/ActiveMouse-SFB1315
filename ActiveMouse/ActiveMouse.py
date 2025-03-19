import csv
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import time
from dlclive import Processor
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

print("Processor opened")


class MouseLickImageProcessor(Processor):
    def __init__(self, lik_thresh=0.9, lick_image=r"C:\path\to\your\image.png",
                 no_lick_image=r"C:\path\to\your\image.png"):
        super().__init__()

        self.lik_thresh = lik_thresh
        self.lick_image_path = lick_image
        self.no_lick_image_path = no_lick_image
        self.unix_time = []
        self.XValueNose = []
        self.YValueNose = []
        self.AccuracyNose = []
        self.XValueNeck = []
        self.YValueNeck = []
        self.AccuracyNeck = []
        self.XValueButt = []
        self.YValueButt = []
        self.AccuracyButt = []
        self.XValueTail = []
        self.YValueTail = []
        self.AccuracyTail = []

        # Tkinter setup
        self.root = tk.Tk()
        self.root.title("Lick Detection")

        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        self.update_image(initial=True)

    def update_image(self, image_path=None, initial=False):
        """Loads and updates the displayed image"""
        try:
            if initial:
                image_path = self.no_lick_image_path  # Default image

            image = Image.open(image_path)
            image = image.resize((800, 600), Image.Resampling.LANCZOS)
            image = ImageTk.PhotoImage(image)

            self.image_label.config(image=image)
            self.image_label.image = image  # Keep reference
        except Exception as e:
            print(f"Error loading image: {e}")

    def process(self, pose, **kwargs):

        ### bodyparts
        # 0. nose
        # 1. neck
        # 2. butt
        # 3. tail

        if kwargs["record"]:
            self.unix_time.append(kwargs["frame_time"])
            self.XValueNose.append(pose[0, 0])
            self.YValueNose.append(pose[0, 1])
            self.AccuracyNose.append(pose[0, 2])
            self.XValueNeck.append(pose[1, 0])
            self.YValueNeck.append(pose[1, 1])
            self.AccuracyNeck.append(pose[1, 2])
            self.XValueButt.append(pose[2, 0])
            self.YValueButt.append(pose[2, 1])
            self.AccuracyButt.append(pose[2, 2])
            self.XValueTail.append(pose[3, 0])
            self.YValueTail.append(pose[3, 1])
            self.AccuracyTail.append(pose[3, 2])
            if pose[1, 2] > self.lik_thresh:
                self.update_image(self.lick_image_path)
            else:
                self.update_image(self.no_lick_image_path)

            self.root.update_idletasks()
            self.root.update()

        return pose

    def run_gui(self):
        """Starts the Tkinter main loop."""
        self.root.mainloop()

    def save(self, filename):
        
        base_filename = filename
        
        csv_filename = f"{base_filename}.csv"

        unix_time = np.array(self.unix_time)
        XValueNose = np.array(self.XValueNose)
        YValueNose = np.array(self.YValueNose)
        AccuracyNose = np.array(self.AccuracyNose)
        XValueNeck = np.array(self.XValueNeck)
        YValueNeck = np.array(self.YValueNeck)
        AccuracyNeck = np.array(self.AccuracyNeck)
        XValueButt = np.array(self.XValueButt)
        YValueButt = np.array(self.YValueButt)
        AccuracyButt = np.array(self.AccuracyButt)
        XValueTail = np.array(self.XValueTail)
        YValueTail = np.array(self.YValueTail)
        AccuracyTail = np.array(self.AccuracyTail)

        try:
            df = pd.DataFrame({
                "unix_time": unix_time,
                "XValueNose": XValueNose, "YValueNose": YValueNose, "AccuracyNose": AccuracyNose,
                "XValueNeck": XValueNeck, "YValueNeck": YValueNeck, "AccuracyNeck": AccuracyNeck,
                "XValueButt": XValueButt, "YValueButt": YValueButt, "AccuracyButt": AccuracyButt,
                "XValueTail": XValueTail, "YValueTail": YValueTail, "AccuracyTail": AccuracyTail
            })

            df["scorer"] = df.index

            df.to_csv(csv_filename, index=False)

            save_code = True
        except Exception as e:
            print(f"Error saving CSV: {e}")
            save_code = False
        print("df shape:", df.shape)
        df = pd.DataFrame(df, columns=['unix_time',
                                       'XValueNose', 'YValueNose', 'AccuracyNose',
                                       'XValueNeck', 'YValueNeck', 'AccuracyNeck',
                                       'XValueButt', 'YValueButt', 'AccuracyButt',
                                       'XValueTail', 'YValueTail', 'AccuracyTail',
                                       'scorer'])
        df1 = df.iloc[:, 1:]
        print(df1)

        def format_scientific(value):
            try:
                return '{:.10f}'.format(float(value)).rstrip('0').rstrip('.')
            except ValueError:
                return value

        df1['AccuracyNose'] = df1['AccuracyNose'].apply(format_scientific)
        df1['AccuracyNeck'] = df1['AccuracyNeck'].apply(format_scientific)
        df1['AccuracyButt'] = df1['AccuracyButt'].apply(format_scientific)
        df1['AccuracyTail'] = df1['AccuracyTail'].apply(format_scientific)

        dfBadAccuracyNose = df1.query('AccuracyNose <="0.90"')
        dfBadAccuracyNeck = df1.query('AccuracyNeck <="0.90"')
        dfBadAccuracyButt = df1.query('AccuracyButt <="0.90"')
        dfBadAccuracyTail = df1.query('AccuracyTail <="0.90"')

        total_rows = len(df1)
        bad_countNose = len(dfBadAccuracyNose)
        bad_countNeck = len(dfBadAccuracyNeck)
        good_countNeck = total_rows - bad_countNeck
        bad_countButt = len(dfBadAccuracyButt)
        bad_countTail = len(dfBadAccuracyTail)

        TotalBad_count = sum([bad_countNose, bad_countNeck, bad_countButt, bad_countTail])

        plt.figure(2)
        labels = ['Good Accuracy', 'Bad Accuracy']
        sizes = [good_countNeck, bad_countNeck]
        colors = ['#66b3ff', '#ff6666']
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.axis('equal')
        plt.title("Good vs Bad Accuracy Neck")
        plt.savefig(f"{base_filename}_GoodBadAccuracyNeck.png")

        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True

        df1Neck = df1.drop(dfBadAccuracyNeck.index)
        dfBadAccuracyNeck.to_csv(f"{base_filename}_BadAccuracyNeck.csv")
        df1Neck = df1Neck.reset_index()
        df1Neck.to_csv(f"{base_filename}_GoodValuesNeck.csv")
        TotalEntriesNeck = df1Neck[df1Neck.columns[0]].count()
        print("Total entries Neck:", TotalEntriesNeck)
        nb_row = 30

        Neck_df = df1Neck.rolling(nb_row).mean()[nb_row::nb_row]
        Neck_df.shape  # no one knows what it does but nothing works without it
        Neck_df.to_csv(f"{base_filename}_AveragesNeck.csv")
        Neck_df_every30 = df1Neck.iloc[::30].copy()
        Neck_df_every30.to_csv(f"{base_filename}_test30entriesNeck.csv")
        Neck_df["scorer"] = Neck_df_every30["scorer"]
        Neck_df = Neck_df.reset_index()

        print("Neck_df Datatype:", Neck_df.dtypes)

        dfXvalueNeck = Neck_df["XValueNeck"].shift(1)
        dfyvalueNeck = Neck_df["YValueNeck"].shift(1)
        dfXdefaultNeck = Neck_df["XValueNeck"]
        dfydefaultNeck = Neck_df["YValueNeck"]
        distancesNeck = np.sqrt((dfXdefaultNeck - dfXvalueNeck) ** 2 + (dfydefaultNeck - dfyvalueNeck) ** 2)

        ### Conversion factors:
        # distances = (distances/px_per_cm)

        # Pylon/Basler 4096x2160
        distancesNeck = (distancesNeck/42)

        # OBS/MKV 1280x720
        # distancesNeck = (distancesNeck/13.2)

        # OBS/MKV 1920x1080
        # distancesNeck = (distancesNeck/20)

        distancesNeck = distancesNeck.reset_index()
        distancesNeck.columns.values[1] = "distance"
        Neck_df_every30["scorer"] = pd.to_numeric(Neck_df_every30["scorer"], errors="coerce")
        Neck_df_every30["score_difference"] = Neck_df_every30["scorer"].diff()
        Neck_df_every30.to_csv(f"{base_filename}_Difference.csv")

        Neck_df_every30 = Neck_df_every30.drop(index=0).reset_index(drop=True)
        distancesNeck["DistanceFrames"] = Neck_df_every30["score_difference"].values
        print(distancesNeck["DistanceFrames"].dtype)
        distancesNeck["DistanceFrames"] = distancesNeck["DistanceFrames"] / 30
        distancesNeck = distancesNeck.drop(index=0).reset_index(drop=True)

        distancesNeck["distance"] = distancesNeck["distance"] / distancesNeck["DistanceFrames"]
        distancesNeck["DistanceFrames"] = distancesNeck["DistanceFrames"] / distancesNeck["DistanceFrames"]
        distancesNeck.to_csv(f"{base_filename}_DistanceNeckWithScorer.csv")

        dfdistanceValueNeck = distancesNeck
        dfdistanceValueNeck["DistanceNeck"] = distancesNeck.iloc[:, 1]
        Neckmean_df = distancesNeck.iloc[:, 1].mean()
        Neckstd_dev = distancesNeck.iloc[:, 1].std()
        Neckmean_rounded = Neckmean_df.round(3)
        Neckstd_dev_rounded = Neckstd_dev.round(3)
        print("Mean:\n", Neckmean_rounded)
        print("\nStandard Deviation:\n", Neckstd_dev_rounded)

        dfdistanceValueNeck.to_csv(f"{base_filename}_FinalDistanceNeck.csv")
        distancesNeck.to_csv(f"{base_filename}_beforeIloc.csv")
        FullDistanceNeck = sum(distancesNeck.iloc[0:, 1])  # not necessarily necessary
        print("Full walking Distance based on Neck is:", FullDistanceNeck)

        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True

        plt.figure(6)
        x_Neck = list(dfdistanceValueNeck['index'])
        activityindexNeck = list(dfdistanceValueNeck['DistanceNeck'])

        plt.plot(x_Neck, activityindexNeck, linestyle='-', label='Mouse speed [cm/s]')
        ax = plt.gca()
        ymin, ymax = ax.get_ylim()
        extra_space = (ymax - ymin) * 0.1
        ax.set_ylim(ymin, ymax + extra_space)

        bbox_props = dict(facecolor="lightblue", alpha=0.3, edgecolor="black", boxstyle="round,pad=0.5")
        text = (f"Full Distance: {FullDistanceNeck:.2f}cm\n"
                f"Average Distance: {Neckmean_rounded:.2f}cm\n"
                f"Standard deviation: {Neckstd_dev_rounded:.2f}")

        plt.text(0.05, 0.96, text,
                 transform=ax.transAxes,
                 fontsize=10,
                 verticalalignment='top',
                 horizontalalignment='left',
                 bbox=bbox_props)

        plt.legend()
        plt.title('Mouse [Neck]')
        plt.xlabel('time [s]')
        plt.ylabel('Distance [cm]')
        plt.savefig(f"{base_filename}_FinalNeck.png", dpi=500)

        df1Neck["XValueNeck"] = df1Neck["XValueNeck"].astype(float)
        df1Neck["YValueNeck"] = df1Neck["YValueNeck"].astype(float)  # needs to be float

        dfHeatNeck = df1Neck.iloc[:, [4, 5]]  # should be only x and y
        dfHeatNeck.to_csv(f"{base_filename}_newtest.csv")
        dfHeatNeck = pd.DataFrame(dfHeatNeck)

        bin_size = 10
        x_bins = np.arange(dfHeatNeck['XValueNeck'].min(), dfHeatNeck['XValueNeck'].max() + bin_size, bin_size)
        y_bins = np.arange(dfHeatNeck['YValueNeck'].min(), dfHeatNeck['YValueNeck'].max() + bin_size, bin_size)
        heatmap, xedges, yedges = np.histogram2d(dfHeatNeck['XValueNeck'], dfHeatNeck['YValueNeck'],
                                                 bins=[x_bins, y_bins])

        plt.figure((7), figsize=(8, 6))
        sns.heatmap(heatmap.T,
                    cmap='viridis', cbar=False,
                    square=True,
                    )
        plt.title('Heatmap Mouse [Neck]')
        # plt.xlabel('x')
        # plt.ylabel('y')
        plt.axis('off')
        plt.savefig(f"{base_filename}_HeatmapNeck.png", dpi=500)

       plt.show()

        # Flush all arrays dynamically
        for attr in dir(self):  
            if (attr.startswith("unix") or attr.startswith("XValue")
                    or attr.startswith("YValue") or attr.startswith("Accuracy")):

                setattr(self, attr, [])  

        print("All arrays flushed dynamically!")

        return save_code
