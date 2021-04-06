.. note::
   This manual is still under development and there are some incomplete parts, marked as 'Work in progress'.

==========================
NeuroTessMesh Introduction
==========================

**NeuroLOTs** is a set of libraries and tools that implement a method for generating neuronal meshes and for visualizing them at different levels of detail using GPU-based tessellation. As a part of NeuroLOTs, **NeuroTessMesh** provides a visual environment for the generation of 3D polygonal meshes that approximate the membrane of neuronal cells, from the morphological tracings that describe the morphology of the neurons. The 3D models can be tessellated at different levels of detail, providing either homogeneous or adaptive resolution along the model. The soma shape is recovered from the incomplete information of the tracings, applying a physical deformation model that can be interactively adjusted. The adaptive refinement process performed in the GPU generates meshes that allow good visual quality geometries at an affordable computational cost, both in terms of memory and rendering time. NeuroTessMesh is the front-end GUI to NeuroLOTs framework. 

---------------------
Hardware requirements
---------------------

The application requires a graphic card that supports OpenGL 4.0 at least. NVIDIA offers support for GPU tessellation from the GTX 400 serie on, and ATI/AMD from Radeon  HD  5000  serie  on.  Previous  series  of  both  companies  are  not  able  to tessellate and consequently the mesh refinement will not work. 

.. note::

   The  GPU  Tessellation  on  Intel  graphics  cards  is  present  only  on  certain models, for more information  you  can  visit  the  next  link: `Supported  APIs  and  Features  for  Intel Graphics Drivers`_
   
.. _Supported  APIs  and  Features  for  Intel Graphics Drivers: http://www.intel.com/content/www/us/en/support/graphics-drivers/000005524.html

--------------
External Links
--------------

The homepage for NeuroLOTs and NeuroTessMesh is located at `NeuroLOTs & NeuroTessMesh Homepage`_ and the source code for the latest releases is available in the `NeuroLOTs Github page`_ and `NeuroTessMesh Github page`_. For reporting bugs please use the `NeuroLOTs Github Issues`_ and the `NeuroTessMesh Github Issues`_ pages. If you have any questions or suggestions about NeuroLOTs or NeuroTessMesh refer to dev@vg-lab.es.

.. _NeuroLOTs & NeuroTessMesh Homepage: https://vg-lab.es/neurolots/
.. _NeuroLOTs Github page: https://github.com/vg-lab/neurolots
.. _NeuroTessMesh Github page: https://github.com/vg-lab/NeuroTessMesh
.. _NeuroLOTs Github Issues: https://github.com/vg-lab/visimpl/issues
.. _NeuroTessMesh Github Issues: https://github.com/vg-lab/visimpl/issues

------------------------
Installation and running
------------------------

.. note::
   Work in progress.

