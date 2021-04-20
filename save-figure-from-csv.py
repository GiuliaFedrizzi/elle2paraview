"""
Import csv file converted from an elle file, apply 'Table To Points', save figure.

This script was mostly generated with the "trace" tool in ParaView (Tools > Start Trace)
Giulia Fedrizzi, March 2021
"""

#### import the simple module from the paraview
from paraview.simple import *
import glob 
import os
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

for file_to_convert in glob.glob("*.csv"):
    converted_file_name=file_to_convert.replace(".csv","") # extract the name without file extension
    # create a new 'CSV Reader'
    convertedcsv = CSVReader(FileName=file_to_convert)
    if os.path.isfile('Fractures-'+converted_file_name+'.png') and os.path.isfile('Pressure-'+converted_file_name+'.png') and  os.path.isfile('Porosity'+converted_file_name+'.png'):
        print "Files already exist."
        continue
    convertedcsv.DetectNumericColumns = 1
    convertedcsv.UseStringDelimiter = 1
    convertedcsv.HaveHeaders = 1
    convertedcsv.FieldDelimiterCharacters = ','
    convertedcsv.MergeConsecutiveDelimiters = 0

    # # Create a new 'SpreadSheet View'
    spreadSheetView1 = CreateView('SpreadSheetView')

    # get layout
    layout1 = GetLayout()
    # find view
    renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')

    # create a new 'Table To Points'
    tableToPoints1 = TableToPoints(Input=convertedcsv)
    tableToPoints1.a2DPoints = 0
    tableToPoints1.KeepAllDataArrays = 0

    # Properties modified on tableToPoints1
    tableToPoints1.XColumn = 'x coord'
    tableToPoints1.YColumn = 'y coord'
    tableToPoints1.ZColumn = 'z coord'

    # show data in view
    tableToPoints1Display = Show(tableToPoints1, spreadSheetView1)
    # trace defaults for the display properties.
    tableToPoints1Display.FieldAssociation = 'Point Data'
    tableToPoints1Display.CompositeDataSetIndex = [0]


    # update the view to ensure updated data information
    spreadSheetView1.Update()

    # destroy spreadSheetView1
    Delete(spreadSheetView1)
    del spreadSheetView1

    # set active view
    SetActiveView(renderView1)

    # set active source
    SetActiveSource(tableToPoints1)

    # show data in view
    tableToPoints1Display = Show(tableToPoints1, renderView1)
    # trace defaults for the display properties.
    tableToPoints1Display.Representation = 'Surface'
    tableToPoints1Display.AmbientColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.ColorArrayName = [None, '']
    tableToPoints1Display.DiffuseColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.LookupTable = None
    tableToPoints1Display.MapScalars = 1
    tableToPoints1Display.InterpolateScalarsBeforeMapping = 1
    tableToPoints1Display.Opacity = 1.0
    tableToPoints1Display.PointSize = 2.0
    tableToPoints1Display.LineWidth = 1.0
    tableToPoints1Display.Interpolation = 'Gouraud'
    tableToPoints1Display.Specular = 0.0
    tableToPoints1Display.SpecularColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.SpecularPower = 100.0
    tableToPoints1Display.Ambient = 0.0
    tableToPoints1Display.Diffuse = 1.0
    tableToPoints1Display.EdgeColor = [0.0, 0.0, 0.5]
    tableToPoints1Display.BackfaceRepresentation = 'Follow Frontface'
    tableToPoints1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.BackfaceOpacity = 1.0
    tableToPoints1Display.Position = [0.0, 0.0, 0.0]
    tableToPoints1Display.Scale = [1.0, 1.0, 1.0]
    tableToPoints1Display.Orientation = [0.0, 0.0, 0.0]
    tableToPoints1Display.Origin = [0.0, 0.0, 0.0]
    tableToPoints1Display.Pickable = 1
    tableToPoints1Display.Texture = None
    tableToPoints1Display.Triangulate = 0
    tableToPoints1Display.NonlinearSubdivisionLevel = 1
    tableToPoints1Display.UseDataPartitions = 0
    tableToPoints1Display.OSPRayUseScaleArray = 0
    tableToPoints1Display.OSPRayScaleArray = 'Fractures'
    tableToPoints1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    tableToPoints1Display.Orient = 0
    tableToPoints1Display.OrientationMode = 'Direction'
    tableToPoints1Display.SelectOrientationVectors = 'Fractures'
    tableToPoints1Display.Scaling = 0
    tableToPoints1Display.ScaleMode = 'No Data Scaling Off'
    tableToPoints1Display.ScaleFactor = 0.1
    tableToPoints1Display.SelectScaleArray = 'Fractures'
    tableToPoints1Display.GlyphType = 'Arrow'
    tableToPoints1Display.UseGlyphTable = 0
    tableToPoints1Display.GlyphTableIndexArray = 'Fractures'
    tableToPoints1Display.UseCompositeGlyphTable = 0
    tableToPoints1Display.DataAxesGrid = 'GridAxesRepresentation'
    tableToPoints1Display.SelectionCellLabelBold = 0
    tableToPoints1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
    tableToPoints1Display.SelectionCellLabelFontFamily = 'Arial'
    tableToPoints1Display.SelectionCellLabelFontSize = 18
    tableToPoints1Display.SelectionCellLabelItalic = 0
    tableToPoints1Display.SelectionCellLabelJustification = 'Left'
    tableToPoints1Display.SelectionCellLabelOpacity = 1.0
    tableToPoints1Display.SelectionCellLabelShadow = 0
    tableToPoints1Display.SelectionPointLabelBold = 0
    tableToPoints1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
    tableToPoints1Display.SelectionPointLabelFontFamily = 'Arial'
    tableToPoints1Display.SelectionPointLabelFontSize = 18
    tableToPoints1Display.SelectionPointLabelItalic = 0
    tableToPoints1Display.SelectionPointLabelJustification = 'Left'
    tableToPoints1Display.SelectionPointLabelOpacity = 1.0
    tableToPoints1Display.SelectionPointLabelShadow = 0
    tableToPoints1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
    tableToPoints1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

    # init the 'Arrow' selected for 'GlyphType'
    tableToPoints1Display.GlyphType.TipResolution = 6
    tableToPoints1Display.GlyphType.TipRadius = 0.1
    tableToPoints1Display.GlyphType.TipLength = 0.35
    tableToPoints1Display.GlyphType.ShaftResolution = 6
    tableToPoints1Display.GlyphType.ShaftRadius = 0.03
    tableToPoints1Display.GlyphType.Invert = 0

    # init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
    tableToPoints1Display.DataAxesGrid.XTitle = 'X Axis'
    tableToPoints1Display.DataAxesGrid.YTitle = 'Y Axis'
    tableToPoints1Display.DataAxesGrid.ZTitle = 'Z Axis'
    tableToPoints1Display.DataAxesGrid.XTitleColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
    tableToPoints1Display.DataAxesGrid.XTitleBold = 0
    tableToPoints1Display.DataAxesGrid.XTitleItalic = 0
    tableToPoints1Display.DataAxesGrid.XTitleFontSize = 12
    tableToPoints1Display.DataAxesGrid.XTitleShadow = 0
    tableToPoints1Display.DataAxesGrid.XTitleOpacity = 1.0
    tableToPoints1Display.DataAxesGrid.YTitleColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
    tableToPoints1Display.DataAxesGrid.YTitleBold = 0
    tableToPoints1Display.DataAxesGrid.YTitleItalic = 0
    tableToPoints1Display.DataAxesGrid.YTitleFontSize = 12
    tableToPoints1Display.DataAxesGrid.YTitleShadow = 0
    tableToPoints1Display.DataAxesGrid.YTitleOpacity = 1.0
    tableToPoints1Display.DataAxesGrid.ZTitleColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
    tableToPoints1Display.DataAxesGrid.ZTitleBold = 0
    tableToPoints1Display.DataAxesGrid.ZTitleItalic = 0
    tableToPoints1Display.DataAxesGrid.ZTitleFontSize = 12
    tableToPoints1Display.DataAxesGrid.ZTitleShadow = 0
    tableToPoints1Display.DataAxesGrid.ZTitleOpacity = 1.0
    tableToPoints1Display.DataAxesGrid.FacesToRender = 63
    tableToPoints1Display.DataAxesGrid.CullBackface = 0
    tableToPoints1Display.DataAxesGrid.CullFrontface = 1
    tableToPoints1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.DataAxesGrid.ShowGrid = 0
    tableToPoints1Display.DataAxesGrid.ShowEdges = 1
    tableToPoints1Display.DataAxesGrid.ShowTicks = 1
    tableToPoints1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
    tableToPoints1Display.DataAxesGrid.AxesToLabel = 63
    tableToPoints1Display.DataAxesGrid.XLabelColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
    tableToPoints1Display.DataAxesGrid.XLabelBold = 0
    tableToPoints1Display.DataAxesGrid.XLabelItalic = 0
    tableToPoints1Display.DataAxesGrid.XLabelFontSize = 12
    tableToPoints1Display.DataAxesGrid.XLabelShadow = 0
    tableToPoints1Display.DataAxesGrid.XLabelOpacity = 1.0
    tableToPoints1Display.DataAxesGrid.YLabelColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
    tableToPoints1Display.DataAxesGrid.YLabelBold = 0
    tableToPoints1Display.DataAxesGrid.YLabelItalic = 0
    tableToPoints1Display.DataAxesGrid.YLabelFontSize = 12
    tableToPoints1Display.DataAxesGrid.YLabelShadow = 0
    tableToPoints1Display.DataAxesGrid.YLabelOpacity = 1.0
    tableToPoints1Display.DataAxesGrid.ZLabelColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
    tableToPoints1Display.DataAxesGrid.ZLabelBold = 0
    tableToPoints1Display.DataAxesGrid.ZLabelItalic = 0
    tableToPoints1Display.DataAxesGrid.ZLabelFontSize = 12
    tableToPoints1Display.DataAxesGrid.ZLabelShadow = 0
    tableToPoints1Display.DataAxesGrid.ZLabelOpacity = 1.0
    tableToPoints1Display.DataAxesGrid.XAxisNotation = 'Mixed'
    tableToPoints1Display.DataAxesGrid.XAxisPrecision = 2
    tableToPoints1Display.DataAxesGrid.XAxisUseCustomLabels = 0
    tableToPoints1Display.DataAxesGrid.XAxisLabels = []
    tableToPoints1Display.DataAxesGrid.YAxisNotation = 'Mixed'
    tableToPoints1Display.DataAxesGrid.YAxisPrecision = 2
    tableToPoints1Display.DataAxesGrid.YAxisUseCustomLabels = 0
    tableToPoints1Display.DataAxesGrid.YAxisLabels = []
    tableToPoints1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
    tableToPoints1Display.DataAxesGrid.ZAxisPrecision = 2
    tableToPoints1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
    tableToPoints1Display.DataAxesGrid.ZAxisLabels = []

    # init the 'PolarAxesRepresentation' selected for 'PolarAxes'
    tableToPoints1Display.PolarAxes.Visibility = 0
    tableToPoints1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
    tableToPoints1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
    tableToPoints1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
    tableToPoints1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
    tableToPoints1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
    tableToPoints1Display.PolarAxes.EnableCustomRange = 0
    tableToPoints1Display.PolarAxes.CustomRange = [0.0, 1.0]
    tableToPoints1Display.PolarAxes.PolarAxisVisibility = 1
    tableToPoints1Display.PolarAxes.RadialAxesVisibility = 1
    tableToPoints1Display.PolarAxes.DrawRadialGridlines = 1
    tableToPoints1Display.PolarAxes.PolarArcsVisibility = 1
    tableToPoints1Display.PolarAxes.DrawPolarArcsGridlines = 1
    tableToPoints1Display.PolarAxes.NumberOfRadialAxes = 0
    tableToPoints1Display.PolarAxes.AutoSubdividePolarAxis = 1
    tableToPoints1Display.PolarAxes.NumberOfPolarAxis = 0
    tableToPoints1Display.PolarAxes.MinimumRadius = 0.0
    tableToPoints1Display.PolarAxes.MinimumAngle = 0.0
    tableToPoints1Display.PolarAxes.MaximumAngle = 90.0
    tableToPoints1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
    tableToPoints1Display.PolarAxes.Ratio = 1.0
    tableToPoints1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.PolarAxes.PolarAxisTitleVisibility = 1
    tableToPoints1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
    tableToPoints1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
    tableToPoints1Display.PolarAxes.PolarLabelVisibility = 1
    tableToPoints1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
    tableToPoints1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
    tableToPoints1Display.PolarAxes.RadialLabelVisibility = 1
    tableToPoints1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
    tableToPoints1Display.PolarAxes.RadialLabelLocation = 'Bottom'
    tableToPoints1Display.PolarAxes.RadialUnitsVisibility = 1
    tableToPoints1Display.PolarAxes.ScreenSize = 10.0
    tableToPoints1Display.PolarAxes.PolarAxisTitleColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
    tableToPoints1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
    tableToPoints1Display.PolarAxes.PolarAxisTitleBold = 0
    tableToPoints1Display.PolarAxes.PolarAxisTitleItalic = 0
    tableToPoints1Display.PolarAxes.PolarAxisTitleShadow = 0
    tableToPoints1Display.PolarAxes.PolarAxisTitleFontSize = 12
    tableToPoints1Display.PolarAxes.PolarAxisLabelColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
    tableToPoints1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
    tableToPoints1Display.PolarAxes.PolarAxisLabelBold = 0
    tableToPoints1Display.PolarAxes.PolarAxisLabelItalic = 0
    tableToPoints1Display.PolarAxes.PolarAxisLabelShadow = 0
    tableToPoints1Display.PolarAxes.PolarAxisLabelFontSize = 12
    tableToPoints1Display.PolarAxes.LastRadialAxisTextColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
    tableToPoints1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
    tableToPoints1Display.PolarAxes.LastRadialAxisTextBold = 0
    tableToPoints1Display.PolarAxes.LastRadialAxisTextItalic = 0
    tableToPoints1Display.PolarAxes.LastRadialAxisTextShadow = 0
    tableToPoints1Display.PolarAxes.LastRadialAxisTextFontSize = 12
    tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextColor = [1.0, 1.0, 1.0]
    tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
    tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
    tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
    tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
    tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
    tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
    tableToPoints1Display.PolarAxes.EnableDistanceLOD = 1
    tableToPoints1Display.PolarAxes.DistanceLODThreshold = 0.7
    tableToPoints1Display.PolarAxes.EnableViewAngleLOD = 1
    tableToPoints1Display.PolarAxes.ViewAngleLODThreshold = 0.7
    tableToPoints1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
    tableToPoints1Display.PolarAxes.PolarTicksVisibility = 1
    tableToPoints1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
    tableToPoints1Display.PolarAxes.TickLocation = 'Both'
    tableToPoints1Display.PolarAxes.AxisTickVisibility = 1
    tableToPoints1Display.PolarAxes.AxisMinorTickVisibility = 0
    tableToPoints1Display.PolarAxes.ArcTickVisibility = 1
    tableToPoints1Display.PolarAxes.ArcMinorTickVisibility = 0
    tableToPoints1Display.PolarAxes.DeltaAngleMajor = 10.0
    tableToPoints1Display.PolarAxes.DeltaAngleMinor = 5.0
    tableToPoints1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
    tableToPoints1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
    tableToPoints1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
    tableToPoints1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
    tableToPoints1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
    tableToPoints1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
    tableToPoints1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
    tableToPoints1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
    tableToPoints1Display.PolarAxes.ArcMajorTickSize = 0.0
    tableToPoints1Display.PolarAxes.ArcTickRatioSize = 0.3
    tableToPoints1Display.PolarAxes.ArcMajorTickThickness = 1.0
    tableToPoints1Display.PolarAxes.ArcTickRatioThickness = 0.5
    tableToPoints1Display.PolarAxes.Use2DMode = 0
    tableToPoints1Display.PolarAxes.UseLogAxis = 0

    # reset view to fit data
    renderView1.ResetCamera()

    # set the view size: (important so that the colorbar has a reasonable size)
    renderView1.ViewSize=[971, 528]

    # set scalar coloring
    ColorBy(tableToPoints1Display, ('POINTS', 'Fractures'))

    # rescale color and/or opacity maps used to include current data range
    tableToPoints1Display.RescaleTransferFunctionToDataRange(True, False)

    # No legend for fractures. Uncomment the following to show legend.
    # # show color bar/color legend
    # tableToPoints1Display.SetScalarBarVisibility(renderView1, True)

    # # get color transfer function/color map for 'Fractures'
    # fracturesLUT = GetColorTransferFunction('Fractures')
    # fracturesLUT.LockDataRange = 0
    # fracturesLUT.InterpretValuesAsCategories = 0
    # fracturesLUT.ShowCategoricalColorsinDataRangeOnly = 0
    # fracturesLUT.RescaleOnVisibilityChange = 0
    # fracturesLUT.EnableOpacityMapping = 0
    # fracturesLUT.RGBPoints = [-1.0, 0.231373, 0.298039, 0.752941, -0.5, 0.865003, 0.865003, 0.865003, 0.0, 0.705882, 0.0156863, 0.14902]
    # fracturesLUT.UseLogScale = 0
    # fracturesLUT.ColorSpace = 'Diverging'
    # fracturesLUT.UseBelowRangeColor = 0
    # fracturesLUT.BelowRangeColor = [0.0, 0.0, 0.0]
    # fracturesLUT.UseAboveRangeColor = 0
    # fracturesLUT.AboveRangeColor = [1.0, 1.0, 1.0]
    # fracturesLUT.NanColor = [1.0, 1.0, 0.0]
    # fracturesLUT.Discretize = 1
    # fracturesLUT.NumberOfTableValues = 256
    # fracturesLUT.ScalarRangeInitialized = 1.0
    # fracturesLUT.HSVWrap = 0
    # fracturesLUT.VectorComponent = 0
    # fracturesLUT.VectorMode = 'Magnitude'
    # fracturesLUT.AllowDuplicateScalars = 1
    # fracturesLUT.Annotations = []
    # fracturesLUT.ActiveAnnotatedValues = []
    # fracturesLUT.IndexedColors = []

    # # Properties modified on renderView1
    renderView1.Background = [1.0, 1.0, 1.0]

    # # get color legend/bar for fracturesLUT in view renderView1
    # fracturesLUTColorBar = GetScalarBar(fracturesLUT, renderView1)
    # fracturesLUTColorBar.AutoOrient = 1
    # fracturesLUTColorBar.Orientation = 'Vertical'
    # fracturesLUTColorBar.WindowLocation = 'LowerRightCorner'
    # fracturesLUTColorBar.Position = [0.89, 0.02]
    # fracturesLUTColorBar.Title = 'Fractures'
    # fracturesLUTColorBar.ComponentTitle = ''
    # fracturesLUTColorBar.TitleJustification = 'Centered'
    # fracturesLUTColorBar.TitleColor = [1.0, 1.0, 1.0]
    # fracturesLUTColorBar.TitleOpacity = 1.0
    # fracturesLUTColorBar.TitleFontFamily = 'Arial'
    # fracturesLUTColorBar.TitleBold = 0
    # fracturesLUTColorBar.TitleItalic = 0
    # fracturesLUTColorBar.TitleShadow = 0
    # fracturesLUTColorBar.TitleFontSize = 16
    # fracturesLUTColorBar.LabelColor = [1.0, 1.0, 1.0]
    # fracturesLUTColorBar.LabelOpacity = 1.0
    # fracturesLUTColorBar.LabelFontFamily = 'Arial'
    # fracturesLUTColorBar.LabelBold = 0
    # fracturesLUTColorBar.LabelItalic = 0
    # fracturesLUTColorBar.LabelShadow = 0
    # fracturesLUTColorBar.LabelFontSize = 16
    # fracturesLUTColorBar.AutomaticLabelFormat = 1
    # fracturesLUTColorBar.LabelFormat = '%-#6.3g'
    # fracturesLUTColorBar.DrawTickMarks = 1
    # fracturesLUTColorBar.DrawTickLabels = 1
    # fracturesLUTColorBar.UseCustomLabels = 0
    # fracturesLUTColorBar.CustomLabels = []
    # fracturesLUTColorBar.AddRangeLabels = 1
    # fracturesLUTColorBar.RangeLabelFormat = '%-#6.1e'
    # fracturesLUTColorBar.DrawAnnotations = 1
    # fracturesLUTColorBar.AddRangeAnnotations = 0
    # fracturesLUTColorBar.AutomaticAnnotations = 0
    # fracturesLUTColorBar.DrawNanAnnotation = 0
    # fracturesLUTColorBar.NanAnnotation = 'NaN'
    # fracturesLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
    # fracturesLUTColorBar.ScalarBarThickness = 16
    # fracturesLUTColorBar.ScalarBarLength = 0.33

    # # Properties modified on fracturesLUTColorBar
    # fracturesLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    # fracturesLUTColorBar.LabelColor = [0.0, 0.0, 0.0]

    # # change scalar bar placement
    # fracturesLUTColorBar.WindowLocation = 'AnyLocation'
    # fracturesLUTColorBar.Position = [0.8032955715756951, 0.3446969696969697]
    # fracturesLUTColorBar.ScalarBarLength = 0.32999999999999974


    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [0.5, 0.4999802879, 2.731996953640956]
    renderView1.CameraFocalPoint = [0.5, 0.4999802879, 0.0]
    renderView1.CameraParallelScale = 0.7070928427643479

    # save screenshot
    SaveScreenshot('Fractures-'+converted_file_name+'.png', renderView1, ImageResolution=[971, 528],
        FontScaling='Scale fonts proportionally',
        OverrideColorPalette='',
        StereoMode='No change',
        TransparentBackground=0,
        ImageQuality=100)

    # hide color bar/color legend
    # tableToPoints1Display.SetScalarBarVisibility(renderView1, False)


    '''
    ========== END OF FRACTURES, START OF PRESSURE ===========
    '''

    #### saving camera placements for all active views

    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [0.5, 0.4999802879, 2.731996953640956]
    renderView1.CameraFocalPoint = [0.5, 0.4999802879, 0.0]
    renderView1.CameraParallelScale = 0.7070928427643479

    # set scalar coloring
    ColorBy(tableToPoints1Display, ('POINTS', 'Pressure'))

    # rescale color and/or opacity maps used to include current data range
    tableToPoints1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    tableToPoints1Display.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for 'Pressure'
    pressureLUT = GetColorTransferFunction('Pressure')
    pressureLUT.RGBPoints = [9800000.0, 0.231373, 0.298039, 0.752941, 36237328.25, 0.865003, 0.865003, 0.865003, 62674656.5, 0.705882, 0.0156863, 0.14902]
    pressureLUT.ScalarRangeInitialized = 1.0
    # get color legend/bar for pressureLUT in view renderView1
    pressureLUTColorBar = GetScalarBar(pressureLUT, renderView1)
    pressureLUTColorBar.WindowLocation = 'AnyLocation'
    pressureLUTColorBar.Position = [0.8403707518022657, 0.10037878787878785]
    pressureLUTColorBar.Title = 'Pressure'
    pressureLUTColorBar.ComponentTitle = ''
    pressureLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    pressureLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    pressureLUTColorBar.ScalarBarLength = 0.3300000000000001

    # change scalar bar placement
    pressureLUTColorBar.Position = [0.761071060762101, 0.3181818181818182]
    pressureLUTColorBar.ScalarBarLength = 0.33000000000000046

    #### saving camera placements for all active views

    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [0.49875, 0.496315801, 10000.0]
    renderView1.CameraFocalPoint = [0.49875, 0.496315801, 0.0]
    renderView1.CameraParallelScale = 0.7020994664762287

    # save screenshot
    SaveScreenshot('Pressure-'+converted_file_name+'.png', renderView1, ImageResolution=[971, 528],
        FontScaling='Scale fonts proportionally',
        OverrideColorPalette='',
        StereoMode='No change',
        TransparentBackground=0,
        ImageQuality=100)    
    '''
    ========== END OF PRESSURE, START OF POROSITY ===========
    '''
    #### saving camera placements for all active views

    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [0.5, 0.4999802879, 2.731996953640956]
    renderView1.CameraFocalPoint = [0.5, 0.4999802879, 0.0]
    renderView1.CameraParallelScale = 0.7070928427643479

    # set scalar coloring
    ColorBy(tableToPoints1Display, ('POINTS', 'Porosity'))


    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(pressureLUT, renderView1)

    # rescale color and/or opacity maps used to include current data range
    tableToPoints1Display.RescaleTransferFunctionToDataRange(True, False)

    # show color bar/color legend
    tableToPoints1Display.SetScalarBarVisibility(renderView1, True)

    # get color transfer function/color map for 'Porosity'
    porosityLUT = GetColorTransferFunction('Porosity')
    porosityLUT.RGBPoints = [0.08999329060000001, 0.231373, 0.298039, 0.752941, 0.23440400979999998, 0.865003, 0.865003, 0.865003, 0.37881472899999996, 0.705882, 0.0156863, 0.14902]
    porosityLUT.ScalarRangeInitialized = 1.0

    # get color legend/bar for porosityLUT in view renderView1
    porosityLUTColorBar = GetScalarBar(porosityLUT, renderView1)
    porosityLUTColorBar.WindowLocation = 'AnyLocation'
    porosityLUTColorBar.Position = [0.8403707518022657, 0.10037878787878785]
    porosityLUTColorBar.Title = 'Porosity'
    porosityLUTColorBar.ComponentTitle = ''
    porosityLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    porosityLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    porosityLUTColorBar.ScalarBarLength = 0.3300000000000001

    # change scalar bar placement
    porosityLUTColorBar.Position = [0.761071060762101, 0.3181818181818182]
    pressureLUTColorBar.ScalarBarLength = 0.33000000000000046

    #### saving camera placements for all active views

    # current camera placement for renderView1
    renderView1.InteractionMode = '2D'
    renderView1.CameraPosition = [0.49875, 0.496315801, 2.712704029172661]
    renderView1.CameraFocalPoint = [0.49875, 0.496315801, 0.0]
    renderView1.CameraParallelScale = 0.7020994664762287

    # save screenshot
    SaveScreenshot('Porosity'+converted_file_name+'.png', renderView1, ImageResolution=[971, 528],
        FontScaling='Scale fonts proportionally',
        OverrideColorPalette='',
        StereoMode='No change',
        TransparentBackground=0,
        ImageQuality=100)
  # hide color bar/color legend
    tableToPoints1Display.SetScalarBarVisibility(renderView1, False)  
    #### uncomment the following to render all views
    # RenderAllViews()
    # alternatively, if you want to write images, you can use SaveScreenshot(...).
