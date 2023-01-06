public ParticleAnalyzer(int options, int measurements, ResultsTable rt, double minSize, double maxSize, double minCirc, double maxCirc) {
    this.options = options;
    this.measurements = measurements;
    this.rt = rt;
    if (this.rt==null)
    	this.rt = new ResultsTable();
    this.minSize = minSize;
    this.maxSize = maxSize;
    this.minCircularity = minCirc;
    this.maxCircularity = maxCirc;
    slice = 1;
    if ((options&SHOW_ROI_MASKS)!=0)
        showChoice = ROI_MASKS;
    if ((options&SHOW_OVERLAY_OUTLINES)!=0)
        showChoice = OVERLAY_OUTLINES;
    if ((options&SHOW_OVERLAY_MASKS)!=0)
        showChoice = OVERLAY_MASKS;
    if ((options&SHOW_OUTLINES)!=0)
        showChoice = OUTLINES;
    if ((options&SHOW_MASKS)!=0)
        showChoice = MASKS;
    if ((options&SHOW_NONE)!=0)
        showChoice = NOTHING;
    if ((options&FOUR_CONNECTED)!=0) {
        wandMode = Wand.FOUR_CONNECTED;
        options |= INCLUDE_HOLES;
    }
    nextFontSize = defaultFontSize;
    nextFontColor = defaultFontColor;
    nextLineWidth = 1;
    calledByPlugin = true;
}
