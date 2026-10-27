---
title: "Distance Metrics"
description: Quantifying phenotypic change using mathematical distance.
---

Once images are converted to embeddings, we measure mathematical distance between them to quantify phenotypic change.

- **Low distance** = similar to the reference (e.g. no treatment effect).
- **High distance** = different from the reference (e.g. strong phenotypic change).

## Common methods

- **Euclidean vs cosine**: Euclidean measures absolute straight-line distance; cosine measures the angle between vectors (often better for high-dimensional embeddings because it ignores magnitude).
- **Centroid vs nearest**: compare each image to the **average** (centroid) of the reference group, or take the **minimum distance to any individual** reference image. A reference image is compared with the other reference images and stays in the returned table and plot.

For a complete guide, see [Common workflows](/PhenoMe/workflows/).
