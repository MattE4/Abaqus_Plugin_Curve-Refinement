from abaqus import *
from abaqusConstants import *
from caeModules import *

def curveRefinement(kw_crl=None):
    
    vpName = session.currentViewportName
    modelname = session.viewports[vpName].displayedObject.modelName
    
    m = mdb.models[modelname]
    
    if kw_crl == 'Fine':
    	level = FINE
    elif kw_crl == 'Extra Coarse':
    	level = EXTRA_COARSE
    elif kw_crl == 'Coarse':
    	level = COARSE
    elif kw_crl == 'Medium':
    	level = MEDIUM
    elif kw_crl == 'Extra Fine':
    	level = EXTRA_FINE
    else:
    	level = FINE
    
    
    for i in m.parts.keys():
        if len(m.parts[i].edges) > 0:
            m.parts[i].setValues(geometryRefinement=level)
    
    m.rootAssembly.regenerate()