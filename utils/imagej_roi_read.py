from ij import IJ
from ij.plugin.frame import RoiManager
from java.awt import FileDialog

fd1 = FileDialog(IJ.getInstance(), "Spot2Cell", FileDialog.LOAD)
fd1.show()
file_name = fd1.getDirectory() + fd1.getFile()

fd2 = FileDialog(IJ.getInstance(), "Rois zip", FileDialog.LOAD)
fd2.show()
rois_file = fd2.getDirectory() + fd2.getFile()


RM = RoiManager()
rm = RM.getRoiManager()
imp = IJ.getImage()
ROIs = rm.open(rois_file)
numb_Rois = rm.getCount()
    
with open(file_name, "r") as textfile:
    # Skip the first line
    next(textfile)
    for line in textfile:
        lineText = line.rstrip()
        if not lineText:
            continue
        coor = line.rstrip().split(",")[101:106]
        coor_xy = map(float,coor)
        cellid = line.rstrip().split(",")[0]
        x_centroid = int(coor_xy[0])
        y_centroid = int(coor_xy[1])
        for i in range(numb_Rois):
            roi = rm.getRoi(i)
            if roi.containsPoint(x_centroid,y_centroid):
                rm.select(i)
                rm.rename(i,cellid)
                break
textfile.close()
rm.runCommand("Associate", "true")
rm.runCommand("Show All with labels")

            
