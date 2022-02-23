#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Copyright 2021 SAIC Artificial Intelligence Lab. All Rights Reserved.
# ----------------------------------------------------------------------

import numpy as np
from sklearn.preprocessing import SplineTransformer


def periodic_spline_transformer(period, n_splines=None, degree=3):
    if n_splines is None:
        n_splines = period
    n_knots = n_splines + 1
    return SplineTransformer(degree=degree, n_knots=n_knots, extrapolation="periodic", include_bias=True,
                             knots=np.linspace(0, period, n_knots).reshape(n_knots, 1))
