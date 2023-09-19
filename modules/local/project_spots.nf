process PROJECT_SPOTS{
    debug true
    tag "Projecting spots $meta"

    container 'wuennemannflorian/project_spots:latest'

    input:
    tuple val(meta), path(spots)
    path(img)

    output:
    tuple val(meta), path("${spots.baseName}.tiff"), emit: img_spots
    tuple val(meta), path("${spots.baseName}.channel_names.csv"), emit: channel_names

    script:
    """
    project_spots.dask.py \
    --input ${spots} \
    --sample_id ${spots.baseName} \
    --img_dims $img
    """
}
