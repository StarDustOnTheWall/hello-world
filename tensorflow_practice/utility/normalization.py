#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Copyright 2021 SAIC Artificial Intelligence Lab. All Rights Reserved.
# ----------------------------------------------------------------------

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, StandardScaler
from sklearn_features.transformers import DataFrameSelector

from tensorflow_practice.utility.sklearn_utility import periodic_spline_transformer


def normalization_pipe(numeric_index: list = None, cat_index: list = None, cyclic_index: list = None):
    """
    :param numeric_index:  list of numeric index
    :param cat_index: list of tuple (index, [categories]), [('promotion', [0,1,2])]
                      [categories] could be None
    :param cyclic_index:  list of tuple (index, periodicity), [('hour', 24)]
    :return:
    """
    all_feature_list = []
    if numeric_index:
        num_pipe = Pipeline([('selector', DataFrameSelector(numeric_index)),
                             ('standard', StandardScaler())
                             ])
        all_feature_list.append(('num_pipe', num_pipe))
    if cat_index:
        for cat_tuple in cat_index:
            cat_pipe = Pipeline([('selector', DataFrameSelector([cat_tuple[0]])),
                                 ('hot_code', OneHotEncoder(categories=[cat_tuple[1]] if cat_tuple[1] else 'auto'))
                                 ])
            all_feature_list.append((cat_tuple[0]+'_cat_pipe', cat_pipe))
    if cyclic_index:
        for cyclic_tuple in cyclic_index:
            cyclic_pipe = Pipeline([('selector', DataFrameSelector([cyclic_tuple[0]])),
                                    ('cyclic_transform', periodic_spline_transformer(
                                        cyclic_tuple[1], n_splines=int(cyclic_tuple[1]/2)))])
            all_feature_list.append((cyclic_tuple[0]+'_cyclic_pipe', cyclic_pipe))
    if len(all_feature_list) > 0:
        return FeatureUnion(transformer_list=all_feature_list)
    else:
        return None
