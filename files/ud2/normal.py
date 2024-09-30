#!/usr/bin/env python3

from statistics import NormalDist

height_dist = NormalDist(mu=170, sigma=10)

# Probability of a person being taller than 160 cm and shorter than 180 cm
p = height_dist.cdf(180) - height_dist.cdf(160)
print("Probability of a person being taller than 160 cm and shorter than 180 cm:", p)

# Probability of a person being taller than 190 cm
p = 1 - height_dist.cdf(190)
print("Probability of a person being taller than 190 cm:", p)
