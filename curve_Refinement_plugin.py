from abaqusGui import getAFXApp, Activator, AFXMode
from abaqusConstants import ALL
import os
thisPath = os.path.abspath(__file__)
thisDir = os.path.dirname(thisPath)

toolset = getAFXApp().getAFXMainWindow().getPluginToolset()
toolset.registerGuiMenuButton(
    buttonText='Set Curve Refinement', 
    object=Activator(os.path.join(thisDir, 'curve_RefinementDB.py')),
    kernelInitString='import curve_refinement_kernel',
    messageId=AFXMode.ID_ACTIVATE,
    icon=None,
    applicableModules=['Part', 'Property', 'Assembly', 'Step', 'Interaction', 'Load', 'Mesh', 'Optimization'],
    version='1.0',
    author='Matthias Ernst',
    description='Change curve refinement for all parts (with geometry) of currently displayed model.',
    helpUrl='N/A'
)
