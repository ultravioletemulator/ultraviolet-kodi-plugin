__author__ = 'developer'
import ultraviolet.PlatformProviderSpectrum
import ultraviolet.MetadataProviderWorldOfSpectrum
import os
import ultraviolet.apputils


provider = ultraviolet.PlatformProviderSpectrum.PlatformProviderSpectrum()
metadataProvider = ultraviolet.MetadataProviderWorldOfSpectrum.MetadataProviderWorldOfSpectrum()
metadataProvider.indexGames()