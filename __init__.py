# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DiversityCalc
                                 A QGIS plugin
 Calculates biodiversity indexes (Richness, Shannons and Simpsons)
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-03-07
        copyright            : (C) 2024 by Aloísio Ângelo
        email                : aloisioneto432@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DiversityCalc class from file DiversityCalc.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .diversity_calc import DiversityCalc
    return DiversityCalc(iface)
