__author__ = 'developer'
import PlatformProviderSpectrum
import MetadataProviderWorldOfSpectrum
import os
import apputils


provider = PlatformProviderSpectrum.PlatformProviderSpectrum()
metadataProvider = MetadataProviderWorldOfSpectrum.MetadataProviderWorldOfSpectrum()
metadataProvider.indexGames()