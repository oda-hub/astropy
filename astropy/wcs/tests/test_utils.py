# Licensed under a 3-clause BSD style license - see LICENSE.rst
from __future__ import absolute_import, division, print_function, unicode_literals
from ...wcs import WCS
from .. import utils
import numpy as np

def test_wcs_dropping():
    wcs = WCS(naxis=4)
    wcs.wcs.pc = np.zeros([4,4])
    np.fill_diagonal(wcs.wcs.pc, np.arange(1,5))
    pc = wcs.wcs.pc # for later use below

    dropped = wcs.dropaxis(0)
    assert np.all(dropped.wcs.get_pc().diagonal() == np.array([2,3,4]))
    dropped = wcs.dropaxis(1)
    assert np.all(dropped.wcs.get_pc().diagonal() == np.array([1,3,4]))
    dropped = wcs.dropaxis(2)
    assert np.all(dropped.wcs.get_pc().diagonal() == np.array([1,2,4]))
    dropped = wcs.dropaxis(3)
    assert np.all(dropped.wcs.get_pc().diagonal() == np.array([1,2,3]))

    wcs = WCS(naxis=4)
    wcs.wcs.cd = pc

    dropped = wcs.dropaxis(0)
    assert np.all(dropped.wcs.get_pc().diagonal() == np.array([2,3,4]))
    dropped = wcs.dropaxis(1)
    assert np.all(dropped.wcs.get_pc().diagonal() == np.array([1,3,4]))
    dropped = wcs.dropaxis(2)
    assert np.all(dropped.wcs.get_pc().diagonal() == np.array([1,2,4]))
    dropped = wcs.dropaxis(3)
    assert np.all(dropped.wcs.get_pc().diagonal() == np.array([1,2,3]))

def test_wcs_swapping():
    wcs = WCS(naxis=4)
    wcs.wcs.pc = np.zeros([4,4])
    np.fill_diagonal(wcs.wcs.pc, np.arange(1,5))
    pc = wcs.wcs.pc # for later use below

    swapped = wcs.swapaxes(0,1)
    assert np.all(swapped.wcs.get_pc().diagonal() == np.array([2,1,3,4]))
    swapped = wcs.swapaxes(0,3)
    assert np.all(swapped.wcs.get_pc().diagonal() == np.array([4,2,3,1]))
    swapped = wcs.swapaxes(2,3)
    assert np.all(swapped.wcs.get_pc().diagonal() == np.array([1,2,4,3]))

    wcs = WCS(naxis=4)
    wcs.wcs.cd = pc

    swapped = wcs.swapaxes(0,1)
    assert np.all(swapped.wcs.get_pc().diagonal() == np.array([2,1,3,4]))
    swapped = wcs.swapaxes(0,3)
    assert np.all(swapped.wcs.get_pc().diagonal() == np.array([4,2,3,1]))
    swapped = wcs.swapaxes(2,3)
    assert np.all(swapped.wcs.get_pc().diagonal() == np.array([1,2,4,3]))

def test_add_stokes():
    wcs = WCS(naxis=3)
    
    for ii in range(4):
        outwcs = utils.add_stokes_axis_to_wcs(wcs,ii)
        assert outwcs.wcs.naxis == 4
