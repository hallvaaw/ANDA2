""" Jython script to perform cell metric quantification in Fiji """

from ij import IJ, ImagePlus
from ij.plugin import ImageCalculator

# Open file with parameters for image analysis
with open("anda_parameters.txt", 'r') as anda_parameters:
    analysis_read = anda_parameters.readlines()

CELL_TYPE = str(anda_parameters[1])
INPUT_ANALYSIS = str(anda_parameters[0]) # List
IMAGE_DIR = str(anda_parameters[1])
OUTLINES = str(anda_parameters[2])


# Open file with image file names
with open("file_names.txt", 'r') as file_names:
    input_files = file_names.read().splitlines()

# Open file with parameters for analyzing cell type
with open("{}_parameters.txt".format(CELL_TYPE), 'r') as cell_type:
    cell_read = cell_type.readlines()

cell_line_parameters = [str(i.rstrip()) for i in cell_read] # Cell parameters list
PATH = str(cell_line_parameters[0])

##### Cell metric parameters
min_cell_size = int(cell_line_parameters[1])
max_cell_size = int(cell_line_parameters[2])
min_cell_circularity = float(cell_line_parameters[3])
max_cell_circularity = float(cell_line_parameters[4])
min_neurite_size = int(cell_line_parameters[5])
max_neurite_size = int(cell_line_parameters[6])
min_neurite_circularity = float(cell_line_parameters[7])
max_neurite_circularity = float(cell_line_parameters[8])
CELL_THRESHOLD = str(cell_line_parameters[9])
NEURITE_THRESHOLD = str(cell_line_parameters[10])
WATERSHED_CHOICE = str(cell_line_parameters[11])


if CELL_THRESHOLD == "NO THRESHOLD":
    CELL_THRESHOLD = "Default" # Default thresholding method in ImageJ
if NEURITE_THRESHOLD == "NO THRESHOLD":
    NEURITE_THRESHOLD = "Default" # Default thresholding method in ImageJ

IJ.run("Set Measurements...", "area fit shape display add redirect=None decimal=3")
image_calc = ImageCalculator() # ImageJ plugin

def particle_analysis(analysis, file_):
    """Quantify cell body count, neurite lengths and neurite attachment points"""

    if analysis == "cells": # Run cell body count analysis
        IJ.open(file_)
        imp = IJ.getImage()
        IJ.run("8-bit")
        IJ.run("Auto Threshold", "method={}".format(CELL_THRESHOLD))
        if WATERSHED_CHOICE == "apply_watershed":
            IJ.run("Watershed")
            IJ.run("Analyze Particles...", "size={}-{} pixel circularity={}-{} show=Nothing display summarize".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
        else:
            IJ.run("Analyze Particles...", "size={}-{} pixel circularity={}-{} show=Nothing display summarize".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
        IJ.saveAs("Results", "{}".format(str(outputfiles)))
        # IJ.run("Clear Results")
        if OUTLINES == "show_OUTLINES":
            IJ.run("Analyze Particles...", "size={}-{} pixel circularity={}-{} show=Nothing display summarize".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
            overlay_ = ImagePlus.getOverlay(imp)
            image_width = imp.getWidth()
            image_height = imp.getHeight()
            IJ.newImage("blank_c", "RGB white", image_width, image_height, 1)
            imp2 = IJ.getImage().setOverlay(overlay_)
            imp2 = IJ.getImage()
            imp3 = imp2.flatten()
            IJ.run(imp3, "8-bit", "")
            IJ.saveAs(imp3, "Tiff", "{}".format(str(outlinefiles)))

    elif analysis == "neurites": # Run neurite length analysis
        IJ.open(file_)
        imp = IJ.getImage()
        IJ.run("8-bit")
        IJ.run("Auto Threshold", "method={}".format(NEURITE_THRESHOLD))
        if WATERSHED_CHOICE == "apply_watershed":
            IJ.run("Watershed")
            IJ.run("Analyze Particles...", "size={}-{} pixel circularity={}-{} show=Nothing display summarize".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
        else:
            IJ.run("Analyze Particles...", "size={}-{} pixel circularity={}-{} show=Nothing display summarize".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
        IJ.run("Analyze Particles...", "size={}-{} pixel circularity={}-{} show=Nothing display summarize".format(min_neurite_size, max_neurite_size, min_neurite_circularity, max_neurite_circularity))
        IJ.saveAs("Results", "{}".format(str(outputfiles)))
        # IJ.run("Clear Results")
        if OUTLINES == "show_OUTLINES":
            IJ.run("Analyze Particles...", "size={}-{} pixel circularity={}-{} show=Nothing display summarize".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
            overlay_ = ImagePlus.getOverlay(imp)
            image_width = imp.getWidth()
            image_height = imp.getHeight()
            IJ.newImage("blank_n", "RGB white", image_width, image_height, 1)
            imp2 = IJ.getImage().setOverlay(overlay_)
            imp2 = IJ.getImage()
            imp3 = imp2.flatten()
            IJ.run(imp3, "8-bit", "")
            IJ.saveAs(imp3, "Tiff", "{}".format(str(outlinefiles)))


    elif analysis == "attachment": # Run neurite attachment point analysis
        IJ.open(file_)
        imp_c = IJ.getImage() # Cell bodies
        imp_n = IJ.getImage() # Neurites
        IJ.run(imp_c, "8-bit", "")
        IJ.run(imp_n, "8-bit", "")

        # Threshold highlighting neurites
        IJ.run(imp_c, "Auto Threshold", "method={}".format(NEURITE_THRESHOLD))
        IJ.run(imp_n, "Auto Threshold", "method={}".format(NEURITE_THRESHOLD))
        if WATERSHED_CHOICE == "apply_watershed":
            IJ.run(imp_c, "Watershed", "") # Watershed segmentation
            IJ.run(imp_c, "Analyze Particles...", "size={}-{} pixel circularity={}-{} show=Overlay".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity)) # Use cell body parameters to extract overlay
            overlay_c = ImagePlus.getOverlay(imp_c) # Get cell body overlay

            IJ.run(imp_n, "Watershed", "") # Watershed segmentation
            IJ.run(imp_n, "Analyze Particles...", "size={}-{} pixel circularity={}-{} show=Overlay".format(min_neurite_size, max_neurite_size, min_neurite_circularity, max_neurite_circularity)) # Use neurite parameters to extract overlay
            overlay_n = ImagePlus.getOverlay(imp_n) # Get neurite overlay
        else:
            IJ.run(imp_c, "Analyze Particles...", "size={}-{} pixel circularity={}-{} show=Overlay".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity)) # Use cell body parameters to extract overlay
            overlay_c = ImagePlus.getOverlay(imp_c) # Get cell body overlay

            IJ.run(imp_n, "Analyze Particles...", "size={}-{} pixel circularity={}-{} show=Overlay".format(min_neurite_size, max_neurite_size, min_neurite_circularity, max_neurite_circularity)) # Use neurite parameters to extract overlay
            overlay_n = ImagePlus.getOverlay(imp_n) # Get neurite overlay

        # Blank image for pasting the overlay onto
        image_width = imp.getWidth()
        image_height = imp.getHeight()
        IJ.newImage("{}_blank_c".format(file_), "RGB white", image_width, image_height, 1)
        imp_c2 = IJ.getImage().setOverlay(overlay_c)
        imp_c2 = IJ.getImage()
        imp_c3 = imp_c2.flatten()
        IJ.run(imp_c3, "8-bit", "")
        IJ.run(imp_c3, "Make Binary", "")
        IJ.saveAs(imp_c3, "Tiff", "{}/imp_c3.tif".format(PATH))

        # Blank image for pasting the overlay onto
        image_width = imp.getWidth()
        image_height = imp.getHeight()
        IJ.newImage("{}_blank_n".format(file_), "RGB white", image_width, image_height, 1)
        imp_n2 = IJ.getImage().setOverlay(overlay_n)
        imp_n2 = IJ.getImage()
        imp_n3 = imp_n2.flatten()
        IJ.run(imp_n3, "8-bit", "")
        IJ.run(imp_n3, "Make Binary", "")
        IJ.saveAs(imp_n3, "Tiff", "{}/imp_n3.tif".format(PATH))
        IJ.run(imp_n3, "Find Edges", "") # Sobel edge detector

        # Get the overlap between cell bodies and neurites - the attachment points
        imp_res = image_calculator.run("Multiply create", imp_n3, imp_c3)
        IJ.saveAs(imp_res, "Tiff", "{}/{}_imp_res.tif".format(PATH, file_))
        IJ.run(imp_res, "Analyze Particles...", "size=0-100 pixel circularity=0.00-1.00 show=Nothing display summarize")
        IJ.saveAs("Results", "{}".format(str(outputfiles)))
        IJ.run("Clear Results")
        if OUTLINES == "show_OUTLINES":
            IJ.run("Analyze Particles...", "size={}-{} pixel circularity={}-{} show=Nothing display summarize".format(min_cell_size, max_cell_size, min_cell_circularity, max_cell_circularity))
            overlay_ = ImagePlus.getOverlay(imp_res)
            image_width = imp.getWidth()
            image_height = imp.getHeight()
            IJ.newImage("blank_b", "RGB white", image_width, image_height, 1)
            imp2 = IJ.getImage().setOverlay(overlay_)
            imp2 = IJ.getImage()
            imp3 = imp2.flatten()
            IJ.run(imp3, "8-bit", "")
            IJ.saveAs(imp3, "Tiff", "{}".format(str(outlinefiles)))

for file_name in input_files:
    particle_analysis(INPUT_ANALYSIS, file_name)

def file_read():
    """If ouputfile is not written, write an empty outputfile"""
    try:
        output = open(outputfiles, "r")
    except IOError:
        with open(outputfiles, "w") as output:
            output.write("NO IDENTIFIED MOTIFS")

file_read()
