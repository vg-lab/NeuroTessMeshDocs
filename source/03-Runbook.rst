=======
Runbook
=======

.. note::
   This runbook will test the main functionalities of NeuroTessMesh and can be considered as a basic tutorial for the application, but **not** as a complete and exhaustive tutorial of all its functionalities. This runbook is up to date with NeuroTessMesh version 0.4.3 (some images are from version 0.4.0). 

1. Load a "swc" file (:numref:`fig5`). 

.. _fig5:

.. figure:: images/NTMimage005.png
   :alt: Opening a file.
   :align: center
   :width: 999
   :scale: 60%

   Opening a file.
   
.. raw:: latex

    \clearpage   

2. Visualize and navigate through the reconstructed neuronal mesh using the scene camera controls as previously explained in user interface section (:numref:`fig6`).

.. _fig6:

.. figure:: images/NTMimage006.png
   :alt: 3D view navigation.
   :align: center
   :width: 1020
   :scale: 60%

   3D View navigation.
   
.. raw:: latex

    \clearpage   

3. Change the render options. In this example the Subdivision level has been increased to 10, the Distance threshold has been also increased and the Tessellation criteria has been modified to Homogeneous criteria (:numref:`fig7`).

.. _fig7:

.. figure:: images/NTMimage007.png
   :alt: Render options manipulation.
   :align: center
   :width: 1020
   :scale: 60%

   Render options manipulation.
   
.. raw:: latex

    \clearpage

4. Modify the soma reconstruction params. In this example the soma volume has been decreased setting the Radius factor to 0.75 and the starting points of the neurites have been displaced using the Neurite [n] factors (:numref:`fig8`).

.. _fig8:

.. figure:: images/NTMimage008.png
   :alt: Reconstruction parameters manipulation.
   :align: center
   :width: 1020
   :scale: 60%

   Reconstruction parameters manipulation.

.. raw:: latex

    \clearpage
    
5. Save the results to a "obj" file (:numref:`fig9`). 

.. _fig9:

.. figure:: images/NTMimage009.png
   :alt: Save to file.
   :align: center
   :width: 999
   :scale: 60%

   Save results to file.

  
