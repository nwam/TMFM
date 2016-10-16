# Tone Mapping Feature Matcher
Input: pictures of the same scene at different exposure levels

Output: beautiful image with no under- or over-exposure

This program runs in two stages:

1. Feature Matching: pictures taken without a tripod are not perfectly aligned. This stage aligns the source photos.
2. Tone Mapping: this stage combines the data from all source images to yield a flattened hdri-esque image.

# TODO
* Feature Matching
* Ghosting removal
* More/better tone mapping functions
