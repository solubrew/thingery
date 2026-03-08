# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name: Thingery Institutions
	description: >
		Complete institutions database - universities, labs, companies
	version: 0.0.0.0.0.0
	authority: filesystem
	security: seclvl2
	<(WT)>: -32
"""
# -*- coding: utf-8 -*
from dataclasses import dataclass
from typing import List
from thingery.models import Institution, InstitutionType


# ======================================Standard Library Modules======================================================||
# ======================================3rd Party Library Modules=====================================================||
# ======================================Solutions Brewer Library Modules=============================================||
# ====================================================================================================================||


# ===========================UNIVERSITIES===========================================================================||
# ====================================================================================================================||


@dataclass
class MIT(Institution):
    def __init__(self):
        super().__init__(
            name="Massachusetts Institute of Technology",
            institution_type=InstitutionType.UNIVERSITY.value,
            location="Cambridge, USA",
            founded=1861,
            website="https://www.mit.edu",
            focus_areas=["Engineering", "Computer Science", "Physics", "Mathematics"],
            notable_research=["Quantum Computing", "AI", "Energy", "Space Exploration"]
        )


@dataclass
class Stanford(Institution):
    def __init__(self):
        super().__init__(
            name="Stanford University",
            institution_type=InstitutionType.UNIVERSITY.value,
            location="Stanford, USA",
            founded=1885,
            website="https://www.stanford.edu",
            focus_areas=["Computer Science", "Medicine", "Engineering", "Business"],
            notable_research=["AI", "Autonomous Vehicles", "Biotechnology"]
        )


@dataclass
class Harvard(Institution):
    def __init__(self):
        super().__init__(
            name="Harvard University",
            institution_type=InstitutionType.UNIVERSITY.value,
            location="Cambridge, USA",
            founded=1636,
            website="https://www.harvard.edu",
            focus_areas=["Law", "Medicine", "Business", "Arts & Sciences"],
            notable_research=["Genetics", "Climate Science", "Economics"]
        )


@dataclass
class Caltech(Institution):
    def __init__(self):
        super().__init__(
            name="California Institute of Technology",
            institution_type=InstitutionType.UNIVERSITY.value,
            location="Pasadena, USA",
            founded=1891,
            website="https://www.caltech.edu",
            focus_areas=["Science", "Engineering", "Space Exploration"],
            notable_research=["Jet Propulsion", "Quantum Information", "Astrophysics"]
        )


@dataclass
class Oxford(Institution):
    def __init__(self):
        super().__init__(
            name="University of Oxford",
            institution_type=InstitutionType.UNIVERSITY.value,
            location="Oxford, UK",
            founded=1096,
            website="https://www.ox.ac.uk",
            focus_areas=["Humanities", "Sciences", "Medicine", "Engineering"],
            notable_research=["Vaccines", "Climate Science", "AI"]
        )


@dataclass
class Cambridge(Institution):
    def __init__(self):
        super().__init__(
            name="University of Cambridge",
            institution_type=InstitutionType.UNIVERSITY.value,
            location="Cambridge, UK",
            founded=1209,
            website="https://www.cam.ac.uk",
            focus_areas=["Sciences", "Engineering", "Medicine", "Humanities"],
            notable_research=["DNA Structure", "Stephen Hawking", "Quantum Computing"]
        )


@dataclass
class ETHZurich(Institution):
    def __init__(self):
        super().__init__(
            name="ETH Zurich",
            institution_type=InstitutionType.UNIVERSITY.value,
            location="Zurich, Switzerland",
            founded=1855,
            website="https://www.ethz.ch",
            focus_areas=["Science", "Technology", "Engineering", "Mathematics"],
            notable_research=["Quantum Physics", "Robotics", "Climate Science"]
        )


@dataclass
class Tsinghua(Institution):
    def __init__(self):
        super().__init__(
            name="Tsinghua University",
            institution_type=InstitutionType.UNIVERSITY.value,
            location="Beijing, China",
            founded=1911,
            website="https://www.tsinghua.edu.cn",
            focus_areas=["Engineering", "Science", "Management", "Law"],
            notable_research=["AI", "Clean Energy", "Aerospace"]
        )


@dataclass
class Stanford2(Institution):
    def __init__(self):
        super().__init__(
            name="University of California Berkeley",
            institution_type=InstitutionType.UNIVERSITY.value,
            location="Berkeley, USA",
            founded=1868,
            website="https://www.berkeley.edu",
            focus_areas=["Computer Science", "Engineering", "Physics", "Chemistry"],
            notable_research=["DNA Technology", "Particle Physics", "AI"]
        )


@dataclass
class MIT2(Institution):
    def __init__(self):
        super().__init__(
            name="Imperial College London",
            institution_type=InstitutionType.UNIVERSITY.value,
            location="London, UK",
            founded=1907,
            website="https://www.imperial.ac.uk",
            focus_areas=["Science", "Engineering", "Medicine", "Business"],
            notable_research=["Climate Change", "Quantum Systems", "Biomedical Engineering"]
        )


# ===========================RESEARCH LABS==========================================================================||
# ====================================================================================================================||


@dataclass
class NIST(Institution):
    def __init__(self):
        super().__init__(
            name="National Institute of Standards and Technology",
            institution_type=InstitutionType.RESEARCH_LAB.value,
            location="Gaithersburg, USA",
            founded=1901,
            website="https://www.nist.gov",
            focus_areas=["Measurement Standards", "Technology", "Standards"],
            notable_research=["Atomic Clocks", "Quantum Measurement", "Cybersecurity"]
        )


@dataclass
class LosAlamos(Institution):
    def __init__(self):
        super().__init__(
            name="Los Alamos National Laboratory",
            institution_type=InstitutionType.RESEARCH_LAB.value,
            location="Los Alamos, USA",
            founded=1943,
            website="https://www.lanl.gov",
            focus_areas=["Nuclear Physics", "Computational Science", "Energy"],
            notable_research=["Manhattan Project", "Supercomputing", "Cybersecurity"]
        )


@dataclass
class OakRidge(Institution):
    def __init__(self):
        super().__init__(
            name="Oak Ridge National Laboratory",
            institution_type=InstitutionType.RESEARCH_LAB.value,
            location="Oak Ridge, USA",
            founded=1943,
            website="https://www.ornl.gov",
            focus_areas=["Energy", "Computational Science", "Materials"],
            notable_research=["Supercomputing", "Nuclear Energy", "Neutron Science"]
        )


@dataclass
class Argonne(Institution):
    def __init__(self):
        super().__init__(
            name="Argonne National Laboratory",
            institution_type=InstitutionType.RESEARCH_LAB.value,
            location="Lemont, USA",
            founded=1946,
            website="https://www.anl.gov",
            focus_areas=["Energy", "Materials Science", "Computing"],
            notable_research=["Particle Physics", "Advanced Batteries", "AI"]
        )


@dataclass
class JPL(Institution):
    def __init__(self):
        super().__init__(
            name="Jet Propulsion Laboratory",
            institution_type=InstitutionType.RESEARCH_LAB.value,
            location="Pasadena, USA",
            founded=1936,
            website="https://www.jpl.nasa.gov",
            focus_areas=["Space Exploration", "Robotics", "Earth Observation"],
            notable_research=["Mars Rovers", "Voyager", "James Webb Telescope"]
        )


@dataclass
class CERN(Institution):
    def __init__(self):
        super().__init__(
            name="European Organization for Nuclear Research",
            institution_type=InstitutionType.RESEARCH_LAB.value,
            location="Geneva, Switzerland",
            founded=1954,
            website="https://home.cern",
            focus_areas=["Particle Physics", "Accelerator Science"],
            notable_research=["Higgs Boson", "Large Hadron Collider", "Antimatter"]
        )


# ===========================COMPANIES===============================================================================||
# ====================================================================================================================||


@dataclass
class SpaceX(Institution):
    def __init__(self):
        super().__init__(
            name="SpaceX",
            institution_type=InstitutionType.COMPANY.value,
            location="Hawthorne, USA",
            founded=2002,
            website="https://www.spacex.com",
            focus_areas=["Space Exploration", "Rocketry", "Satellites"],
            notable_research=["Falcon Rockets", "Starship", "Starlink"]
        )


@dataclass
class Tesla(Institution):
    def __init__(self):
        super().__init__(
            name="Tesla",
            institution_type=InstitutionType.COMPANY.value,
            location="Austin, USA",
            founded=2003,
            website="https://www.tesla.com",
            focus_areas=["Electric Vehicles", "Energy", "Battery Technology"],
            notable_research=["Autonomous Driving", "Solar Energy", "Megapack"]
        )


@dataclass
class Google(Institution):
    def __init__(self):
        super().__init__(
            name="Google",
            institution_type=InstitutionType.COMPANY.value,
            location="Mountain View, USA",
            founded=1998,
            website="https://www.google.com",
            focus_areas=["Search", "AI", "Cloud Computing", "Android"],
            notable_research=["Deep Learning", "Quantum Computing", "Self-Driving Cars"]
        )


@dataclass
class Microsoft(Institution):
    def __init__(self):
        super().__init__(
            name="Microsoft",
            institution_type=InstitutionType.COMPANY.value,
            location="Redmond, USA",
            founded=1975,
            website="https://www.microsoft.com",
            focus_areas=["Software", "Cloud Computing", "AI", "Gaming"],
            notable_research=["Azure AI", "Quantum Computing", "Mixed Reality"]
        )


@dataclass
class IBM(Institution):
    def __init__(self):
        super().__init__(
            name="IBM",
            institution_type=InstitutionType.COMPANY.value,
            location="Armonk, USA",
            founded=1911,
            website="https://www.ibm.com",
            focus_areas=["Computing", "AI", "Cloud", "Quantum"],
            notable_research=["Watson", "Quantum Computing", "Blockchain"]
        )


@dataclass
class Intel(Institution):
    def __init__(self):
        super().__init__(
            name="Intel",
            institution_type=InstitutionType.COMPANY.value,
            location="Santa Clara, USA",
            founded=1968,
            website="https://www.intel.com",
            focus_areas=["Semiconductors", "Computing", "AI"],
            notable_research=["Moore's Law", "Processor Architecture", "5G"]
        )


@dataclass
class NVIDIA(Institution):
    def __init__(self):
        super().__init__(
            name="NVIDIA",
            institution_type=InstitutionType.COMPANY.value,
            location="Santa Clara, USA",
            founded=1993,
            website="https://www.nvidia.com",
            focus_areas=["GPUs", "AI", "Gaming", "Autonomous Vehicles"],
            notable_research=["Deep Learning", "Ray Tracing", "CUDA"]
        )


@dataclass
class AppleCompany(Institution):
    def __init__(self):
        super().__init__(
            name="Apple",
            institution_type=InstitutionType.COMPANY.value,
            location="Cupertino, USA",
            founded=1976,
            website="https://www.apple.com",
            focus_areas=["Consumer Electronics", "Software", "Services"],
            notable_research=["iOS", "Silicon Chips", "AR/VR"]
        )


# ===========================EXPORTS===================================================================================||
# ====================================================================================================================||


__all__ = [
    # Universities
    'MIT', 'Stanford', 'Harvard', 'Caltech', 'Oxford', 'Cambridge', 'ETHZurich', 'Tsinghua',
    # Labs
    'NIST', 'LosAlamos', 'OakRidge', 'Argonne', 'JPL', 'CERN',
    # Companies
    'SpaceX', 'Tesla', 'Google', 'Microsoft', 'IBM', 'Intel', 'NVIDIA', 'AppleCompany',
]
