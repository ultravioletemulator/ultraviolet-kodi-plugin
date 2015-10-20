__author__ = 'developer'
import ultraviolet.PlatformProviderSpectrum
import ultraviolet.MetadataProviderWorldOfSpectrumScraper
import os
import ultraviolet.apputils


provider = ultraviolet.PlatformProviderSpectrum.PlatformProviderSpectrum()
metadataProvider = ultraviolet.MetadataProviderWorldOfSpectrumScraper.MetadataProviderWorldOfSpectrum()
metadataProvider.indexGames()