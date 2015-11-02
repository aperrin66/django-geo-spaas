import os
import numpy as np
import matplotlib.pyplot as plt

from django.db import models
from django.core.exceptions import ValidationError

from django.contrib.gis.geos import WKTReader
from django.conf import settings

from nansat import Nansat

from nansencloud.catalog.models import DataLocation
from nansencloud.catalog.models import Product as CatalogProduct


class Product(CatalogProduct):
    class Meta:
        proxy = True

    @classmethod
    def process(cls, dataset):
        ''' Run HAB processing '''
        dsUri = dataset.datalocation_set.filter(protocol='LOCALFILE')[0].uri
        dsBasename = os.path.split(dsUri)[1]
        prodBasename = dsBasename + 'chlor_a.png'
        prodFileName = os.path.join(settings.PROCESSING_HAB['outdir'], prodBasename)
        prodUrl = os.path.join(settings.PROCESSING_HAB['outhttp'], prodBasename)

        # actual 'processing'
        print 'PROCESSSS:', dsUri
        n = Nansat(dsUri)
        l = n[3]
        plt.imsave(prodFileName, l[::10, ::10])

        location = DataLocation.objects.get_or_create(protocol='HTTP',
                           uri=prodUrl,
                           dataset=dataset)[0]

        return CatalogProduct(
            short_name='chlor_a',
            standard_name='chlorophyll_surface',
            long_name='CHLOROPHYLL',
            units='mg -1',
            dataset=dataset,
            location=location)
