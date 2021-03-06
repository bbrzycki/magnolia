"""
magnolia is a simple package for analyzing the contribution of
magnetic fields to the physics within the cores of galaxy cluster mergers
"""

__version__ = "1.0"

import sys
import os
sys.path.append(os.path.dirname(__file__))

# import derived_field_definitions

from store_dataset_info import \
    find_center, \
    generate_profiles, \
    write_profiles_to_hdf5, \
    make_profiles, \
    generate_energy_over_time, \
    write_energy_over_time_to_hdf5, \
    make_energy_over_time

from retrieve_dataset_info import \
    get_units, get_groupnames, get_fieldnames, \
    remove_group, remove_field, \
    list_groupnames, list_fieldnames, list_all_fieldnames, \
    get_field, get_mean, get_stddev, \
    density, kT, velocity_variance_radial, velocity_variance_tangential, \
    velocity_variance, velocity_mean_squared, \
    mag_field_squared_mean_radius, mag_field_squared_mean_theta, \
    mag_field_squared_mean_phi, mag_field_squared_mean, \
    mag_field_variance_radial, mag_field_variance_tangential, \
    mag_field_variance, mag_field_mean_squared, \
    mag_field_mean_squared_Cartesian, mag_field_variance_Cartesian, \
    mag_field_squared_mean_Cartesian, \
    c_s_squared, v_A_squared, n_e, entropy, \
    get_mass, get_IE, get_KE, get_tKE, get_ME

from plot_dataset_info import make_multiplot
