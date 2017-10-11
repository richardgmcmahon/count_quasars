import configparser
import numpy as np

conf = configparser.SafeConfigParser()
conf.read("countQuasars.conf")

# get general config params

f = conf.get("general", "filter")
reddening = conf.getfloat("general", "reddening")
skyArea = conf.getfloat("general", "area")
qlfParamsFilename = conf.get("general", "qlfParamsFilename")

# get SED config params
sedDir = conf.get("sed", "sedDir")
sedFilenameFormat = conf.get("sed", "sedFilenameFormat")

# get integral config params
zMin = conf.getfloat("integral", "zMin")
zMax = conf.getfloat("integral", "zMax")
zStep = conf.getfloat("integral", "zStep")

M1450Min = conf.getfloat("integral", "M1450Min")
M1450Max = conf.getfloat("integral", "M1450Max")
M1450Step = conf.getfloat("integral", "M1450Step")

# get cosmology config params
km_s_Mpc2Hz = 3.24077828 * 10**-20
m2pc = 3.24078e-17
c = 3. * 10**8
H0 = conf.getfloat("cosmology", "H0") * km_s_Mpc2Hz
DH = c / H0
omegaM = conf.getfloat("cosmology", "omegaM")
omegaLambda = 1 - omegaM

# get plot config params
plotTitle = conf.get("plot", "plotTitle")
plotYMin = conf.getfloat("plot", "yMin")
plotGrid = conf.getboolean("plot", "plotGrid")

minLimitingDepth = conf.getfloat("plot", "minLimitingDepth")
maxLimitingDepth = conf.getfloat("plot", "maxLimitingDepth")
limitingDepthStep = 0.1

zCutoffs = map(float, conf.get("plot", "zCutoffs").split(","))
zCutoffs = np.array(list(zCutoffs))
zColors = list(map(str.strip, conf.get("plot", "zColors").split(",")))
if len(zCutoffs) != len(zColors):
    raise ValueError("zCutoffs and zColors must have the same length in " +
                     "the configuration file")

errorEnvelopeAlpha = conf.getfloat("plot", "errorEnvelopeAlpha")
errorNSigma = conf.getfloat("plot", "errorNSigma")

# get achievedMedianDepths config params
depths = conf.get("achievedMedianDepths", f + "Depths")
depths = list(map(float, depths.split(",")))
labels = conf.get("achievedMedianDepths", f + "Labels")
labels = list(map(str.strip, labels.split(",")))
depthNSigma = conf.getint("achievedMedianDepths", f + "NSigma")
depthLabelXs = conf.get("achievedMedianDepths", f + "LabelXs")
depthLabelXs = list(map(float, depthLabelXs.split(",")))
depthLabelYs = conf.get("achievedMedianDepths", f + "LabelYs")
depthLabelYs = list(map(float, depthLabelYs.split(",")))

if not (len(depthLabelXs) == len(depthLabelYs) == len(depths) == len(labels)):
    raise ValueError("The depths, labels, and labelX and labelY arrays " +
                     "must all be the same length in the .conf")

