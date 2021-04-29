# trace generated using paraview version 5.9.0

#### import the simple module from the paraview
from paraview.simple import *
import glob
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'CSV Reader'
#my_experiment02 = CSVReader(registrationName='my_experiment*',
 #FileName=['/home/ubuntu/elle-daniel/myExperiments/testDir/my_experiment034.csv', 
 #'/home/ubuntu/elle-daniel/myExperiments/testDir/my_experiment035.csv', 
 #'/home/ubuntu/elle-daniel/myExperiments/testDir/my_experiment036.csv'])
FileName=sorted(glob.glob("*.csv"))
my_experiment02 = CSVReader(registrationName='*', FileName=FileName)
my_experiment02.DetectNumericColumns = 1
my_experiment02.UseStringDelimiter = 1
my_experiment02.HaveHeaders = 1
my_experiment02.FieldDelimiterCharacters = ','
my_experiment02.AddTabFieldDelimiter = 0
my_experiment02.MergeConsecutiveDelimiters = 0

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.UseCache = 0
spreadSheetView1.ViewSize = [400, 400]
spreadSheetView1.CellFontSize = 9
spreadSheetView1.HeaderFontSize = 9
spreadSheetView1.SelectionOnly = 0
spreadSheetView1.GenerateCellConnectivity = 0
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.InvertOrder = 0
spreadSheetView1.BlockSize = 1024
spreadSheetView1.HiddenColumnLabels = ['Block Number']
spreadSheetView1.FieldAssociation = 'Point Data'

# show data in view
my_experiment02Display = Show(my_experiment02, spreadSheetView1, 'SpreadSheetRepresentation')

# trace defaults for the display properties.
my_experiment02Display.CompositeDataSetIndex = [0]

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=spreadSheetView1, layout=layout1, hint=0)

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')

# update the view to ensure updated data information
renderView1.Update()

# destroy spreadSheetView1
Delete(spreadSheetView1)
del spreadSheetView1

# close an empty frame
#layout1.Collapse(2)

# set active view
SetActiveView(renderView1)

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(registrationName='TableToPoints1', Input=my_experiment02)
tableToPoints1.XColumn = 'Fractures'
tableToPoints1.YColumn = 'Fractures'
tableToPoints1.ZColumn = 'Fractures'
tableToPoints1.a2DPoints = 0
tableToPoints1.KeepAllDataArrays = 0

# Properties modified on tableToPoints1
tableToPoints1.XColumn = 'x coord'
tableToPoints1.YColumn = 'y coord'
tableToPoints1.ZColumn = 'z coord'

# set the background to white
LoadPalette(paletteName='WhiteBackground')

# show data in view
tableToPoints1Display = Show(tableToPoints1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tableToPoints1Display.Selection = None
tableToPoints1Display.Representation = 'Surface'
tableToPoints1Display.ColorArrayName = [None, '']
tableToPoints1Display.LookupTable = None
tableToPoints1Display.MapScalars = 1
tableToPoints1Display.MultiComponentsMapping = 0
tableToPoints1Display.InterpolateScalarsBeforeMapping = 1
tableToPoints1Display.Opacity = 1.0
tableToPoints1Display.PointSize = 2.0
tableToPoints1Display.LineWidth = 1.0
tableToPoints1Display.RenderLinesAsTubes = 0
tableToPoints1Display.RenderPointsAsSpheres = 0
tableToPoints1Display.Interpolation = 'Gouraud'
tableToPoints1Display.Specular = 0.0
tableToPoints1Display.SpecularColor = [1.0, 1.0, 1.0]
tableToPoints1Display.SpecularPower = 100.0
tableToPoints1Display.Luminosity = 0.0
tableToPoints1Display.Ambient = 0.0
tableToPoints1Display.Diffuse = 1.0
tableToPoints1Display.Roughness = 0.3
tableToPoints1Display.Metallic = 0.0
tableToPoints1Display.EdgeTint = [1.0, 1.0, 1.0]
tableToPoints1Display.SelectTCoordArray = 'None'
tableToPoints1Display.SelectNormalArray = 'None'
tableToPoints1Display.SelectTangentArray = 'None'
tableToPoints1Display.Texture = None
tableToPoints1Display.RepeatTextures = 1
tableToPoints1Display.InterpolateTextures = 0
tableToPoints1Display.SeamlessU = 0
tableToPoints1Display.SeamlessV = 0
tableToPoints1Display.UseMipmapTextures = 0
tableToPoints1Display.BaseColorTexture = None
tableToPoints1Display.NormalTexture = None
tableToPoints1Display.NormalScale = 1.0
tableToPoints1Display.MaterialTexture = None
tableToPoints1Display.OcclusionStrength = 1.0
tableToPoints1Display.EmissiveTexture = None
tableToPoints1Display.EmissiveFactor = [1.0, 1.0, 1.0]
tableToPoints1Display.FlipTextures = 0
tableToPoints1Display.BackfaceRepresentation = 'Follow Frontface'
tableToPoints1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
tableToPoints1Display.BackfaceOpacity = 1.0
tableToPoints1Display.Position = [0.0, 0.0, 0.0]
tableToPoints1Display.Scale = [1.0, 1.0, 1.0]
tableToPoints1Display.Orientation = [0.0, 0.0, 0.0]
tableToPoints1Display.Origin = [0.0, 0.0, 0.0]
tableToPoints1Display.CoordinateShiftScaleMethod = 'Always Auto Shift Scale'
tableToPoints1Display.Pickable = 1
tableToPoints1Display.Triangulate = 0
tableToPoints1Display.UseShaderReplacements = 0
tableToPoints1Display.ShaderReplacements = ''
tableToPoints1Display.NonlinearSubdivisionLevel = 1
tableToPoints1Display.UseDataPartitions = 0

tableToPoints1Display.OSPRayUseScaleArray = 'All Approximate'

tableToPoints1Display.OSPRayScaleArray = 'Fractures'

tableToPoints1Display.OSPRayScaleFunction = 'PiecewiseFunction'

tableToPoints1Display.OSPRayMaterial = 'None'

tableToPoints1Display.Orient = 0

tableToPoints1Display.OrientationMode = 'Direction'

tableToPoints1Display.SelectOrientationVectors = 'None'

tableToPoints1Display.Scaling = 0

tableToPoints1Display.ScaleMode = 'No Data Scaling Off'

tableToPoints1Display.ScaleFactor = 0.09975

tableToPoints1Display.SelectScaleArray = 'Fractures'

tableToPoints1Display.GlyphType = 'Arrow'

tableToPoints1Display.UseGlyphTable = 0

tableToPoints1Display.GlyphTableIndexArray = 'Fractures'

tableToPoints1Display.UseCompositeGlyphTable = 0

tableToPoints1Display.UseGlyphCullingAndLOD = 0

tableToPoints1Display.LODValues = []

tableToPoints1Display.ColorByLODIndex = 0

tableToPoints1Display.GaussianRadius = 0.004987500000000001

tableToPoints1Display.ShaderPreset = 'Sphere'

tableToPoints1Display.CustomTriangleScale = 3

tableToPoints1Display.CustomShader = """ // This custom shader code define a gaussian blur

// Please take a look into vtkSMPointGaussianRepresentation.cxx

// for other custom shader examples

//VTK::Color::Impl

float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);

float gaussian = exp(-0.5*dist2);

opacity = opacity*gaussian;

"""

tableToPoints1Display.Emissive = 0

tableToPoints1Display.ScaleByArray = 0

tableToPoints1Display.SetScaleArray = ['POINTS', 'Fractures']

tableToPoints1Display.ScaleArrayComponent = ''

tableToPoints1Display.UseScaleFunction = 1

tableToPoints1Display.ScaleTransferFunction = 'PiecewiseFunction'

tableToPoints1Display.OpacityByArray = 0

tableToPoints1Display.OpacityArray = ['POINTS', 'Fractures']

tableToPoints1Display.OpacityArrayComponent = ''

tableToPoints1Display.OpacityTransferFunction = 'PiecewiseFunction'

tableToPoints1Display.DataAxesGrid = 'GridAxesRepresentation'

tableToPoints1Display.SelectionCellLabelBold = 0

tableToPoints1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]

tableToPoints1Display.SelectionCellLabelFontFamily = 'Arial'

tableToPoints1Display.SelectionCellLabelFontFile = ''

tableToPoints1Display.SelectionCellLabelFontSize = 18

tableToPoints1Display.SelectionCellLabelItalic = 0

tableToPoints1Display.SelectionCellLabelJustification = 'Left'

tableToPoints1Display.SelectionCellLabelOpacity = 1.0

tableToPoints1Display.SelectionCellLabelShadow = 0

tableToPoints1Display.SelectionPointLabelBold = 0

tableToPoints1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]

tableToPoints1Display.SelectionPointLabelFontFamily = 'Arial'

tableToPoints1Display.SelectionPointLabelFontFile = ''

tableToPoints1Display.SelectionPointLabelFontSize = 18

tableToPoints1Display.SelectionPointLabelItalic = 0

tableToPoints1Display.SelectionPointLabelJustification = 'Left'

tableToPoints1Display.SelectionPointLabelOpacity = 1.0

tableToPoints1Display.SelectionPointLabelShadow = 0

tableToPoints1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'

tableToPoints1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

tableToPoints1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'

tableToPoints1Display.GlyphType.TipResolution = 6

tableToPoints1Display.GlyphType.TipRadius = 0.1

tableToPoints1Display.GlyphType.TipLength = 0.35

tableToPoints1Display.GlyphType.ShaftResolution = 6

tableToPoints1Display.GlyphType.ShaftRadius = 0.03

tableToPoints1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'

tableToPoints1Display.ScaleTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

tableToPoints1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'

tableToPoints1Display.OpacityTransferFunction.Points = [-1.0, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]

tableToPoints1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
tableToPoints1Display.DataAxesGrid.XTitle = 'X Axis'
tableToPoints1Display.DataAxesGrid.YTitle = 'Y Axis'
tableToPoints1Display.DataAxesGrid.ZTitle = 'Z Axis'
tableToPoints1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
tableToPoints1Display.DataAxesGrid.XTitleFontFile = ''
tableToPoints1Display.DataAxesGrid.XTitleBold = 0
tableToPoints1Display.DataAxesGrid.XTitleItalic = 0
tableToPoints1Display.DataAxesGrid.XTitleFontSize = 12
tableToPoints1Display.DataAxesGrid.XTitleShadow = 0
tableToPoints1Display.DataAxesGrid.XTitleOpacity = 1.0
tableToPoints1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
tableToPoints1Display.DataAxesGrid.YTitleFontFile = ''
tableToPoints1Display.DataAxesGrid.YTitleBold = 0
tableToPoints1Display.DataAxesGrid.YTitleItalic = 0
tableToPoints1Display.DataAxesGrid.YTitleFontSize = 12
tableToPoints1Display.DataAxesGrid.YTitleShadow = 0
tableToPoints1Display.DataAxesGrid.YTitleOpacity = 1.0
tableToPoints1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
tableToPoints1Display.DataAxesGrid.ZTitleFontFile = ''
tableToPoints1Display.DataAxesGrid.ZTitleBold = 0
tableToPoints1Display.DataAxesGrid.ZTitleItalic = 0
tableToPoints1Display.DataAxesGrid.ZTitleFontSize = 12
tableToPoints1Display.DataAxesGrid.ZTitleShadow = 0
tableToPoints1Display.DataAxesGrid.ZTitleOpacity = 1.0
tableToPoints1Display.DataAxesGrid.FacesToRender = 63
tableToPoints1Display.DataAxesGrid.CullBackface = 0
tableToPoints1Display.DataAxesGrid.CullFrontface = 1
tableToPoints1Display.DataAxesGrid.ShowGrid = 0
tableToPoints1Display.DataAxesGrid.ShowEdges = 1
tableToPoints1Display.DataAxesGrid.ShowTicks = 1
tableToPoints1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
tableToPoints1Display.DataAxesGrid.AxesToLabel = 63
tableToPoints1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
tableToPoints1Display.DataAxesGrid.XLabelFontFile = ''
tableToPoints1Display.DataAxesGrid.XLabelBold = 0
tableToPoints1Display.DataAxesGrid.XLabelItalic = 0
tableToPoints1Display.DataAxesGrid.XLabelFontSize = 12
tableToPoints1Display.DataAxesGrid.XLabelShadow = 0
tableToPoints1Display.DataAxesGrid.XLabelOpacity = 1.0
tableToPoints1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
tableToPoints1Display.DataAxesGrid.YLabelFontFile = ''
tableToPoints1Display.DataAxesGrid.YLabelBold = 0
tableToPoints1Display.DataAxesGrid.YLabelItalic = 0
tableToPoints1Display.DataAxesGrid.YLabelFontSize = 12
tableToPoints1Display.DataAxesGrid.YLabelShadow = 0
tableToPoints1Display.DataAxesGrid.YLabelOpacity = 1.0
tableToPoints1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
tableToPoints1Display.DataAxesGrid.ZLabelFontFile = ''
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
tableToPoints1Display.DataAxesGrid.UseCustomBounds = 0
tableToPoints1Display.DataAxesGrid.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]

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
tableToPoints1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
tableToPoints1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
tableToPoints1Display.PolarAxes.PolarAxisTitleFontFile = ''
tableToPoints1Display.PolarAxes.PolarAxisTitleBold = 0
tableToPoints1Display.PolarAxes.PolarAxisTitleItalic = 0
tableToPoints1Display.PolarAxes.PolarAxisTitleShadow = 0
tableToPoints1Display.PolarAxes.PolarAxisTitleFontSize = 12
tableToPoints1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
tableToPoints1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
tableToPoints1Display.PolarAxes.PolarAxisLabelFontFile = ''
tableToPoints1Display.PolarAxes.PolarAxisLabelBold = 0
tableToPoints1Display.PolarAxes.PolarAxisLabelItalic = 0
tableToPoints1Display.PolarAxes.PolarAxisLabelShadow = 0
tableToPoints1Display.PolarAxes.PolarAxisLabelFontSize = 12
tableToPoints1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
tableToPoints1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
tableToPoints1Display.PolarAxes.LastRadialAxisTextFontFile = ''
tableToPoints1Display.PolarAxes.LastRadialAxisTextBold = 0
tableToPoints1Display.PolarAxes.LastRadialAxisTextItalic = 0
tableToPoints1Display.PolarAxes.LastRadialAxisTextShadow = 0
tableToPoints1Display.PolarAxes.LastRadialAxisTextFontSize = 12
tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
tableToPoints1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
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
# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(tableToPoints1Display, ('POINTS', 'Fractures'))

# rescale color and/or opacity maps used to include current data range
tableToPoints1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tableToPoints1Display.SetScalarBarVisibility(renderView1, False)


# get color transfer function/color map for 'Fractures'
fracturesLUT = GetColorTransferFunction('Fractures')
fracturesLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
fracturesLUT.InterpretValuesAsCategories = 0
fracturesLUT.AnnotationsInitialized = 0
fracturesLUT.ShowCategoricalColorsinDataRangeOnly = 0
fracturesLUT.RescaleOnVisibilityChange = 0
fracturesLUT.EnableOpacityMapping = 0
fracturesLUT.RGBPoints = [-1.0, 0.231373, 0.298039, 0.752941, -0.5, 0.865003, 0.865003, 0.865003, 0.0, 0.705882, 0.0156863, 0.14902]
fracturesLUT.UseLogScale = 0
fracturesLUT.UseOpacityControlPointsFreehandDrawing = 0
fracturesLUT.ShowDataHistogram = 0
fracturesLUT.AutomaticDataHistogramComputation = 0
fracturesLUT.DataHistogramNumberOfBins = 10
fracturesLUT.ColorSpace = 'Diverging'
fracturesLUT.UseBelowRangeColor = 0
fracturesLUT.BelowRangeColor = [0.0, 0.0, 0.0]
fracturesLUT.UseAboveRangeColor = 0
fracturesLUT.AboveRangeColor = [0.5, 0.5, 0.5]
fracturesLUT.NanColor = [1.0, 1.0, 0.0]
fracturesLUT.NanOpacity = 1.0
fracturesLUT.Discretize = 1
fracturesLUT.NumberOfTableValues = 256
fracturesLUT.ScalarRangeInitialized = 1.0
fracturesLUT.HSVWrap = 0
fracturesLUT.VectorComponent = 0
fracturesLUT.VectorMode = 'Magnitude'
fracturesLUT.AllowDuplicateScalars = 1
fracturesLUT.Annotations = []
fracturesLUT.ActiveAnnotatedValues = []
fracturesLUT.IndexedColors = []
fracturesLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'Fractures'
fracturesPWF = GetOpacityTransferFunction('Fractures')
fracturesPWF.Points = [-1.0, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]
fracturesPWF.AllowDuplicateScalars = 1
fracturesPWF.UseLogScale = 0
fracturesPWF.ScalarRangeInitialized = 1

# layout/tab size in pixels
#layout1.SetSize(972, 528)

# # set the view size: (important so that the colorbar has a reasonable size)
renderView1.ViewSize=[971, 528]

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.49875, 0.496315801, 2.712704029172661]
renderView1.CameraFocalPoint = [0.49875, 0.496315801, 0.0]
renderView1.CameraParallelScale = 0.7020994664762287

# save animation
SaveAnimation('fractures.png', renderView1, ImageResolution=[972, 528],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    FrameRate=1,
    FrameWindow=[0, len(FileName)], 
    # PNG options
    CompressionLevel='5',
    SuffixFormat='.%04d')
# save animation VIDEO
SaveAnimation('fracturesVideo.avi', renderView1, ImageResolution=[972, 528],
    FrameWindow=[0, len(FileName)])
'''
=============================================
-------------- END OF FRACTURES -------------
=============================================
'''
# set scalar coloring
ColorBy(tableToPoints1Display, ('POINTS', 'Porosity'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(fracturesLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
tableToPoints1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tableToPoints1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Porosity'
porosityLUT = GetColorTransferFunction('Porosity')
porosityLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
porosityLUT.InterpretValuesAsCategories = 0
porosityLUT.AnnotationsInitialized = 0
porosityLUT.ShowCategoricalColorsinDataRangeOnly = 0
porosityLUT.RescaleOnVisibilityChange = 0
porosityLUT.EnableOpacityMapping = 0
porosityLUT.RGBPoints = [0.102867839, 0.231373, 0.298039, 0.752941, 0.11613101350000002, 0.865003, 0.865003, 0.865003, 0.12939418800000002, 0.705882, 0.0156863, 0.14902]
porosityLUT.UseLogScale = 0
porosityLUT.UseOpacityControlPointsFreehandDrawing = 0
porosityLUT.ShowDataHistogram = 0
porosityLUT.AutomaticDataHistogramComputation = 0
porosityLUT.DataHistogramNumberOfBins = 10
porosityLUT.ColorSpace = 'Diverging'
porosityLUT.UseBelowRangeColor = 0
porosityLUT.BelowRangeColor = [0.0, 0.0, 0.0]
porosityLUT.UseAboveRangeColor = 0
porosityLUT.AboveRangeColor = [0.5, 0.5, 0.5]
porosityLUT.NanColor = [1.0, 1.0, 0.0]
porosityLUT.NanOpacity = 1.0
porosityLUT.Discretize = 1
porosityLUT.NumberOfTableValues = 256
porosityLUT.ScalarRangeInitialized = 1.0
porosityLUT.HSVWrap = 0
porosityLUT.VectorComponent = 0
porosityLUT.VectorMode = 'Magnitude'
porosityLUT.AllowDuplicateScalars = 1
porosityLUT.Annotations = []
porosityLUT.ActiveAnnotatedValues = []
porosityLUT.IndexedColors = []
porosityLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'Porosity'
porosityPWF = GetOpacityTransferFunction('Porosity')
porosityPWF.Points = [0.102867839, 0.0, 0.5, 0.0, 0.12939418800000002, 1.0, 0.5, 0.0]
porosityPWF.AllowDuplicateScalars = 1
porosityPWF.UseLogScale = 0
porosityPWF.ScalarRangeInitialized = 1

# get color legend/bar for porosityLUT in view renderView1
porosityLUTColorBar = GetScalarBar(porosityLUT, renderView1)
porosityLUTColorBar.AutoOrient = 1
porosityLUTColorBar.Orientation = 'Vertical'
porosityLUTColorBar.WindowLocation = 'LowerRightCorner'
porosityLUTColorBar.Position = [0.89, 0.02]
porosityLUTColorBar.Title = 'Porosity'
porosityLUTColorBar.ComponentTitle = ''
porosityLUTColorBar.TitleJustification = 'Centered'
porosityLUTColorBar.HorizontalTitle = 0
porosityLUTColorBar.TitleOpacity = 1.0
porosityLUTColorBar.TitleFontFamily = 'Arial'
porosityLUTColorBar.TitleFontFile = ''
porosityLUTColorBar.TitleBold = 0
porosityLUTColorBar.TitleItalic = 0
porosityLUTColorBar.TitleShadow = 0
porosityLUTColorBar.TitleFontSize = 16
porosityLUTColorBar.LabelOpacity = 1.0
porosityLUTColorBar.LabelFontFamily = 'Arial'
porosityLUTColorBar.LabelFontFile = ''
porosityLUTColorBar.LabelBold = 0
porosityLUTColorBar.LabelItalic = 0
porosityLUTColorBar.LabelShadow = 0
porosityLUTColorBar.LabelFontSize = 16
porosityLUTColorBar.AutomaticLabelFormat = 1
porosityLUTColorBar.LabelFormat = '%-#6.3g'
porosityLUTColorBar.DrawTickMarks = 1
porosityLUTColorBar.DrawTickLabels = 1
porosityLUTColorBar.UseCustomLabels = 0
porosityLUTColorBar.CustomLabels = []
porosityLUTColorBar.AddRangeLabels = 1
porosityLUTColorBar.RangeLabelFormat = '%-#6.1e'
porosityLUTColorBar.DrawAnnotations = 1
porosityLUTColorBar.AddRangeAnnotations = 0
porosityLUTColorBar.AutomaticAnnotations = 0
porosityLUTColorBar.DrawNanAnnotation = 0
porosityLUTColorBar.NanAnnotation = 'NaN'
porosityLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
porosityLUTColorBar.ReverseLegend = 0
porosityLUTColorBar.ScalarBarThickness = 16
porosityLUTColorBar.ScalarBarLength = 0.33

# change scalar bar placement
porosityLUTColorBar.WindowLocation = 'AnyLocation'
porosityLUTColorBar.Position = [0.7664609053497944, 0.3446969696969697]
porosityLUTColorBar.ScalarBarLength = 0.32999999999999996

# layout/tab size in pixels
#layout1.SetSize(972, 528)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.49875, 0.496315801, 10000.0]
renderView1.CameraFocalPoint = [0.49875, 0.496315801, 0.0]
renderView1.CameraParallelScale = 0.7020994664762287

# save animation
SaveAnimation('porosity-variation.png', renderView1, ImageResolution=[972, 528],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    FrameRate=1,
    FrameWindow=[0, len(FileName)], 
    # PNG options
    CompressionLevel='5',
    SuffixFormat='.%04d')

# save animation VIDEO
SaveAnimation('porosityVideo.avi', renderView1, ImageResolution=[972, 528],
    FrameWindow=[0, len(FileName)])

'''
===========================
------END OF POROSITY------
===========================
'''

# set scalar coloring
ColorBy(tableToPoints1Display, ('POINTS', 'Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(porosityLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
tableToPoints1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
tableToPoints1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')
pressureLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
pressureLUT.InterpretValuesAsCategories = 0
pressureLUT.AnnotationsInitialized = 0
pressureLUT.ShowCategoricalColorsinDataRangeOnly = 0
pressureLUT.RescaleOnVisibilityChange = 0
pressureLUT.EnableOpacityMapping = 0
pressureLUT.RGBPoints = [9800000.0, 0.231373, 0.298039, 0.752941, 14710000.0, 0.865003, 0.865003, 0.865003, 19620000.0, 0.705882, 0.0156863, 0.14902]
pressureLUT.UseLogScale = 0
pressureLUT.UseOpacityControlPointsFreehandDrawing = 0
pressureLUT.ShowDataHistogram = 0
pressureLUT.AutomaticDataHistogramComputation = 0
pressureLUT.DataHistogramNumberOfBins = 10
pressureLUT.ColorSpace = 'Diverging'
pressureLUT.UseBelowRangeColor = 0
pressureLUT.BelowRangeColor = [0.0, 0.0, 0.0]
pressureLUT.UseAboveRangeColor = 0
pressureLUT.AboveRangeColor = [0.5, 0.5, 0.5]
pressureLUT.NanColor = [1.0, 1.0, 0.0]
pressureLUT.NanOpacity = 1.0
pressureLUT.Discretize = 1
pressureLUT.NumberOfTableValues = 256
pressureLUT.ScalarRangeInitialized = 1.0
pressureLUT.HSVWrap = 0
pressureLUT.VectorComponent = 0
pressureLUT.VectorMode = 'Magnitude'
pressureLUT.AllowDuplicateScalars = 1
pressureLUT.Annotations = []
pressureLUT.ActiveAnnotatedValues = []
pressureLUT.IndexedColors = []
pressureLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'Pressure'
pressurePWF = GetOpacityTransferFunction('Pressure')
pressurePWF.Points = [9800000.0, 0.0, 0.5, 0.0, 19620000.0, 1.0, 0.5, 0.0]
pressurePWF.AllowDuplicateScalars = 1
pressurePWF.UseLogScale = 0
pressurePWF.ScalarRangeInitialized = 1

# get color legend/bar for pressureLUT in view renderView1
pressureLUTColorBar = GetScalarBar(pressureLUT, renderView1)
pressureLUTColorBar.AutoOrient = 1
pressureLUTColorBar.Orientation = 'Vertical'
pressureLUTColorBar.WindowLocation = 'LowerRightCorner'
pressureLUTColorBar.Position = [0.89, 0.02]
pressureLUTColorBar.Title = 'Pressure'
pressureLUTColorBar.ComponentTitle = ''
pressureLUTColorBar.TitleJustification = 'Centered'
pressureLUTColorBar.HorizontalTitle = 0
pressureLUTColorBar.TitleOpacity = 1.0
pressureLUTColorBar.TitleFontFamily = 'Arial'
pressureLUTColorBar.TitleFontFile = ''
pressureLUTColorBar.TitleBold = 0
pressureLUTColorBar.TitleItalic = 0
pressureLUTColorBar.TitleShadow = 0
pressureLUTColorBar.TitleFontSize = 16
pressureLUTColorBar.LabelOpacity = 1.0
pressureLUTColorBar.LabelFontFamily = 'Arial'
pressureLUTColorBar.LabelFontFile = ''
pressureLUTColorBar.LabelBold = 0
pressureLUTColorBar.LabelItalic = 0
pressureLUTColorBar.LabelShadow = 0
pressureLUTColorBar.LabelFontSize = 16
pressureLUTColorBar.AutomaticLabelFormat = 1
pressureLUTColorBar.LabelFormat = '%-#6.3g'
pressureLUTColorBar.DrawTickMarks = 1
pressureLUTColorBar.DrawTickLabels = 1
pressureLUTColorBar.UseCustomLabels = 0
pressureLUTColorBar.CustomLabels = []
pressureLUTColorBar.AddRangeLabels = 1
pressureLUTColorBar.RangeLabelFormat = '%-#6.1e'
pressureLUTColorBar.DrawAnnotations = 1
pressureLUTColorBar.AddRangeAnnotations = 0
pressureLUTColorBar.AutomaticAnnotations = 0
pressureLUTColorBar.DrawNanAnnotation = 0
pressureLUTColorBar.NanAnnotation = 'NaN'
pressureLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
pressureLUTColorBar.ReverseLegend = 0
pressureLUTColorBar.ScalarBarThickness = 16
pressureLUTColorBar.ScalarBarLength = 0.33

# change scalar bar placement
pressureLUTColorBar.WindowLocation = 'AnyLocation'
pressureLUTColorBar.Position = [0.7489711934156378, 0.35227272727272724]
pressureLUTColorBar.ScalarBarLength = 0.33

# layout/tab size in pixels
#layout1.SetSize(972, 528)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.49875, 0.496315801, 10000.0]
renderView1.CameraFocalPoint = [0.49875, 0.496315801, 0.0]
renderView1.CameraParallelScale = 0.7020994664762287

# save animation
SaveAnimation('pressure.png', renderView1, ImageResolution=[972, 528],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0,
    FrameRate=1,
    FrameWindow=[0, len(FileName)], 
    # PNG options
    CompressionLevel='5',
    SuffixFormat='.%04d')

# save animation VIDEO
SaveAnimation('pressureVideo.avi', renderView1, ImageResolution=[972, 528],
    FrameWindow=[0, len(FileName)])

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
#layout1.SetSize(972, 528)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.49875, 0.496315801, 10000.0]
renderView1.CameraFocalPoint = [0.49875, 0.496315801, 0.0]
renderView1.CameraParallelScale = 0.7020994664762287

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
