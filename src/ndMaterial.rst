.. include:: sub.txt

===========================
 nDMaterial commands
===========================

.. function:: nDMaterial(matType, matTag, *matArgs)

   This command is used to construct an NDMaterial object which represents the stress-strain relationship at the gauss-point of a continuum element.

   ================================   ===========================================================================
   ``matType`` |str|                  material type
   ``matTag`` |int|                   material tag.
   ``matArgs`` |list|                 a list of material arguments, must be preceded with ``*``.
   ================================   ===========================================================================

For example,

.. code-block:: python

   matType = 'ElasticIsotropic'
   matTag = 1
   matArgs = [E, v]
   nDMaterial(matType, matTag, *matArgs)



The following contain information about available ``matType``:

#. :doc:`elasticIsotropic`
#. :doc:`elasticOrthotropic`
#. :doc:`J2Plasticity`
#. :doc:`DrunkerPrager`
#. :doc:`Damage2p`
#. :doc:`PlaneStress`
#. :doc:`PlaneStrain`
#. :doc:`MultiAxialCyclicPlasticity`
#. :doc:`BoundingCamClay`
#. :doc:`PlateFiber`
#. :doc:`FSAM`
#. :doc:`ManzariDafalias`
#. :doc:`PM4Sand`
#. :doc:`StressDensityModel`
#. :doc:`AcousticMedium`


.. toctree::
   :maxdepth: 2
   :hidden:

   elasticIsotropic
   elasticOrthotropic
   J2Plasticity
   DrunkerPrager
   Damage2p
   PlaneStress
   PlaneStrain
   MultiAxialCyclicPlasticity
   BoundingCamClay
   PlateFiber
   FSAM
   ManzariDafalias
   PM4Sand
   StressDensityModel
   AcousticMedium


Tsinghua Sand Models
---------------------

#. :doc:`CycLiqCP`
#. :doc:`CycLiqCPSP`


.. toctree::
   :maxdepth: 2
   :hidden:

   CycLiqCP
   CycLiqCPSP


Materials for Modeling Concrete Walls
-------------------------------------


#. :doc:`PlaneStressUserMaterial`
#. :doc:`PlateFromPlaneStress`
#. :doc:`PlateRebar`


.. toctree::
   :maxdepth: 2
   :hidden:

   PlaneStressUserMaterial
   PlateFromPlaneStress
   PlateRebar

Contact Materials for 2D and 3D
-------------------------------


#. :doc:`ContactMaterial2D`
#. :doc:`ContactMaterial3D`


.. toctree::
   :maxdepth: 2
   :hidden:

   ContactMaterial2D
   ContactMaterial3D

Wrapper material for Initial State Analysis
-------------------------------------------

#. :doc:`InitialStateAnalysisWrapper`

.. toctree::
   :maxdepth: 2
   :hidden:

   InitialStateAnalysisWrapper

UC San Diego soil models
------------------------


#. :doc:`PressureIndependMultiYield`
#. :doc:`PressureDependMultiYield`
#. :doc:`PressureDependMultiYield02`


.. toctree::
   :maxdepth: 2
   :hidden:

   PressureIndependMultiYield
   PressureDependMultiYield
   PressureDependMultiYield02


UC San Diego Saturated Undrained soil
-------------------------------------

#. :doc:`FluidSolidPorousMaterial`

.. toctree::
   :maxdepth: 2
   :hidden:

   FluidSolidPorousMaterial
