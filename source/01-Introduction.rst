==========================
NeuroTessMesh Introduction
==========================

**NeuroLOTs** is a set of libraries and tools that implement a method for generating neuronal meshes and for visualizing them at different levels of detail using GPU-based tessellation. As a part of NeuroLOTs, **NeuroTessMesh** provides a visual environment for the generation of 3D polygonal meshes that approximate the membrane of neuronal cells, from the morphological tracings that describe the morphology of the neurons. The 3D models can be tessellated at different levels of detail, providing either homogeneous or adaptive resolution along the model. The soma shape is recovered from the incomplete information of the tracings, applying a physical deformation model that can be interactively adjusted. The adaptive refinement process performed in the GPU generates meshes that allow good visual quality geometries at an affordable computational cost, both in terms of memory and rendering time. NeuroTessMesh is the front-end GUI to NeuroLOTs framework. 

This documentation is for NeuroTessMesh version 0.5.2 software that can be obtained from the homepage.

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

NeuroTessMesh can be downloaded from the `NeuroLOTs & NeuroTessMesh Homepage`_ for Linux and Mac operating systems and executed locally. Additionally it can be executed using a docker image.

^^^^^^^^^^^^^^^^^
Docker containers
^^^^^^^^^^^^^^^^^

The docker containers for **NeuroTessMesh** can be found on `Docker Hub`_. It's recommended to use the highest tag number as it represents the latest official release.

.. _Docker Hub: https://hub.docker.com/r/vglab/neurotessmesh/tags?page=1&ordering=last_updated

^^^^^^^^^^^^^^^^^
Executing locally
^^^^^^^^^^^^^^^^^

The application options and parameters are:

.. tabularcolumns:: |p{3.5cm}|p{2.5cm}|p{9.0cm}|

+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| **OPTION**             | **PARAMETER**                   | **DESCRIPTION**                                                                          |
+========================+=================================+==========================================================================================+
| ``--version``          | *none*                          | Shows the version of the application.                                                    |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``--help``             | *none*                          | Shows the options and arguments used                                                     |
|                        |                                 | for executing the application.                                                           |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``-bc``                | *path_to_bc_file*               | Load BlueConfig file.                                                                    |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``-swc``               | *path_to_swc_file*              | Load SWC file.                                                                           |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``-xml``               | *path_to_xml_file*              | Load XML scene file.                                                                     |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``-target``            | *target_label*                  | Specifies target label of the BlueConfig file.                                           |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``-zeroeq``            | *schema_id*                     | Enables ZeroEQ communications with the specified id.                                     |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``--json``             | *path_to_json_file*             | Load JSON data file.                                                                     |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``-ws``                | *width* *height*                | Specifies the size of the application window.                                            |
|                        |                                 |                                                                                          |
| ``--window-size``      |                                 |                                                                                          |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``-fs``                | *none*                          | Sets the application window to fullscreen mode.                                          |
|                        |                                 |                                                                                          |
| ``--fullscreen``       |                                 |                                                                                          |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``-mw``                | *none*                          | Maximizes the application window to the desktop resolution.                              |
|                        |                                 |                                                                                          |
| ``--maximize-window``  |                                 |                                                                                          |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``-s``                 | *samples_number*                | Sets the samples number for OpenGL.                                                      |
|                        |                                 |                                                                                          |
| ``--samples``          |                                 | Overwritten, if present, by the enviroment variable CONTEXT_OPENGL_SAMPLES.              |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``-nvs``               | *none*                          | Disables vertical sync for OpenGL.                                                       |
|                        |                                 |                                                                                          |
| ``--no-vsync``         |                                 | Overwritten, if present, by the enviroment variable CONTEXT_OPENGL_VSYNC.                |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+
| ``-cv``                | *major* *minor*                 | Sets the OpenGL version of the application.                                              |
|                        |                                 |                                                                                          |
| ``--context-version``  |                                 | Overwritten, if present, by the enviroment variables CONTEXT_OPENGL_MAJOR and            |
|                        |                                 | CONTEXT_OPENGL_MINOR.                                                                    |
+------------------------+---------------------------------+------------------------------------------------------------------------------------------+

If the options are incompatible or its parameters invalid the application will abort the execution and will show the help message in the console.

^^^^^^^^^^^^
Test dataset
^^^^^^^^^^^^

A test data for NeuroTessMesh can be downloaded from:

* http://neuromorpho.org/dableFiles/allen%20cell%20types/CNG%20version/H16-03-001-01-09-01_559391771_m.CNG.swc

^^^^^^^^^^^^^^
Docker example
^^^^^^^^^^^^^^

.. code-block:: bash
  :linenos:
  :emphasize-lines: 7

  xhost +local:docker
  # Pull the image.
  docker pull vglab/neurotessmesh:0.5.2-nvidia-ubuntu-16.04
  # Download example data
  wget http://neuromorpho.org/dableFiles/allen%20cell%20types/CNG%20version/H16-03-001-01-09-01_559391771_m.CNG.swc
  # Run example
  docker run --gpus 1 -ti --rm -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /etc/machine-id:/etc/machine-id -v $(pwd)/H16-03-001-01-09-01_559391771_m.CNG.swc:/H16-03-001-01-09-01_559391771_m.CNG.swc --privileged vglab/neurotessmesh:0.5.2-nvidia-ubuntu-16.04 /usr/bin/NeuroTessMesh -swc /H16-03-001-01-09-01_559391771_m.CNG.swc

