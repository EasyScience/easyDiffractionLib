#  SPDX-FileCopyrightText: 2024 easyDiffraction contributors  <support@easydiffraction.software>
#  SPDX-License-Identifier: BSD-3-Clause
#  © 2021-2024 Contributors to the easydiffraction project <https://github.com/easyScience/easydiffraction


from easyscience.Datasets.xarray import xr
from easyscience.Objects.Job.Experiment import ExperimentBase as coreExperiment


class Experiment(coreExperiment):
    """
    Diffraction-specific Experiment object.
    """
    def __init__(self, name: str, dataset: xr.Dataset = None, *args, **kwargs):
        super(Experiment, self).__init__(name, *args, **kwargs)
        self._name = name

        self.is_tof = False
        self.is_polarized = False
        self.is_single_crystal = False
        self._simulation_prefix = "sim_"
        self._dataset = dataset if dataset is not None else xr.Dataset()


    @staticmethod
    def from_cif(cif_file: str):
        """
        Load the experiment from a CIF file
        """
        # TODO: Implement this
        return Experiment("Experiment")

    @staticmethod
    def from_cif_strig(cif_string: str):
        """
        Load the experiment from a string
        """
        # TODO: Implement this
        return Experiment("Experiment")

    # required dunder methods
    def __str__(self):
        return f"Experiment: {self._name}"
    
    def as_dict(self, skip: list = []) -> dict:
        this_dict = super(Experiment, self).as_dict(skip=skip)
        return this_dict