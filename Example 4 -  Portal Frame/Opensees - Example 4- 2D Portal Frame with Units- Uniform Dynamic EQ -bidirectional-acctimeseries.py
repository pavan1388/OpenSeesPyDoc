# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:12:06 2019

@author: pchi893
"""
# Converted to openseespy by: Pavan Chigullapally       
#                         University of Auckland  
#                         Email: pchi893@aucklanduni.ac.nz 
# --------------------------------------------------------------------------------------------------
# Example4. 2D Portal Frame--  Dynamic EQ input analysis -- bidirectional - uniform excitation
#                              Silvia Mazzoni & Frank McKenna, 2006
#the problem description can be found here: http://opensees.berkeley.edu/wiki/index.php/Examples_Manual  (example: 4)
# execute this file after you have built the model, and after you apply gravity
#
# Bidirectional Uniform Earthquake ground motion (uniform acceleration input at all support nodes)
##########################################################################################################################################################################
import openseespy.opensees as op
#import the os module
#import os
import math
op.wipe()
##########################################################################################################################################################################

from InelasticFiberSectionPortal2Dframe import *
# execute this file after you have built the model, and after you apply gravity
#

# MultipleSupport Earthquake ground motion (different displacement input at spec'd support nodes) -- two nodes here

#applying Dynamic Ground motion analysis
#iSupportNode = [1, 2]
iGMfact = [1.5, 0.25]
iGMdirection = [1, 2]
iGMfile = ['H-E01140', 'H-E12140']
DtAnalysis = 0.01*sec # time-step Dt for lateral analysis
TmaxAnalysis = 10.0*sec # maximum duration of ground-motion analysis
Tol = 1e-8

# define DAMPING--------------------------------------------------------------------------------------
# apply Rayleigh DAMPING from $xDamp
# D=$alphaM*M + $betaKcurr*Kcurrent + $betaKcomm*KlastCommit + $beatKinit*$Kinitial
Lambda = op.eigen('-fullGenLapack', 1) # eigenvalue mode 1
Omega = math.pow(Lambda, 0.5)
betaKcomm = 2 * (0.02/Omega)

xDamp = 0.02				# 2% damping ratio
alphaM = 0.0				# M-prop. damping; D = alphaM*M	
betaKcurr = 0.0		# K-proportional damping;      +beatKcurr*KCurrent
betaKinit = 0.0 # initial-stiffness proportional damping      +beatKinit*Kini

op.rayleigh(alphaM,betaKcurr, betaKinit, betaKcomm) # RAYLEIGH damping
#--------------------------------------------------------------------------------------
#  ---------------------------------    perform Dynamic Ground-Motion Analysis
# the following commands are unique to the Multiple-Support Earthquake excitation
# Set some parameters
IDloadTag = 400			# load tag


# read a PEER strong motion database file, extracts dt from the header and converts the file 
# to the format OpenSees expects for Uniform/multiple-support ground motions
record = ['H-E01140', 'H-E12140']
#dt =[]
#nPts = []

import ReadRecord

#this is similar to uniform excitation in single direction
count = 2
for i in range(len(iGMdirection)):
    IDloadTag = IDloadTag+count
    record_single = record[i]
    GMfatt = (iGMfact[i])*g
    dt, nPts = ReadRecord.ReadRecord(record_single+'.AT2', record_single+'.dat')
    op.timeSeries('Path', count, '-dt', dt, '-filePath', record_single+'.dat', '-factor', GMfatt)
    op.pattern('UniformExcitation', IDloadTag, iGMdirection[i], '-accel', 2)
    count = count + 1

maxNumIter = 10
op.wipeAnalysis()
op.constraints('Transformation')
op.numberer('RCM')
op.system('BandGeneral')
#op.test('EnergyIncr', Tol, maxNumIter)
#op.algorithm('ModifiedNewton')
#NewmarkGamma = 0.5
#NewmarkBeta = 0.25
#op.integrator('Newmark', NewmarkGamma, NewmarkBeta)
#op.analysis('Transient')


#Nsteps =  int(TmaxAnalysis/ DtAnalysis)
#
#ok = op.analyze(Nsteps, DtAnalysis)

tCurrent = op.getTime()

# for gravity analysis, load control is fine, 0.1 is the load factor increment (http://opensees.berkeley.edu/wiki/index.php/Load_Control)

test = {1:'NormDispIncr', 2: 'RelativeEnergyIncr', 3:'EnergyIncr', 4: 'RelativeNormUnbalance',5: 'RelativeNormDispIncr', 6: 'NormUnbalance'}
algorithm = {1:'KrylovNewton', 2: 'SecantNewton' , 3:'ModifiedNewton' , 4: 'RaphsonNewton',5: 'PeriodicNewton', 6: 'BFGS', 7: 'Broyden', 8: 'NewtonLineSearch'}

#tFinal = TmaxAnalysis
tFinal = nPts*dt
time = [tCurrent]
u3 = [0.0]
u4 = [0.0]
ok = 0

while tCurrent < tFinal:
#    ok = op.analyze(1, .01)     
    for i in test:
        for j in algorithm: 
            if j < 4:
                op.algorithm(algorithm[j], '-initial')
                
            else:
                op.algorithm(algorithm[j])
            while ok == 0 and tCurrent < tFinal:
                    
                op.test(test[i], Tol, maxNumIter)        
                NewmarkGamma = 0.5
                NewmarkBeta = 0.25
                op.integrator('Newmark', NewmarkGamma, NewmarkBeta)
                op.analysis('Transient')
                ok = op.analyze(1, .01)
                
                if ok == 0 :
                    tCurrent = op.getTime()                
                    time.append(tCurrent)
                    u3.append(op.nodeDisp(3,1))
                    u4.append(op.nodeDisp(4,1))
                    print(test[i], algorithm[j], 'tCurrent=', tCurrent)
       
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
plt.plot(time, u3)
plt.ylabel('Horizontal Displacement of node 3 (in)')
plt.xlabel('Time (s)')
plt.savefig('Horizontal Disp at Node 3 vs time-uniform excitation-acctime.jpeg', dpi = 500)
plt.show()

plt.figure(figsize=(8,8))
plt.plot(time, u4)
plt.ylabel('Horizontal Displacement of node 4 (in)')
plt.xlabel('Time (s)')
plt.savefig('Horizontal Disp at Node 4 vs time-uniform excitation-acctime.jpeg', dpi = 500)
plt.show() 
#

op.wipe()