# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 12:16:33 2018

@author: SMukherjee
"""

import numpy


def gmm_scoring_singleThread(ubm, enroll, ndx, feature_server, score_mat, seg_idx=None):

    if seg_idx is None:
            seg_idx = range(ndx.segset.shape[0])
    
    for ts in range(0,len(seg_idx)): 
        # Select the models to test with the current segment
        models = ndx.modelset[ndx.trialmask[:, ts]]
        ind_dict = dict((k, i) for i, k in enumerate(ndx.modelset))
        inter = set(ind_dict.keys()).intersection(models)
        idx_ndx = [ind_dict[x] for x in inter]
        ind_dict = dict((k, i) for i, k in enumerate(enroll.modelset))
        inter = set(ind_dict.keys()).intersection(models)
        idx_enroll = [ind_dict[x] for x in inter]

        # Load feature file
        cep, _ = feature_server.load(ndx.segset[ts])
        
        llr = numpy.zeros(numpy.array(idx_enroll).shape)
        for m in range(llr.shape[0]):
            # Compute llk for the current model
            if ubm.invcov.ndim == 2:
                lp = ubm.compute_log_posterior_probabilities(cep, enroll.stat1[idx_enroll[m], :])
            elif ubm.invcov.ndim == 3:
                lp = ubm.compute_log_posterior_probabilities_full(cep, enroll.stat1[idx_enroll[m], :])
            pp_max = numpy.max(lp, axis=1)
            log_lk = pp_max + numpy.log(numpy.sum(numpy.exp((lp.transpose() - pp_max).transpose()), axis=1))
            llr[m] = log_lk.mean()
       
        # Compute and substract llk for the ubm
        if ubm.invcov.ndim == 2:
            lp = ubm.compute_log_posterior_probabilities(cep)
        elif ubm.invcov.ndim == 3:
            lp = ubm.compute_log_posterior_probabilities_full(cep)
        ppMax = numpy.max(lp, axis=1)
        loglk = ppMax + numpy.log(numpy.sum(numpy.exp((lp.transpose() - ppMax).transpose()), axis=1))
        llr = llr - loglk.mean()

        # Fill the score matrix
        score_mat[idx_ndx, ts] = llr
        print(ts)


def gmm_scoring_singleThread_twoModels(ubm, enroll, ndx, feature_server, score_mat, ubm_mat, seg_idx=None):

    if seg_idx is None:
            seg_idx = range(ndx.segset.shape[0])
    
    for ts in range(0,len(seg_idx)): 
        # Select the models to test with the current segment
        models = ndx.modelset[ndx.trialmask[:, ts]]
        ind_dict = dict((k, i) for i, k in enumerate(ndx.modelset))
        inter = set(ind_dict.keys()).intersection(models)
        idx_ndx = [ind_dict[x] for x in inter]
        ind_dict = dict((k, i) for i, k in enumerate(enroll.modelset))
        inter = set(ind_dict.keys()).intersection(models)
        idx_enroll = [ind_dict[x] for x in inter]

        # Load feature file
        cep, _ = feature_server.load(ndx.segset[ts])
        
        llr = numpy.zeros(numpy.array(idx_enroll).shape)
        for m in range(llr.shape[0]):
            # Compute llk for the current model
            if ubm.invcov.ndim == 2:
                lp = ubm.compute_log_posterior_probabilities(cep, enroll.stat1[idx_enroll[m], :])
            elif ubm.invcov.ndim == 3:
                lp = ubm.compute_log_posterior_probabilities_full(cep, enroll.stat1[idx_enroll[m], :])
            pp_max = numpy.max(lp, axis=1)
            log_lk = pp_max + numpy.log(numpy.sum(numpy.exp((lp.transpose() - pp_max).transpose()), axis=1))
            llr[m] = log_lk.mean()
       
        # Compute and substract llk for the ubm
        if ubm.invcov.ndim == 2:
            lp = ubm.compute_log_posterior_probabilities(cep)
        elif ubm.invcov.ndim == 3:
            lp = ubm.compute_log_posterior_probabilities_full(cep)
        ppMax = numpy.max(lp, axis=1)
        loglk = ppMax + numpy.log(numpy.sum(numpy.exp((lp.transpose() - ppMax).transpose()), axis=1))
        llr_ubm = loglk.mean()

        # Fill the score matrix
        score_mat[idx_ndx, ts] = llr
        ubm_mat[ts] = llr_ubm
        print(ts)
        
        
        
        
        
        
        
        
        
        
        
        