#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:45:11 2024

@author: matteabessette
"""

def overweight(fleet_data, passenger_data):
    general_list = [] #will contain each plane model and how many passengers have overweight bags on each plane
    specific_list  = []  #for every passenger who has an overweight bag, this list will have their name, gate number, and how much their bag exceeds the maximum weight
    for item in fleet_data:
        general_sublist = [item[0], 0] #item[0] is the plane model
        for row in passenger_data:
            if row[2] == item[4]: #comparing gate numbers
                if row[6] > item[7]: #if the bag weight exceeds the maximum
                    specific_sublist = [row[0], row[1], row[2], round(row[6] - item[7],2)] #last item is the amount the bag exceeds the maximum
                    general_sublist[1] = general_sublist[1] + 1 #running counter of how many people per plane   type have an overwight bag
                    specific_list.append(specific_sublist)
        general_list.append(general_sublist)
    return general_list, specific_list